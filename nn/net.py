import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoid_prime(x):
    return x*(1-x)


class NeuralNet(object):
    def __init__(self, num_input, num_hidden, num_output):
        self.syn0 = 2*np.random.random((num_input, num_hidden)) - 1
        self.syn1 = 2*np.random.random((num_hidden, num_output)) - 1

    def forward(self, inpt):
        l1 = sigmoid(np.dot(inpt, self.syn0))
        l2 = sigmoid(np.dot(l1, self.syn1))

        return (inpt, l1, l2)

    def learn(self, inputs, outputs):
        l0, l1, l2 = self.forward(inputs)

        l2_error = outputs - l2
        l2_delta = l2_error * sigmoid_prime(l2)
        l1_error = np.dot(l2_delta, self.syn1.T)
        l1_delta = l1_error * sigmoid_prime(l1)

        self.syn0 += np.dot(l0.T, l1_delta)
        self.syn1 += np.dot(l1.T, l2_delta)

    def error(self, inputs, outputs):
        l0, l1, l2 = self.forward(inputs)

        l2_error = outputs - l2

        return np.mean(np.abs(l2_error))



net = NeuralNet(2, 3, 1)

inputs = np.array([[1,1],
                  [0,0],
                  [1,0],
                  [0,1]])

outputs = np.array([[0],
                    [0],
                    [1],
                    [1]])
print("untrained")
print("error: {}".format(net.error(inputs, outputs)))
for inpt in inputs:
    print(net.forward(inpt))

for i in xrange(1000):
    net.learn(inputs, outputs)

print("trained")
print("error: {}".format(net.error(inputs, outputs)))
for inpt in inputs:
    print(net.forward(inpt))
