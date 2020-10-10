# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-10.0,10.0,1000)
plt.ylim(0,5)
ft = np.exp(-0.6*t)
plt.plot(t,ft)
plt.subplot(221)
ft1 = np.exp(0.6*t)
plt.plot(t,ft1)
plt.show()