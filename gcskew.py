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

for i in initialstring:
    #if count>1000:
        #print('test'+nucleotidestring)
    nucleotidestring+=i
    count+=1
    if (count%1000)==0:
        #print('test'+i+'test')
        oneksetlist.append(nucleotidestring)
        nucleotidestring=''

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
        if i=='a' or i=='A':
            Acount+=1
        if i=='t' or i=='T':
            Tcount+=1
        if i=='c' or i=='C':
            Ccount+=1
        if i=='g' or i=='G':
            Gcount+=1
    Afreqlist.append(Acount)
    Tfreqlist.append(Tcount)
    Cfreqlist.append(Ccount)
    Gfreqlist.append(Gcount)

GCskewlist=[]
ATskewlist=[]

for i in range(len(Afreqlist)):
    if (Gfreqlist[i]+Cfreqlist[i])>0:
        GCskewlist.append((Gfreqlist[i]-Cfreqlist[i])/(Gfreqlist[i]+Cfreqlist[i]))
    else:
        GCskewlist.append(0)
    if (Afreqlist[i]+Tfreqlist[i])>0:
        ATskewlist.append((Afreqlist[i]-Tfreqlist[i])/(Afreqlist[i]+Tfreqlist[i]))
    else:
        ATskewlist.append(0)

print(len(Afreqlist))
print(len(Tfreqlist))
print(len(Cfreqlist))
print(len(Gfreqlist))

GCskewsumlist=[]
GCskewsumlist.append(GCskewlist[0])
ATskewsumlist=[]
ATskewsumlist.append(ATskewlist[0])

for i in range(1,len(GCskewlist)):
    GCskewsumlist.append(GCskewlist[i]+GCskewsumlist[i-1])

for i in range(1,len(ATskewlist)):
    ATskewsumlist.append(ATskewlist[i]+ATskewsumlist[i-1])

plt.plot(range(len(GCskewsumlist)),GCskewsumlist,label='GC Skew',linewidth=1)
plt.plot(range(len(ATskewsumlist)),ATskewsumlist,label='AT skew',linewidth=1)
plt.legend()
plt.show()
