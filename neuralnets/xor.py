import numpy as np
from net import NeuralNet

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
    net.learn(inputs, outputs, 1.0)

print("trained")
print("error: {}".format(net.error(inputs, outputs)))
for inpt in inputs:
    print(net.forward(inpt))
