import numpy as np
import matplotlib.pyplot as plt

# noen startparametre
L = 1
N_lodd = 30

# posisjon til N_lodd legemer
r_x = np.linspace(0, L, N_lodd).reshape(-1, 1)
r_y = np.zeros_like(r_x)

# Vi kan sette massen og fjærkonstantene til hvert enkelt objekt på denne måten. Bruk indeksering for å endre for enkeltlegemer eller grupper av legemer.
m = np.ones_like(r_x)
# k = np.linspace(0.01, 10, N_lodd)
k = np.ones(N_lodd) * 2

# massen går fra 0.3 til 10 jevnt økende for hvert lodd, deretter snus rekkefølgen på denne, slik at den minker jevnt.
# m = np.linspace(.3, 10, N_lodd).reshape(-1, 1)[::-1]

# m[N_lodd // 2] = 10

# setter sammen x-koordinatene og y-koordinatene til en 2D posisjonsvektor
r = np.concatenate((r_x, r_y), axis=1)

# 2D hastighetsvektor
v = np.zeros_like(r)

# 2D kraftvektor
F = v.copy()

# r[N_lodd // 2, 1] = 1

# setter posisjonen til andre loddet til (0.1, 0.1)
r[1] = np.array([.1, .1])

# Noen tidsbetingelser
t = 0
dt = .1
tmax = 70

# main loop
while t < tmax:

    # utfører kraftutregningen på hvert objekt (utenom endepunktene)
    for n, pos in enumerate(r):

        # passer på at endepunktene ikke påvirkes
        if n == 0 or n == len(r) - 1:
            continue

        # regner krafta på hvert legeme
        F[n] = - k[n] * (pos - r[n - 1]) - k[n] * (pos - r[n + 1])

    # euler cromer
    v = v + F / m * dt
    r = r + v * dt

    # bruk denne for å kontinuerlig endre posisjonen til første lodd med en sinusfunksjon.
    # r[1, 1] = np.sin(t)

    # clf() tømmer forrige figur
    plt.clf()

    # grensene på plottet.
    plt.ylim(-2, 2)
    plt.xlim(-0.1, L + 0.1)

    # plotter posisjonene som prikker med linjer mellom
    plt.plot(*r.T, ".-")

    # setter en ventetid på 0.01 mellom hver oppdatering av plottet
    plt.pause(.01)

    t += dt
