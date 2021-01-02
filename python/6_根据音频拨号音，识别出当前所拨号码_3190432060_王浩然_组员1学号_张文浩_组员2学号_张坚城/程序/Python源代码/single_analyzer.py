#coding: UTF-8
import wave
import numpy as np
import window
import sys
from matplotlib import pyplot as plt
#图表中文
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

def wave_analysis(file_path):
    f=wave.open(file_path,'rb')
    num=file_path[-5] 
    params=f.getparams()
    nchannels,samplewidth,framerate,nframes=params[:4]
    str_data=f.readframes(nframes)
    f.close()
    wave_data=np.fromstring(str_data,dtype=np.short)
    wave_data.shape=-1,1
    if nchannels==2:
        wave_data.shape=-1,2
    else:
        pass
    wave_data=wave_data.T
    time=np.arange(0,nframes)*(1.0/framerate)
    df=framerate/(nframes-1)
    freq=[df*n for n in range(0,nframes)]
    transformed=np.fft.fft(wave_data[0])
    d=int(len(transformed)/2)
    while freq[d]>4000:
        d-=10
    freq=freq[:d]
    transformed=transformed[:d]
    for i,data in enumerate(transformed):
        transformed[i]=abs(data)
    plt.plot(time,wave_data[0],'r-')
    plt.xlabel('时间/秒')
    plt.ylabel(u'振幅')
    plt.title('时域振幅图')
    plt.show()
    plt.plot(freq,transformed,'b-')
    plt.xlabel('频率/赫兹')
    plt.ylabel(u'振幅')
    plt.title('频域振幅图')
    local_max=[]
    for i in np.arange(1,len(transformed)-1):
        if transformed[i]>transformed[i-1] and transformed[i]>transformed[i+1]:
            local_max.append(transformed[i])
    local_max=sorted(local_max)
    loc1=np.where(transformed==local_max[-1])
    max_freq=freq[loc1[0][0]]
    loc1=np.where(transformed==local_max[-2])
    min_freq=freq[loc1[0][0]]
    plt.show()
    return max_freq,min_freq
    

def main():
    x=[]
    y=[]
    path='C://Users//Suxas//Desktop//6_根据音频拨号音，识别出当前所拨号码_3190432060_王浩然_组员1学号_张文浩_组员2学号_张坚城//程序//Python源代码//test_new.wav'
    max_freq,min_freq=wave_analysis(path)
    plt.show()
 
if __name__=='__main__':
    main()