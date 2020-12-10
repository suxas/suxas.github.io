import wave  
import numpy as np  
from matplotlib import pyplot as plt  
  
#moving average  
def moving_average(data,n):  
    weights=np.ones(n)  
    weights/=weights.sum()  
    ma=np.convolve(data,weights,mode='full')[:len(data)]  
    ma[:n]=ma[n]  
    return ma  
  
  
          
#get wave data  
def get_wave_data(file_path):  
    f=wave.open(file_path,'rb')  
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
    return wave_data[0],framerate  
  
#find the efficient area in wave  
def find_efficient_area(wave_data):  
    wave_data=moving_average(wave_data,10)  
    wave_data=moving_average(wave_data,10)  
    wave_data=moving_average(wave_data,10)  
    wave_data=moving_average(wave_data,10)  
    new_data=[]  
    max_wave=wave_data.max()  
    efficient_data=[]  
    index=0  
    count=0  
    flag=False  
    for i in np.arange(0,len(wave_data)):  
        if abs(wave_data[i])>=0.05*max_wave:  
            new_data.append(wave_data[i])  
            index=0  
            if i+1>=len(wave_data):  
                break  
            if abs(wave_data[i+1])<0.05*max_wave:  
                for j in np.arange(1,60):  
                    if i+1+j>=len(wave_data):  
                        break  
                    if abs(wave_data[i+1+j])<0.05*max_wave:  
                        index+=1  
                if index>=59:   
                    flag=True  
                          
                  
                
        if flag==True:  
            if len(new_data)>2000:  
#                plt.plot(new_data,'r-')  
#                plt.show()  
                efficient_data.append(new_data)  
                count+=1  
            new_data=[]  
            index=0  
            flag=False  
    print ('Find ',count,' efficient wave') 
    return efficient_data,count  
  
#Analysis single wave data  
def wave_analysis_single(efficient_data,framerate):  
    time=np.arange(0,len(efficient_data[0]))*(1.0/framerate)  
#    plt.plot(time,efficient_data[0],'r-')  
#    plt.xlabel('Time/s')  
#    plt.ylabel('Ampltitude')  
#    plt.title(' time/ampltitude')  
#    plt.show()  
    df=framerate/(len(efficient_data[0])-1)  
    freq=[df*n for n in range(0,len(efficient_data[0]))]  
    transformed=np.fft.fft(efficient_data[0])  
    d=int(len(transformed)/2)  
    while freq[d]>2000:  
        d-=10  
    freq=freq[:d]  
    transformed=transformed[:d]  
    for i,data in enumerate(transformed):  
        transformed[i]=abs(data)  
    transformed=moving_average(transformed,5)  
    transformed=moving_average(transformed,5)  
    transformed=moving_average(transformed,5)  
#    transformed=moving_average(transformed,5)  
#    plt.plot(freq,transformed,'b-')  
#    plt.xlabel('Freq/Hz')  
#    plt.ylabel('Ampltitude')  
#    plt.title(' freq/ampltitude')  
#    plt.show()  
    #look for local maximum  
    local_max=[]  
    for i in np.arange(1,len(transformed)-1):  
        if transformed[i]>transformed[i-1] and transformed[i]>transformed[i+1]:  
            local_max.append(transformed[i])  
    local_max=sorted(local_max)  
    loc1=np.where(transformed==local_max[-1])  
    freq_1=freq[loc1[0][0]]  
    loc1=np.where(transformed==local_max[-2])  
    freq_2=freq[loc1[0][0]]  
    print ('Frequency',freq_1,freq_2)  
    return freq_1,freq_2  
          
          
  
  
#Get training data  
train_data={}  
for i in np.arange(0,10):  
    file_path='F:/github/suxas.github.io/python/Term Project/sample/num_'+str(i)+'.wav'  
    wave_data,framerate=get_wave_data(file_path)  
    data,count=find_efficient_area(wave_data)  
    a,b=wave_analysis_single(data,framerate)  
    train_data[i]=[a,b]  
  
  
  
#multi_number estimate  
def number_estimate(freq1,freq2):  
    err=100000  
    num=0  
    for i in np.arange(0,10):  
        tmp=(freq1-train_data[i][0])**2+(freq2-train_data[i][1])**2  
        if tmp<err:  
            err=tmp  
            num=i  
        else:  
            pass  
    return num  
      
      
#Analysis multi wave data  
def wave_analysis_multi(efficient_data,framerate):  
    num=[]  
    for data in efficient_data:  
        time=np.arange(0,len(data))*(1.0/framerate)  
        plt.plot(time,data,'r-')  
        plt.xlabel('Time/s')  
        plt.ylabel('Ampltitude')  
        plt.title(' time/ampltitude')  
        plt.show()  
        df=framerate/(len(data)-1)  
        freq=[df*n for n in range(0,len(data))]  
        transformed=np.fft.fft(data)  
        d=int(len(transformed)/2)  
        while freq[d]>2000:  
            d-=10  
        freq=freq[:d]  
        transformed=transformed[:d]  
        for i,data in enumerate(transformed):  
            transformed[i]=abs(data)  
        transformed=moving_average(transformed,5)  
        transformed=moving_average(transformed,5)     
        transformed=moving_average(transformed,5)  
        plt.plot(freq,transformed,'b-')  
        plt.xlabel('Freq/Hz')  
        plt.ylabel('Ampltitude')  
        plt.title(' freq/ampltitude')  
        plt.show()  

          
      
    print (num)  

          
file_path='F:/github/suxas.github.io/python/Term Project/sample/1145141919810.wav'  
wave_data,framerate=get_wave_data(file_path)  
data,count=find_efficient_area(wave_data)  
wave_analysis_multi(data,framerate)