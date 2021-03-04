#European call option value plot

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from bsm_option_valuation import BSM_call_value
mpl.rcParams['font.family'] = 'serif'

#model and option Parameters

K = 8000 #strike
T = 1.0 #time to maturity
r = 0.25 #sontant risk-less short rate
vol = 0.2 # constant volatility

#sample data generation
S = np.linspace(4000, 12000, 150)   #vestor of index level values

h = np.maximum(S-K, 0) #inner value Option
C = [BSM_call_value(S0,K, 0, T, r, vol) for S0 in S] #calculate call option Values

#graph output
#
plt.plot(S, h, 'b-.', lw=2.5, label = 'inner value')
plt.plot(S, C, 'r', lw=2.5, label='present value')
plt.grid(True)
plt.legend(loc=0)
plt.xlabel('index level $S_0')
plt.ylabel('present value $C(t=0)$')
plt.show()
