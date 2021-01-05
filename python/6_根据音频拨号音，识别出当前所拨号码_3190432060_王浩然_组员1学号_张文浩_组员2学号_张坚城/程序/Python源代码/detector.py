#coding: UTF-8
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import argparse #argparse模块主要用来为脚本传递命令参数功能

#根据先前样本分析后得出的频率
dtmf = {(700, 1210): "1", (700, 1338): "2", (700, 1479): "3", (773, 1210): "4", (773, 1338): "5", (773, 1479): "6", (855, 1210): "7", (855, 1338): "8", (855, 1479): "9", (945, 1210): "*", (945, 1338): "0", (945, 1479): "#"}

#开始读取文件并处理
file = 'test//test.wav'
try:
    fps, data = wavfile.read(file)
except FileNotFoundError:
    print ("没有此文件:", file)
    exit()
except ValueError:
    print ("无法读取:", file)
    print("仅能读取wav文件.")
    exit()

else:
    if len(data.shape) == 2: 
        data = data.sum(axis=1)

precision = 0.17    #扫描精度
duration = len(data)/fps
step = int(len(data)//(duration//precision))
c = ""

try:
    for i in range(0, len(data)-step, step):
        signal = data[i:i+step]
        fourier = np.fft.fft(signal)
        frequencies = np.fft.fftfreq(signal.size, d=1/fps)

        #低频识别
        debut = np.where(frequencies > 0)[0][0]
        fin = np.where(frequencies > 1050)[0][0]
        freq = frequencies[debut:fin]
        amp = abs(fourier.real[debut:fin])
        lf = freq[np.where(amp == max(amp))[0][0]]
        delta = 20      #误差频率
        best = 0
        for f in [700, 773, 855, 945]:
            if abs(lf-f) < delta:
                delta = abs(lf-f)
                best = f

        lf = best

        #高频识别
        debut = np.where(frequencies > 1100)[0][0]
        fin = np.where(frequencies > 2000)[0][0]
        freq = frequencies[debut:fin]
        amp = abs(fourier.real[debut:fin])
        hf = freq[np.where(amp == max(amp))[0][0]]
        delta = 20     #误差频率
        best = 0
        for f in [1210, 1338, 1479]:
            if abs(hf-f) < delta:
                delta = abs(hf-f)
                best = f

        hf = best

        t = int(i//step * precision)
        if lf == 0 or hf == 0:
            c = ""
        elif dtmf[(lf,hf)] != c:
            c = dtmf[(lf,hf)]
            print(c, end='', flush=True)
    print()

except KeyboardInterrupt:
    print("\nCTRL+C退出...")
