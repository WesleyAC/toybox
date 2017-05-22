import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

# x_hat(k) = F * x_hat(k-1) + B*u(k)
# P(k) = F * P(k-1) * F_T + Q

# K' = P(k) * H_T * (H * P(k) * H_T + R)^-1
# x_hat'(k) = x_hat(k) + K'(z(k) - H * x_hat(k))
# P'(k) = P(k) - K' * H * P(k)

# Constants
# F - State transition matrix
# B - State input matrix
# Q - State covariance
# R - Input covariance

# Variables
# x_hat - Estimation of state vector
# P - Variacne of x_hat
# u - Control force
# z - Sensor readings
# K - Kalman gain


k = 1.0
c = 2.0
m = 4.0
Ac = np.asarray([[0,    1],
                 [-k/m, -c/m]])
Bc = np.asarray([[0],
                 [1/m]])
Cc = np.asarray([[1, 0]])
Dc = np.asarray([0])
dt = 1. / 200

F, B, _, _, _ = signal.cont2discrete((Ac, Bc, Cc, Dc), dt)

H = np.asarray([[1, 0],
                [0, 0]])

K = signal.place_poles(Ac, Bc, [-2.0, -3.0]).gain_matrix

Q = np.asarray([[0.01, 0.01],
                [0.01, 0.01]])

R = np.asarray([[0.05, 0.05],
                [0.05, 0.05]])

def run_controller_no_observer(y, prev_y):
    x_hat = np.copy(y)
    x_hat[1] = (y[0] - prev_y[0]) / dt
    u = np.dot(-K, x_hat)
    return u

prev_x_hat = [[5], [0]]
prev_u = 0
prev_P = [[0,0],[0,0]]

def run_controller_kalman(y, prev_y):
    global prev_x_hat
    global prev_u
    global prev_P
    x_hat = np.dot(F, prev_x_hat) + np.dot(B, prev_u)
    P = np.dot(np.dot(F, prev_P), F.T) + Q

    K_kal = np.dot(np.dot(P, H.T), (np.dot(np.dot(H, P), H.T) + R)**-1)
    x_hat = x_hat + np.dot(K_kal, y - np.dot(H, x_hat))
    P = P - np.dot(np.dot(K_kal, H), P)

    u = np.dot(-K, x_hat)

    prev_x_hat = np.copy(x_hat)
    prev_u = np.copy(u)
    prev_P = np.copy(P)

    return u

def sim(A, B, time, x0):
    x = np.asmatrix(x0)
    prev_y = np.dot(H, x)
    x_out = []
    x_hat_out = []
    u_out = []
    time_out = []

    for t in xrange(time):
        x_hat = x + ((np.random.random((2,1)) - 0.5) * 0.05)
        y = np.dot(H, x_hat)
        u = run_controller_kalman(y, prev_y)
        x = np.dot(A, x) + np.dot(B, u)

        x_out.append(x)
        x_hat_out.append(x_hat)
        u_out.append(u)
        time_out.append(t*dt)

        prev_y = np.copy(y)

    return (np.asarray(time_out), np.asarray(x_out), np.asarray(x_hat_out), np.asarray(u_out))

def plot(output):
    fig = plt.figure()
    ax = fig.add_subplot(111)

    plots = [[] for _ in range(len(output[1][0]) + len(output[2][0]) + len(output[3][0]))]
    for j,all_states in enumerate(np.vstack((output[1].T[0], output[2].T[0], output[3].T[0]))):
        for i,state in enumerate(all_states):
            plots[j].append(state)

    for i,plot in enumerate(plots):
        ax.plot(output[0], plot) #, label="x_{}".format(i))

    ax.legend()

    plt.show()

if __name__ == '__main__':
    plot(sim(F, B, 200*20, [[5], [0]]))

