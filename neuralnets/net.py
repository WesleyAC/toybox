import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoid_prime(x):
    return x*(1-x)

class NeuralNet(object):
    def __init__(self, num_input, num_hidden_layers, num_neurons_per_layer, num_output, seed=-1):
        if seed != -1:
            np.random.seed(seed)
        self.weights = []

        self.weights.append(2*np.random.random((num_input, num_neurons_per_layer)) - 1)

        for i in xrange(num_hidden_layers-1):
            self.weights.append(2*np.random.random((num_neurons_per_layer, num_neurons_per_layer)) - 1)

        self.weights.append(2*np.random.random((num_neurons_per_layer, num_output)) - 1)

    def forward(self, inpt):
        past_input = [inpt]
        for weight in self.weights:
            past_input.append(sigmoid(np.dot(past_input[-1], weight)))

        return past_input

    def learn(self, inputs, outputs, rate):
        results = self.forward(inputs)

        deltas = []

        output_error = outputs - results[-1]
        deltas.append(output_error * sigmoid_prime(results[-1]))

        for index,result in enumerate(reversed(results[:-1])):
            error = np.dot(deltas[-1], self.weights[-index-1].T)
            deltas.append(error* sigmoid_prime(result))

        deltas.reverse()

        for index,weight in enumerate(self.weights):
            weight += np.dot(results[index].T, deltas[index+1]) * rate

    def error(self, inputs, outputs):
        results = self.forward(inputs)

        output_error = outputs - results[-1]

        return np.mean(np.abs(output_error))

    def output_dot(self, error=None):
        output = []
        output.append("digraph {")
        for index,weight in enumerate(self.weights):
            if index == 0:
                prefix = "I"
                nextprefix = "H"
            elif index == len(self.weights)-1:
                prefix = "H"
                nextprefix = "O"
            else:
                prefix = "H"
                nextprefix = "H"
            for row in xrange(weight.shape[0]):
                for col in xrange(weight.shape[1]):
                    output.append("{}{} -> {}{} [color=\"{},{},0.6\"]".format(
                        prefix, row,
                        nextprefix, col,
                        0.0 if np.sign(weight[row][col]) == -1 else 0.7,
                        round((sigmoid(np.abs(weight[row][col]))-0.5)*2, 4),
                    ))
        if error is not None:
            output.append("error [label=\"Error:\n{}%\", shape=plaintext]".format(round(self.error(error[0], error[1])*100, 2)))
            output.append("O0 -> error [style=invis]")
            output.append("O{} -> error [style=invis]".format(self.weights[-1].shape[1]-1))
        output.append("}")
        return "\n".join(output)
