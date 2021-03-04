#european call option inner value plot
#
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['font.family'] = 'serif'

#option strike

K = 8000

#graphical output

S = np.linspace(7000, 9000, 100)    #index level values
h = np.maximum((S - K), 0)

plt.figure()
plt.plot(S, h, lw=2.5) #plot inner values of call option
plt.xlabel('index level $S_t$ at maturity')
plt.ylabel('inner value of european call option')
plt.grid(True)
plt.show()
