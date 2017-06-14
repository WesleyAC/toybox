import numpy as np

Kt = 1.41/89.0
Kv = 5840.0/3.0
G = 10.0
J = 4.0*(2.54**2.0)/2.0 # 4 kg on a 1 inch pully
R = 12.0/89.0

A = np.asarray([[0, 1],
                [0, -(Kt*Kv)/((G**2)*J*R)]])
B = np.asarray([[0],
                [Kt/(G*J*R)]])
