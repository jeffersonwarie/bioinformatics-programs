import matplotlib.pyplot as plt
import re
import sys
fin1=open('NC_000913.txt','r')
fin2=open('NC_011748.txt','r')
#fin1=open('genomeannotationex1.txt','r')
#fin2=open('genomeannotationex2.txt','r')

genecoordinatelist1=[]
genecoordinatelist2=[]
coordinate1=0
coordinate2=0

line=fin1.readline()
line=''
line=fin1.readline()
line=''
line=fin1.readline()
line=''
line=fin1.readline()

coordinate1=0
coordinate2=0
genename=''
count=0
while len(line)>0:
    line=re.sub(r'\s+',' ',line).strip()
    for i in range(len(line)):
        if line[i]=='.':
            break
        elif line[i]>='0' and line[i]<='9':
            coordinate1=coordinate1*10+int(line[i],10)
        else:
            print('startERROR!')
            sys.exit()
    while i<len(line):
        if line[i]=='+' or line[i]=='-' or line[i]==' ':
            break
        elif line[i]=='.':
            pass
        elif line[i]>='0' and line[i]<='9':
            coordinate2=coordinate2*10+int(line[i],10)
        else:
            print(line)
            print(coordinate2)
            print('endERROR!')
            sys.exit()
        i+=1
    while i<len(line):
        if (line[i]>='0' and line[i]<='9') or line[i]=='+' or line[i]=='-' or line[i]==' ':
            pass
        else:
            break
        i+=1
    while i<len(line):
        if i<=(len(line)-2):
            if line[i]==' ':
                break
            elif (line[i]>='a' and line[i]<='z') or (line[i]>='A' and line[i]<='Z') or (line[i]>='0' and line[i]<='9') or line[i]=='-' or line[i]=='_':
                genename+=line[i]
            else:
                print(line)
                print(genename)
                print(line[i])
                print('geneERROR!')
                sys.exit()
        i+=1
    genecoordinatelist1.append([coordinate1,coordinate2,genename])
    coordinate1=0
    coordinate2=0
    genename=''
    line=''
    line=fin1.readline()

#print(genecoordinatelist1)

line=fin2.readline()
line=''
line=fin2.readline()
line=''
line=fin2.readline()
line=''
line=fin2.readline()

coordinate1=0
coordinate2=0
genename=''
count=0
while len(line)>0:
    line=re.sub(r'\s+',' ',line).strip()
    for i in range(len(line)):
        if line[i]=='.':
            break
        elif line[i]>='0' and line[i]<='9':
            coordinate1=coordinate1*10+int(line[i],10)
        else:
            print('startERROR!')
            sys.exit()
    while i<len(line):
        if line[i]=='+' or line[i]=='-' or line[i]==' ':
            break
        elif line[i]=='.':
            pass
        elif line[i]>='0' and line[i]<='9':
            coordinate2=coordinate2*10+int(line[i],10)
        else:
            print(line)
            print(coordinate2)
            print('endERROR!')
            sys.exit()
        i+=1
    while i<len(line):
        if (line[i]>='0' and line[i]<='9') or line[i]=='+' or line[i]=='-' or line[i]==' ':
            pass
        else:
            break
        i+=1
    while i<len(line):
        if i<=(len(line)-2):
            if line[i]==' ':
                break
            elif (line[i]>='a' and line[i]<='z') or (line[i]>='A' and line[i]<='Z') or (line[i]>='0' and line[i]<='9') or line[i]=='-' or line[i]=='_':
                genename+=line[i]
            else:
                print(line)
                print(genename)
                print(line[i])
                print('geneERROR!')
                sys.exit()
        i+=1
    genecoordinatelist2.append([coordinate1,coordinate2,genename])
    coordinate1=0
    coordinate2=0
    genename=''
    line=''
    line=fin2.readline()

#print(genecoordinatelist2)

for i in range(len(genecoordinatelist1)):
    plt.plot([genecoordinatelist1[i][0],genecoordinatelist1[i][1]],[10,10],linewidth=8)
for i in range(len(genecoordinatelist2)):
    plt.plot([genecoordinatelist2[i][0],genecoordinatelist2[i][1]],[0,0],linewidth=8)
for i in range(len(genecoordinatelist1)):
    for j in range(len(genecoordinatelist2)):
        if genecoordinatelist1[i][2]==genecoordinatelist2[j][2]:
            plt.plot([genecoordinatelist1[i][0],genecoordinatelist2[j][0]],[10,0],linewidth=0.5)
plt.show()
