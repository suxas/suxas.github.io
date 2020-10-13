# -*- coding: utf-8 -*-
import numpy as np
import math
import matplotlib.pyplot as plt             #图表绘图
fig = plt.figure(figsize=(6, 4))            #新建图表
ax1 = fig.add_subplot(111)      

x=np.arange(-4,4,0.01)          
y=np.exp(x)

plt.rcParams['font.sans-serif']=['SimHei'] 
plt.rcParams['axes.unicode_minus']=False 

ax1.spines['right'].set_color('none')
ax1.spines['top'].set_color('none')
ax1.xaxis.set_ticks_position('bottom')
ax1.spines['bottom'].set_position(('data', 0))
ax1.yaxis.set_ticks_position('left')
ax1.spines['left'].set_position(('data',0))

plt.title(r'$f(x)=e^x$') 
plt.plot(x,y)
plt.show()