# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei'] 
plt.rcParams['axes.unicode_minus']=False 

plt.subplot(111)
y=[1,0,0,0,0,0,0,0,0]
plt.stem(y)
plt.grid(True)
plt.title('单位脉冲序列')

plt.show()