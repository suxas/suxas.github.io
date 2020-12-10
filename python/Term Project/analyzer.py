#coding: UTF-8
import wave
import numpy as np
from matplotlib import pyplot as plt
 
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
    plt.subplot(211)
    plt.plot(time,wave_data[0],'r-')
    plt.xlabel('t/s')
    plt.ylabel(u'幅度')
    plt.title('Num '+num+' time/ampltitude')
    plt.subplot(212)
    plt.plot(freq,transformed,'b-')
    plt.xlabel('Freq/Hz')
    plt.ylabel('Ampltitude')
    plt.title('Num '+num+' freq/ampltitude')
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
    for i in np.arange(0,10):
        path='F:/github/suxas.github.io/python/Term Project/sample/num_'+str(i)+'.wav'
        max_freq,min_freq=wave_analysis(path)
        x.append(i)
        y.append(max_freq)
        x.append(i)
        y.append(min_freq)
        plt.scatter(x,y,marker='*')
    plt.show()
 
if __name__=='__main__':
    main()