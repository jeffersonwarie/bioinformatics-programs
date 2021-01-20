import matplotlib.pyplot as plt
#import numpy as np
import sys
fin=open('Aaph_NJ8700_.wgs','r')
line=fin.readline()
initialstring=''
oneksetlist=[]

while len(line)>0:
    line=''
    line=fin.readline()
    line=line.rstrip()
    initialstring+=line

#print(initialstring)
count=0
nucleotidestring=''
skip=False
skipcount=0

for i in initialstring:
    #if count>1000:
        #print('test'+nucleotidestring)
    if skip==True and skipcount<=100:
        skipcount+=1
        continue
    if skip==True and skipcount>100:
        skip=False
        skipcount=0
    nucleotidestring+=i
    count+=1
    if (count%1000)==0:
        #print('test'+i+'test')
        oneksetlist.append(nucleotidestring)
        nucleotidestring=''
        skip=True

#print(oneksetlist)

Afreqlist=[]
Tfreqlist=[]
Cfreqlist=[]
Gfreqlist=[]

for onekstring in oneksetlist:
    Acount=0
    Tcount=0
    Ccount=0
    Gcount=0
    for i in onekstring:
        if i=='a':
            Acount+=1
        if i=='t':
            Tcount+=1
        if i=='c':
            Ccount+=1
        if i=='g':
            Gcount+=1
    Afreqlist.append(Acount)
    Tfreqlist.append(Tcount)
    Cfreqlist.append(Ccount)
    Gfreqlist.append(Gcount)

#print(Afreqlist)
#print(Tfreqlist)
#print(Cfreqlist)
#print(Gfreqlist)

Aminfreq=round(min(Afreqlist),-1)
Amaxfreq=round(max(Afreqlist),-1)
Afreqlist2=[]
for i in range(Aminfreq,Amaxfreq+1,10):
    k=0
    for j in Afreqlist:
        if j>=i and j<=(i+10):
            k+=1
    Afreqlist2.append(k)

Tminfreq=round(min(Tfreqlist),-1)
Tmaxfreq=round(max(Tfreqlist),-1)
Tfreqlist2=[]
for i in range(Tminfreq,Tmaxfreq+1,10):
    k=0
    for j in Tfreqlist:
        if j>=i and j<=(i+10):
            k+=1
    Tfreqlist2.append(k)

Cminfreq=round(min(Cfreqlist),-1)
Cmaxfreq=round(max(Cfreqlist),-1)
Cfreqlist2=[]
for i in range(Cminfreq,Cmaxfreq+1,10):
    k=0
    for j in Cfreqlist:
        if j>=i and j<=(i+10):
            k+=1
    Cfreqlist2.append(k)

Gminfreq=round(min(Gfreqlist),-1)
Gmaxfreq=round(max(Gfreqlist),-1)
Gfreqlist2=[]
for i in range(Gminfreq,Gmaxfreq+1,10):
    k=0
    for j in Gfreqlist:
        if j>=i and j<=(i+10):
            k+=1
    Gfreqlist2.append(k)

#print(len(Afreqlist))
#print(len(Tfreqlist))
#print(len(Cfreqlist))
#print(len(Gfreqlist))
x=[]
for i in range(1,len(Afreqlist)+1):
    x.append(i)
#x=np.array(x)
#Afreqlist=np.array(Afreqlist)
#Tfreqlist=np.array(Tfreqlist)
#Cfreqlist=np.array(Cfreqlist)
#Gfreqlist=np.array(Gfreqlist)

plt.plot(range(Aminfreq,Amaxfreq+1,10),Afreqlist2,label='A',linewidth=0.5)
plt.plot(range(Tminfreq,Tmaxfreq+1,10),Tfreqlist2,label='T',linewidth=0.5)
plt.plot(range(Cminfreq,Cmaxfreq+1,10),Cfreqlist2,label='C',linewidth=0.5)
plt.plot(range(Gminfreq,Gmaxfreq+1,10),Gfreqlist2,label='G',linewidth=0.5)
plt.legend()
plt.show()
