#coding: UTF-8
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import argparse

dtmf = {(695, 1209): "1", (695, 1331): "2", (695, 1475): "3", (766, 1209): "4", (766, 1331): "5", (766, 1475): "6", (846, 1209): "7", (846, 1331): "8", (846, 1475): "9", (934, 1209): "*", (934, 1331): "0", (934, 1475): "#"}


parser = argparse.ArgumentParser(description="DTMF双音多频信号识别器")
parser.add_argument("-t", type=int, metavar="F", default=20)
parser.add_argument("-i", type=float, metavar='T', default=0.08)
parser.add_argument('file', type=argparse.FileType('r'))

args = parser.parse_args()

file = args.file.name
try:
    fps, data = wavfile.read(file)
except FileNotFoundError:
    print ("No such file:", file)
    exit()
except ValueError:
    print ("Impossible to read:", file)
    print("Please give a wav file.")
    exit()

else:
    if len(data.shape) == 2: 
        data = data.sum(axis=1) # stereo

precision = args.i
duration = len(data)/fps
step = int(len(data)//(duration//precision))
c = ""

try:
    for i in range(0, len(data)-step, step):
        signal = data[i:i+step]
        fourier = np.fft.fft(signal)
        frequencies = np.fft.fftfreq(signal.size, d=1/fps)

        #低频
        debut = np.where(frequencies > 0)[0][0]
        fin = np.where(frequencies > 1050)[0][0]
        freq = frequencies[debut:fin]
        amp = abs(fourier.real[debut:fin])
        lf = freq[np.where(amp == max(amp))[0][0]]
        delta = args.t
        best = 0
        for f in [695, 766, 846, 934]:
            if abs(lf-f) < delta:
                delta = abs(lf-f)
                best = f

        lf = best

        #高频
        debut = np.where(frequencies > 1100)[0][0]
        fin = np.where(frequencies > 2000)[0][0]
        freq = frequencies[debut:fin]
        amp = abs(fourier.real[debut:fin])
        hf = freq[np.where(amp == max(amp))[0][0]]
        delta = args.t
        best = 0
        for f in [1209, 1331, 1475]:
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