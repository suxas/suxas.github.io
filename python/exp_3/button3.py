# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei'] 
plt.rcParams['axes.unicode_minus']=False 

x=np.linspace(0,8,10)
plt.subplot(111)
A=2
a=0.6
y=A*a**x
plt.grid(True)
plt.title('实指数信号')
plt.stem(x,y)

plt.show()