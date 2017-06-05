import numpy as np
from net import NeuralNet

net = NeuralNet(2, 1, 3, 1, 342047)
output_dot = False

inputs = np.array([[1,1],
                   [0,0],
                   [1,0],
                   [0,1]])

outputs = np.array([[0],
                    [0],
                    [1],
                    [1]])

for i in xrange(80000):
    if i % 100 == 0:
        print("epoch: {}\terror: {}".format(i, net.error(inputs, outputs)))
        if output_dot:
            open("/tmp/xor{:05d}graph".format(i), mode="w").write(net.output_dot((inputs,outputs)))
    net.learn(inputs, outputs, 0.05)

print("trained")
print("error: {}".format(net.error(inputs, outputs)))
for inpt in inputs:
    print(net.forward(inpt))
