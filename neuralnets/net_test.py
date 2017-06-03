from net import NeuralNet
import numpy as np

#TODO(Wesley) More tests

class TestNeuralNet(object):
    def test_zero_system(self):
        net = NeuralNet(3, 2, 4, 1, seed=0)
        net.weights = [ np.zeros((3,4)),
                        np.zeros((4,4)),
                        np.zeros((4,4)),
                        np.zeros((4,1)) ]
        inpt = np.asarray([1, 1, 1])
        print(net.forward(inpt))
        for layer in net.forward(inpt)[1:]:
            for neuron in layer:
                assert neuron == 0.5
