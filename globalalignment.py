seq1='ACAGTAG'
seq2='ACTCG'

match=1
mismatch=0
gap=-1

scoringmatrix=[]
routematrix=[]

for i in range(len(seq1)+1):
    row=[]
    routerow=[]
    for j in range(len(seq2)+1):
        row.append(0)
        routerow.append('unknown')
    scoringmatrix.append(row)
    routematrix.append(routerow)

for i in range(len(seq1)+1):
    if i==0:
        continue
    else:
        scoringmatrix[i][0]=scoringmatrix[i-1][0]+gap
        routematrix[i][0]='top'

for i in range(len(seq2)+1):
    if i==0:
        continue
    else:
        scoringmatrix[0][i]=scoringmatrix[0][i-1]+gap
        routematrix[0][i]='left'

i=1
diagonalvalue=0
topvalue=0
leftvalue=0

while i<len(seq1)+1:
    j=1
    while j<len(seq2)+1:
        if seq1[i-1]==seq2[j-1]:
            diagonalvalue=scoringmatrix[i-1][j-1]+match
        else:
            diagonalvalue=scoringmatrix[i-1][j-1]+mismatch
        topvalue=scoringmatrix[i-1][j]+gap
        leftvalue=scoringmatrix[i][j-1]+gap
        if diagonalvalue>=topvalue and diagonalvalue>=leftvalue:
            scoringmatrix[i][j]=diagonalvalue
            routematrix[i][j]='diagonal'
        if topvalue>=diagonalvalue and topvalue>=leftvalue:
            scoringmatrix[i][j]=topvalue
            routematrix[i][j]='top'
        if leftvalue>=diagonalvalue and leftvalue>=topvalue:
            scoringmatrix[i][j]=leftvalue
            routematrix[i][j]='left'
        j+=1
    i+=1

print('The scoring matrix:')   
for i in range(len(seq1)+1):
    for j in range(len(seq2)+1):
        print(scoringmatrix[i][j],end=' ')
    print()

print()
print('The route matrix:')
for i in range(len(seq1)+1):
    for j in range(len(seq2)+1):
        print(routematrix[i][j],end=' ')
    print()

maxrowindex=0
maxcolindex=0
maxvalue=0

for i in range(len(seq1)+1):
    for j in range(len(seq2)+1):
        if maxvalue>=scoringmatrix[i][j]:
            maxvalue=scoringmatrix[i][j]

for i in range(len(seq1)+1):
    for j in range(len(seq2)+1):
        if maxvalue<=scoringmatrix[i][j]:
            maxvalue=scoringmatrix[i][j]
            maxrowindex=i
            maxcolindex=j

alignedseq1=''
alignedseq2=''

i=maxrowindex
j=maxcolindex

while routematrix[i][j]!='unknown':
    if routematrix[i][j]=='diagonal':
        alignedseq1+=seq1[i-1]
        alignedseq2+=seq2[j-1]
        i=i-1
        j=j-1
    if routematrix[i][j]=='top':
        alignedseq1+=seq1[i-1]
        alignedseq2+='_'
        i=i-1
    if routematrix[i][j]=='left':
        alignedseq1+='_'
        alignedseq2+=seq2[j-1]
        j=j-1

alignedseq1=alignedseq1[::-1]
alignedseq2=alignedseq2[::-1]

print()
print('Required alignment:')
print(alignedseq1)
print(alignedseq2)
