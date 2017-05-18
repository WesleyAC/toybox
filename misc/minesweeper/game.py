"""
Trains an agent with (stochastic) Policy Gradients on MineSweeper.
Stolen from https://gist.github.com/karpathy/a4166c7fe253700972fcbc77e4ea32c5
And https://gist.github.com/etienne87/6803a65653975114e6c6f08bb25e1522
"""
import numpy as np
import minesweeper as ms
import cPickle as pickle

# hyperparameters
H = 200 # number of hidden layer neurons
batch_size = 10 # every how many episodes to do a param update?
learning_rate = 1e-4
gamma = 0.99 # discount factor for reward
decay_rate = 0.99 # decay factor for RMSProp leaky sum of grad^2
resume = False # resume from previous checkpoint?

# model initialization
DI = 10 * 10 * 9 # input dimensionality
DO = 10 * 10 # output dimensionality
if resume:
    model = pickle.load(open('save.p', 'rb'))
else:
    model = {}
    model['W1'] = np.random.randn(DI,H) / np.sqrt(DI) # "Xavier" initialization
    model['W2'] = np.random.randn(H,DO) / np.sqrt(H)

grad_buffer = { k : np.zeros_like(v) for k,v in model.iteritems() } # update buffers that add up gradients over a batch
rmsprop_cache = { k : np.zeros_like(v) for k,v in model.iteritems() } # rmsprop memory

def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x)) # sigmoid "squashing" function to interval [0,1]

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()

def discount_rewards(r):
    """ take 1D float array of rewards and compute discounted reward """
    discounted_r = np.zeros_like(r)
    running_add = 0
    for t in reversed(xrange(0, r.size)):
        # if r[t] != 0: running_add = 0 # reset the sum, since this was a game boundary (pong specific!)
        running_add = running_add * gamma + r[t]
        discounted_r[t] = running_add
    return discounted_r

def policy_forward(x):
    if(len(x.shape)==1):
        x = x[np.newaxis,...]
    h = x.dot(model['W1'])
    h[h<0] = 0 # ReLU nonlinearity
    logp = h.dot(model['W2'])
    p = softmax(logp)
    return p, h # return probability of taking each action, and hidden state

def policy_backward(eph, epdlogp):
    """ backward pass. (eph is array of intermediate hidden states) """
    # dW2 = np.dot(eph.T, epdlogp).ravel()
    # dh = np.outer(epdlogp, model['W2'])
    # dh[eph <= 0] = 0 # backpro prelu
    # dW1 = np.dot(dh.T, epx)
    dW2 = eph.T.dot(epdlogp)
    dh = epdlogp.dot(model['W2'].T)
    dh[eph <= 0] = 0 # backpro prelu
    dW1 = epx.T.dot(dh)

    return {'W1':dW1, 'W2':dW2}

game = ms.Game(10, 10, 0.1)
x = np.asarray(game.output_ml())
xs,hs,dlogps,drs = [],[],[],[]
episode_number = 0
batch_reward = 0
while True:
    x = np.asarray(game.output_ml())

    # forward the policy network and sample an action from the returned probability
    aprob, h = policy_forward(x)
    u = np.random.uniform()
    aprob_cum = np.cumsum(aprob)
    action = np.where(u <= aprob_cum)[0][0]

    # record various intermediates (needed later for backprop)
    xs.append(x) # observation
    hs.append(h) # hidden state

    dlogsoftmax = aprob.copy()
    dlogsoftmax[0,action] -= 1 #-discounted reward
    dlogps.append(dlogsoftmax) # grad that encourages the action that was taken to be taken (see http://cs231n.github.io/neural-networks-2/#losses if confused)

    # step the environment and get new measurements

    game.move(action / 10, action % 10)
    reward = game.get_reward()
    done = game.game_over()

    drs.append(reward) # record reward (has to be done after we call step() to get reward for previous action)

    if done: # an episode finished
        batch_reward += reward
        episode_number += 1

        # stack together all inputs, hidden states, action gradients, and rewards for this episode
        epx = np.vstack(xs)
        eph = np.vstack(hs)
        epdlogp = np.vstack(dlogps)
        epr = np.vstack(drs)
        xs,hs,dlogps,drs = [],[],[],[] # reset array memory

        # compute the discounted reward backwards through time
        discounted_epr = discount_rewards(epr)

        # standardize the rewards to be unit normal (helps control the gradient estimator variance)
        discounted_epr -= np.mean(discounted_epr)
        if np.std(discounted_epr) != 0:
            discounted_epr /= np.std(discounted_epr)

        epdlogp *= discounted_epr # modulate the gradient with advantage (PG magic happens right here.)
        grad = policy_backward(eph, epdlogp)
        for k in model: grad_buffer[k] += grad[k] # accumulate grad over batch

        # perform rmsprop parameter update every batch_size episodes
        if episode_number % batch_size == 0:
            for k,v in model.iteritems():
                g = grad_buffer[k] # gradient
                rmsprop_cache[k] = decay_rate * rmsprop_cache[k] + (1 - decay_rate) * g**2
                model[k] += learning_rate * g / (np.sqrt(rmsprop_cache[k]) + 1e-5)
                grad_buffer[k] = np.zeros_like(v) # reset batch gradient buffer
            print("batch {} finished, reward avg: {}".format(episode_number / batch_size, batch_reward / batch_size))
            batch_reward = 0

        # boring book-keeping
        if episode_number % 100 == 0: pickle.dump(model, open('save.p', 'wb'))
        game = ms.Game(10, 10, 0.1)
        x = np.asarray(game.output_ml())

        # print ('ep %d: game finished, reward: %f' % (episode_number, reward))
