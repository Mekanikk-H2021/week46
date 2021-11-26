import numpy as np
import matplotlib.pyplot as plt

L = 1
N_lodd = 30

# posisjon
r_x = np.linspace(0, L, N_lodd).reshape(-1, 1)
r_y = np.zeros_like(r_x)

m = np.ones_like(r_x)
# k = np.linspace(0.01, 10, N_lodd)
k = np.ones(N_lodd) * 2

# m = np.linspace(.3, 10, N_lodd).reshape(-1, 1)[::-1]

# m[N_lodd // 2] = 10

r = np.concatenate((r_x, r_y), axis=1)

v = np.zeros_like(r)
F = v.copy()

# r[N_lodd // 2, 1] = 1
r[1] = np.array([.1, .1])

t = 0
dt = .1
tmax = 70

while t < tmax:

    for n, pos in enumerate(r):
        if n == 0 or n == len(r) - 1:
            continue
        F[n] = - k[n] * (pos - r[n - 1]) - k[n] * (pos - r[n + 1])

    v = v + F / m * dt
    r = r + v * dt

    # r[1, 1] = np.sin(t)

    plt.clf()
    plt.ylim(-2, 2)
    plt.xlim(-0.1, L + 0.1)
    plt.plot(*r.T, ".-")
    plt.pause(.01)

    t += dt
