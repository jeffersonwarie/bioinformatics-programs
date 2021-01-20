fin=open('testdata.wgs','r')
line=fin.readline()
initialstring=''

while len(line)>0:
    line=''
    line=fin.readline()
    line=line.rstrip()
    initialstring+=line

print(initialstring)
finalstring=''

for i in initialstring:
    if i=='a':
        finalstring+='t'
    if i=='t':
        finalstring+='a'
    if i=='c':
        finalstring+='g'
    if i=='g':
        finalstring+='c'

print(finalstring)

