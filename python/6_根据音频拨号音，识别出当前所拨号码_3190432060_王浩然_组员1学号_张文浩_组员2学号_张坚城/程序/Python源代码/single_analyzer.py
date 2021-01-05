#coding: UTF-8
import wave
import numpy as np
import sys
from matplotlib import pyplot as plt
#图表中文
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

def wave_analysis(file_name):
    #读取音频
    f=wave.open(file_name,'rb')     #读取wave文件 'rb'：读取模式
    params=f.getparams()
    nchannels,samplewidth,framerate,nframes=params[:4]      #读取wave文件的声道数，量化位数，采样频率，采样点数
    str_data=f.readframes(nframes)      #读取音频，字符串格式
    f.close()
    #开始处理音频
    wave_data=np.fromstring(str_data,dtype=np.short)    #将字符串转为整型，准备进行计算
    #根据文件通道数量修改数组的列数
    wave_data.shape=-1,1        
    if nchannels==2:
        wave_data.shape=-1,2
    else:
        pass

    wave_data=wave_data.T       #数组转置    
    time=np.arange(0,nframes)*(1.0/framerate)       #通过取样点数和取样频率计算出每个取样的时间
    df=framerate/(nframes-1)        #开始采样位置
    freq=[df*n for n in range(0,nframes)]       #分辨率
    transformed=np.fft.fft(wave_data[0])        #使用fft函数进行傅里叶变换
    d=int(len(transformed)/2)

    #删去频率大于4000Hz的范围
    while freq[d]>4000:
        d-=10
    freq=freq[:d]
    transformed=transformed[:d]
    #取y轴正方向振幅
    for i,data in enumerate(transformed):
        transformed[i]=abs(data)

    #生成图像
    plt.plot(time,wave_data[0],'r-')
    plt.xlabel('时间/秒')
    plt.ylabel(u'振幅')
    plt.title('时域振幅图')
    plt.show()
    plt.plot(freq,transformed,'b-')
    plt.xlabel('频率/赫兹')
    plt.ylabel(u'振幅')
    plt.title('频域振幅图')
    plt.show()

def main():
    x=[]
    y=[]
    file_name='test//test_new.wav'
    wave_analysis(file_name)
    plt.show()
 
if __name__=='__main__':
    main()