# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei'] 
plt.rcParams['axes.unicode_minus']=False 

x=np.linspace(0,5,20)
plt.subplot(111)
y2=2*np.sin(0.5*np.pi*x+2)
plt.title('正弦信号')
plt.grid(True)
plt.stem(x,y2)

plt.show()