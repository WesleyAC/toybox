import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoid_prime(x):
    return x*(1-x)


class NeuralNet(object):
    def __init__(self, num_input, num_hidden_layers, num_neurons_per_layer, num_output):
        self.synapses = []

        self.synapses.append(2*np.random.random((num_input, num_neurons_per_layer)) - 1)

        for i in xrange(num_hidden_layers-1):
            self.synapses.append(2*np.random.random((num_neurons_per_layer, num_neurons_per_layer)) - 1)

        self.synapses.append(2*np.random.random((num_neurons_per_layer, num_output)) - 1)

    def forward(self, inpt):
        past_input = [inpt]
        for synapse in self.synapses:
            past_input.append(sigmoid(np.dot(past_input[-1], synapse)))

        return past_input

    def learn(self, inputs, outputs):
        results = self.forward(inputs)

        deltas = []

        output_error = outputs - results[-1]
        deltas.append(output_error * sigmoid_prime(results[-1]))

        for index,result in enumerate(reversed(results[:-1])):
            error = np.dot(deltas[-1], self.synapses[-index-1].T)
            deltas.append(error* sigmoid_prime(result))

        deltas.reverse()

        for index,synapse in enumerate(self.synapses):
            synapse += np.dot(results[index].T, deltas[index+1])

    def error(self, inputs, outputs):
        results = self.forward(inputs)

        output_error = outputs - results[-1]

        return np.mean(np.abs(output_error))


net = NeuralNet(2, 1, 3, 1)

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

for i in xrange(100000):
    net.learn(inputs, outputs)

print("trained")
print("error: {}".format(net.error(inputs, outputs)))
for inpt in inputs:
    print(net.forward(inpt))
