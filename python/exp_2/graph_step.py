# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] 
plt.rcParams['axes.unicode_minus']=False 

fig = plt.figure(figsize=(6, 4))            #新建图表
ax1 = fig.add_subplot(111)  

def function(t):
     r=np.where(t>0.0,2.0,0.0)
     return r
t=np.linspace(-2.0,3.0,10000)

ax1.spines['right'].set_color('none')
ax1.spines['top'].set_color('none')
ax1.xaxis.set_ticks_position('bottom')
ax1.spines['bottom'].set_position(('data', 0))
ax1.yaxis.set_ticks_position('left')
ax1.spines['left'].set_position(('data',0))

plt.ylim(-1.0,3.0)
plt.title('阶跃信号') 
plt.plot(t,function(t))
plt.show()