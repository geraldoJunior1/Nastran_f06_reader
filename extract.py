import numpy as np
import matplotlib.pyplot as plt

def extract(a):
        
    path =  'teste.f06' #./
    fileID = open(path,'r')
    tline = fileID.readline()

    l=10000000
    k=10000000
    flt = 10000000
    x=10000000
    alicate=1
    point=0
    vel_point = np.zeros((36,1))
    damp_point = np.zeros((36,1))
    freq_point = np.zeros((36,1))
    vel = []
    damp = []
    freq = []
    vel_point = []
    damp_point = []
    freq_point = []
    while  tline:

        a=tline

        design=a.find('FLUTTER  SUMMARY')

        if design!=-1:
            l=1
        else:
            l=l+1

        if l==3:
            point = int(a[17:20])

        if l==7:
            x=1

        if x<=36:
            vel_point.append(float(a[58:69]))
            damp_point.append(float(a[70:83]))
            freq_point.append(float(a[86:97]))

            x=x+1

        if point != alicate and x>36:

            vel.append(vel_point)
            damp.append(damp_point)
            freq.append(freq_point)

            vel_point = []
            damp_point = []
            freq_point = []

        alicate = point

        tline = fileID.readline()

    fileID.close()
    return vel, damp, freq

vel, damp, freq = extract('1')

x=8

symbols = ['o', 's', 'd', '^', 'v', '*', 'P', 'h']

n_mechs = 8

for i in range(n_mechs):

    plt.subplot(211)
    plt.plot(vel[7],freq[x],marker=symbols[i], markersize=4.5, linewidth=1)
    plt.xlim(0,40)
    #axs[0].set_title('')
    plt.xlabel('Velocidade (m/s)')
    plt.ylabel('Frequência (Hz)')


    plt.subplot(212)
    plt.axhline(y=0, color='black')
    plt.axvline(x=32, linewidth=1.5, color='red')
    plt.plot(vel[7],damp[x],marker=symbols[i], markersize=4.5, linewidth=1)
    plt.xlim(0,40)
    plt.ylim(-0.5,0.5)
    
    plt.xlabel('Velocidade (m/s)')
    plt.ylabel('Amortecimento')
    x=x+1


plt.show()

    