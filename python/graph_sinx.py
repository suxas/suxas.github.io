# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt             #图表绘图
fig = plt.figure(figsize=(6, 4))            #新建图表
ax1 = fig.add_subplot(111)                  #新建坐标轴

x=np.arange(-2*np.pi,2*np.pi,0.01)          #-2pi到2pi为区间 每0.01描点
y=np.sin(x)                                 #绘制函数sin(x)

plt.rcParams['font.sans-serif']=['SimHei'] 
plt.rcParams['axes.unicode_minus']=False 

ax1.spines['right'].set_color('none')
ax1.spines['top'].set_color('none')
ax1.xaxis.set_ticks_position('bottom')
ax1.spines['bottom'].set_position(('data', 0))
ax1.yaxis.set_ticks_position('left')
ax1.spines['left'].set_position(('data',0))

plt.title(r'$f(x)=sin x$') 
plt.plot(x,y)
plt.show()
