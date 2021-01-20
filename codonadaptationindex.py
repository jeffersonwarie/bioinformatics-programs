#This does not use a reference set

import sys
fin=open('ecolitest.txt','r')
line=''

info=[]
genecount=0
infoindex=0

nseq=''

piW=1
Lcodoncount=0
CAI=0
triplet=''
TTT=TTC=TTA=TTG=TCT=TCC=TCA=TCG=0
TAT=TAC=TGT=TGC=TGG=CTT=CTC=CTA=0
CTG=CCT=CCC=CCA=CCG=CAT=CAC=CAA=0
CAG=CGT=CGC=CGA=CGG=AGA=AGG=ATT=0
ATC=ATA=ATG=ACT=ACC=ACA=ACG=AAT=0
AAC=AAA=AAG=AGT=AGC=GTT=GTC=GTA=0
GTG=GCT=GCC=GCA=GCG=GAT=GAC=GAA=0
GAG=GGT=GGC=GGA=GGG=TAA=TAG=TGA=0
Phe=Leu=Ile=Met=Val=Ser=Pro=Thr=0
Ala=Tyr=Stop=His=Gln=Asn=Lys=Asp=0
Glu=Cys=Trp=Arg=Gly=0

#Phe
TTTrscu=TTCrscu=0

#Leu
TTArscu=TTGrscu=CTTrscu=CTCrscu=CTArscu=CTGrscu=0

#Ile
ATTrscu=ATCrscu=ATArscu=0

#Met
ATGrscu=0

#Val
GTTrscu=GTCrscu=GTArscu=GTGrscu=0

#Ser
TCTrscu=TCCrscu=TCArscu=TCGrscu=AGTrscu=AGCrscu=0

#Pro
CCTrscu=CCCrscu=CCArscu=CCGrscu=0

#Thr
ACTrscu=ACCrscu=ACArscu=ACGrscu=0

#Ala
GCTrscu=GCCrscu=GCArscu=GCGrscu=0

#Tyr
TATrscu=TACrscu=0

#Stop
TAArscu=TAGrscu=TGArscu=0

#His
CATrscu=CACrscu=0

#Gln
CAArscu=CAGrscu=0

#Asn
AATrscu=AACrscu=0

#Lys
AAArscu=AAGrscu=0

#Asp
GATrscu=GACrscu=0

#Glu
GAArscu=GAGrscu=0

#Cys
TGTrscu=TGCrscu=0

#Trp
TGGrscu=0

#Arg
CGTrscu=CGCrscu=CGArscu=CGGrscu=AGArscu=AGGrscu=0

#Gly
GGTrscu=GGCrscu=GGArscu=GGGrscu=0

#Phe
TTTW=TTCW=0

#Leu
TTAW=TTGW=CTTW=CTCW=CTAW=CTGW=0

#Ile
ATTW=ATCW=ATAW=0

#Met
ATGW=0

#Val
GTTW=GTCW=GTAW=GTGW=0

#Ser
TCTW=TCCW=TCAW=TCGW=AGTW=AGCW=0

#Pro
CCTW=CCCW=CCAW=CCGW=0

#Thr
ACTW=ACCW=ACAW=ACGW=0

#Ala
GCTW=GCCW=GCAW=GCGW=0

#Tyr
TATW=TACW=0

#Stop
TAAW=TAGW=TGAW=0

#His
CATW=CACW=0

#Gln
CAAW=CAGW=0

#Asn
AATW=AACW=0

#Lys
AAAW=AAGW=0

#Asp
GATW=GACW=0

#Glu
GAAW=GAGW=0

#Cys
TGTW=TGCW=0

#Trp
TGGW=0

#Arg
CGTW=CGCW=CGAW=CGGW=AGAW=AGGW=0

#Gly
GGTW=GGCW=GGAW=GGGW=0

line=fin.readline()
info.append({'geneinfo':line,'CAI':0})
genecount+=1

while len(line)>0:
    line=''
    line=fin.readline()
    if (len(line)>0 and line[0]=='>' and genecount!=0) or line=='':
        i=0
        while i<len(nseq):
            if len(triplet)<3:
                triplet+=nseq[i]
                i+=1
            else:
                if triplet in ['TTT','TTC']:
                    if triplet=='TTT':
                        TTT+=1
                    if triplet=='TTC':
                        TTC+=1
                    Phe+=1
                elif triplet in ['TCT','TCC','TCA','TCG','AGT','AGC']:
                    if triplet=='TCT':
                        TCT+=1
                    if triplet=='TCC':
                        TCC+=1
                    if triplet=='TCA':
                        TCA+=1
                    if triplet=='TCG':
                        TCG+=1
                    if triplet=='AGT':
                        AGT+=1
                    if triplet=='AGC':
                        AGC+=1
                    Ser+=1
                elif triplet in ['TAT','TAC']:
                    if triplet=='TAT':
                        TAT+=1
                    if triplet=='TAC':
                        TAC+=1
                    Tyr+=1
                elif triplet in ['TGT','TGC']:
                    if triplet=='TGT':
                        TGT+=1
                    if triplet=='TGC':
                        TGC+=1
                    Cys+=1
                elif triplet in ['TGG']:
                    if triplet=='TGG':
                        TGG+=1
                    Trp+=1
                elif triplet in ['CTT','CTC','CTA','CTG','TTA','TTG']:
                    if triplet=='CTT':
                        CTT+=1
                    if triplet=='CTC':
                        CTC+=1
                    if triplet=='CTA':
                        CTA+=1
                    if triplet=='CTG':
                        CTG+=1
                    if triplet=='TTA':
                        TTA+=1
                    if triplet=='TTG':
                        TTG+=1
                    Leu+=1
                elif triplet in ['CCT','CCC','CCA','CCG']:
                    if triplet=='CCT':
                        CCT+=1
                    if triplet=='CCC':
                        CCC+=1
                    if triplet=='CCA':
                        CCA+=1
                    if triplet=='CCG':
                        CCG+=1
                    Pro+=1
                elif triplet in ['CAT','CAC']:
                    if triplet=='CAT':
                        CAT+=1
                    if triplet=='CAC':
                        CAC+=1
                    His+=1
                elif triplet in ['CAA','CAG']:
                    if triplet=='CAA':
                        CAA+=1
                    if triplet=='CAG':
                        CAG+=1
                    Gln+=1
                elif triplet in ['CGT','CGC','CGA','CGG','AGA','AGG']:
                    if triplet=='CGT':
                        CGT+=1
                    if triplet=='CGC':
                        CGC+=1
                    if triplet=='CGA':
                        CGA+=1
                    if triplet=='CGG':
                        CGG+=1
                    if triplet=='AGA':
                        AGA+=1
                    if triplet=='AGG':
                        AGG+=1
                    Arg+=1
                elif triplet in ['ATT','ATC','ATA']:
                    if triplet=='ATT':
                        ATT+=1
                    if triplet=='ATC':
                        ATC+=1
                    if triplet=='ATA':
                        ATA+=1
                    Ile+=1
                elif triplet in ['ATG']:
                    if triplet=='ATG':
                        ATG+=1
                    Met+=1
                elif triplet in ['ACT','ACC','ACA','ACG']:
                    if triplet=='ACT':
                        ACT+=1
                    if triplet=='ACC':
                        ACC+=1
                    if triplet=='ACA':
                        ACA+=1
                    if triplet=='ACG':
                        ACG+=1
                    Thr+=1
                elif triplet in ['AAT','AAC']:
                    if triplet=='AAT':
                        AAT+=1
                    if triplet=='AAC':
                        AAC+=1
                    Asn+=1
                elif triplet in ['AAA','AAG']:
                    if triplet=='AAA':
                        AAA+=1
                    if triplet=='AAG':
                        AAG+=1
                    Lys+=1
                elif triplet in ['GTT','GTC','GTA','GTG']:
                    if triplet=='GTT':
                        GTT+=1
                    if triplet=='GTC':
                        GTC+=1
                    if triplet=='GTA':
                        GTA+=1
                    if triplet=='GTG':
                        GTG+=1
                    Val+=1
                elif triplet in ['GCT','GCC','GCA','GCG']:
                    if triplet=='GCT':
                        GCT+=1
                    if triplet=='GCC':
                        GCC+=1
                    if triplet=='GCA':
                        GCA+=1
                    if triplet=='GCG':
                        GCG+=1
                    Ala+=1
                elif triplet in ['GAT','GAC']:
                    if triplet=='GAT':
                        GAT+=1
                    if triplet=='GAC':
                        GAC+=1
                    Asp+=1
                elif triplet in ['GAA','GAG']:
                    if triplet=='GAA':
                        GAA+=1
                    if triplet=='GAG':
                        GAG+=1
                    Glu+=1
                elif triplet in ['GGT','GGC','GGA','GGG']:
                    if triplet=='GGT':
                        GGT+=1
                    if triplet=='GGC':
                        GGC+=1
                    if triplet=='GGA':
                        GGA+=1
                    if triplet=='GGG':
                        GGG+=1
                    Gly+=1
                elif triplet in ['TAA','TAG','TGA']:
                    if triplet=='TAA':
                        TAA+=1
                    if triplet=='TAG':
                        TAG+=1
                    if triplet=='TGA':
                        TGA+=1
                    Stop+=1
                else:
                    print('READ ERROR!')
                    sys.exit()
                triplet=''

        #Phe
        if ((TTT+TTC)/2)>0:
            TTTrscu=TTT/((TTT+TTC)/2)
            TTCrscu=TTC/((TTT+TTC)/2)
            TTTW=TTTrscu/max(TTTrscu,TTCrscu)
            TTCW=TTCrscu/max(TTTrscu,TTCrscu)

        #Leu
        if ((TTA+TTG+CTT+CTC+CTA+CTG)/6)>0:
            TTArscu=TTA/((TTA+TTG+CTT+CTC+CTA+CTG)/6)
            TTGrscu=TTG/((TTA+TTG+CTT+CTC+CTA+CTG)/6)
            CTTrscu=CTT/((TTA+TTG+CTT+CTC+CTA+CTG)/6)
            CTCrscu=CTC/((TTA+TTG+CTT+CTC+CTA+CTG)/6)
            CTArscu=CTA/((TTA+TTG+CTT+CTC+CTA+CTG)/6)
            CTGrscu=CTG/((TTA+TTG+CTT+CTC+CTA+CTG)/6)
            TTAW=TTArscu/max(TTArscu,TTGrscu,CTTrscu,CTCrscu,CTArscu,CTGrscu)
            TTGW=TTGrscu/max(TTArscu,TTGrscu,CTTrscu,CTCrscu,CTArscu,CTGrscu)
            CTTW=CTTrscu/max(TTArscu,TTGrscu,CTTrscu,CTCrscu,CTArscu,CTGrscu)
            CTCW=CTCrscu/max(TTArscu,TTGrscu,CTTrscu,CTCrscu,CTArscu,CTGrscu)
            CTAW=CTArscu/max(TTArscu,TTGrscu,CTTrscu,CTCrscu,CTArscu,CTGrscu)
            CTGW=CTGrscu/max(TTArscu,TTGrscu,CTTrscu,CTCrscu,CTArscu,CTGrscu)

        #Ile
        if ((ATT+ATC+ATA)/3)>0:
            ATTrscu=ATT/((ATT+ATC+ATA)/3)
            ATCrscu=ATC/((ATT+ATC+ATA)/3)
            ATArscu=ATA/((ATT+ATC+ATA)/3)
            ATTW=ATTrscu/max(ATTrscu,ATCrscu,ATArscu)
            ATCW=ATCrscu/max(ATTrscu,ATCrscu,ATArscu)
            ATAW=ATArscu/max(ATTrscu,ATCrscu,ATArscu)

        #Met
        ATGrscu=1
        ATGW=1

        #Val
        if ((GTT+GTC+GTA+GTG)/4)>0:
            GTTrscu=GTT/((GTT+GTC+GTA+GTG)/4)
            GTCrscu=GTC/((GTT+GTC+GTA+GTG)/4)
            GTArscu=GTA/((GTT+GTC+GTA+GTG)/4)
            GTGrscu=GTG/((GTT+GTC+GTA+GTG)/4)
            GTTW=GTTrscu/max(GTTrscu,GTCrscu,GTArscu,GTGrscu)
            GTCW=GTCrscu/max(GTTrscu,GTCrscu,GTArscu,GTGrscu)
            GTAW=GTArscu/max(GTTrscu,GTCrscu,GTArscu,GTGrscu)
            GTGW=GTGrscu/max(GTTrscu,GTCrscu,GTArscu,GTGrscu)

        #Ser
        if ((TCT+TCC+TCA+TCG+AGT+AGC)/6)>0:
            TCTrscu=TCT/((TCT+TCC+TCA+TCG+AGT+AGC)/6)
            TCCrscu=TCC/((TCT+TCC+TCA+TCG+AGT+AGC)/6)
            TCArscu=TCA/((TCT+TCC+TCA+TCG+AGT+AGC)/6)
            TCGrscu=TCG/((TCT+TCC+TCA+TCG+AGT+AGC)/6)
            AGTrscu=AGT/((TCT+TCC+TCA+TCG+AGT+AGC)/6)
            AGCrscu=AGC/((TCT+TCC+TCA+TCG+AGT+AGC)/6)
            TCTW=TCTrscu/max(TCTrscu,TCCrscu,TCArscu,TCGrscu,AGTrscu,AGCrscu)
            TCCW=TCCrscu/max(TCTrscu,TCCrscu,TCArscu,TCGrscu,AGTrscu,AGCrscu)
            TCAW=TCArscu/max(TCTrscu,TCCrscu,TCArscu,TCGrscu,AGTrscu,AGCrscu)
            TCGW=TCGrscu/max(TCTrscu,TCCrscu,TCArscu,TCGrscu,AGTrscu,AGCrscu)
            AGTW=AGTrscu/max(TCTrscu,TCCrscu,TCArscu,TCGrscu,AGTrscu,AGCrscu)
            AGCW=AGCrscu/max(TCTrscu,TCCrscu,TCArscu,TCGrscu,AGTrscu,AGCrscu)

        #Pro
        if ((CCT+CCC+CCA+CCG)/4)>0:
            CCTrscu=CCT/((CCT+CCC+CCA+CCG)/4)
            CCCrscu=CCC/((CCT+CCC+CCA+CCG)/4)
            CCArscu=CCA/((CCT+CCC+CCA+CCG)/4)
            CCGrscu=CCG/((CCT+CCC+CCA+CCG)/4)
            CCTW=CCTrscu/max(CCTrscu,CCCrscu,CCArscu,CCGrscu)
            CCCW=CCCrscu/max(CCTrscu,CCCrscu,CCArscu,CCGrscu)
            CCAW=CCArscu/max(CCTrscu,CCCrscu,CCArscu,CCGrscu)
            CCGW=CCGrscu/max(CCTrscu,CCCrscu,CCArscu,CCGrscu)

        #Thr
        if ((ACT+ACC+ACA+ACG)/4)>0:
            ACTrscu=ACT/((ACT+ACC+ACA+ACG)/4)
            ACCrscu=ACC/((ACT+ACC+ACA+ACG)/4)
            ACArscu=ACA/((ACT+ACC+ACA+ACG)/4)
            ACGrscu=ACG/((ACT+ACC+ACA+ACG)/4)
            ACTW=ACTrscu/max(ACTrscu,ACCrscu,ACArscu,ACGrscu)
            ACCW=ACCrscu/max(ACTrscu,ACCrscu,ACArscu,ACGrscu)
            ACAW=ACArscu/max(ACTrscu,ACCrscu,ACArscu,ACGrscu)
            ACGW=ACGrscu/max(ACTrscu,ACCrscu,ACArscu,ACGrscu)

        #Ala
        if ((GCT+GCC+GCA+GCG)/4):
            GCTrscu=GCT/((GCT+GCC+GCA+GCG)/4)
            GCCrscu=GCC/((GCT+GCC+GCA+GCG)/4)
            GCArscu=GCA/((GCT+GCC+GCA+GCG)/4)
            GCGrscu=GCG/((GCT+GCC+GCA+GCG)/4)
            GCTW=GCTrscu/max(GCTrscu,GCCrscu,GCArscu,GCGrscu)
            GCCW=GCCrscu/max(GCTrscu,GCCrscu,GCArscu,GCGrscu)
            GCAW=GCArscu/max(GCTrscu,GCCrscu,GCArscu,GCGrscu)
            GCGW=GCGrscu/max(GCTrscu,GCCrscu,GCArscu,GCGrscu)

        #Tyr
        if ((TAT+TAC)/2)>0:
            TATrscu=TAT/((TAT+TAC)/2)
            TACrscu=TAC/((TAT+TAC)/2)
            TATW=TATrscu/max(TATrscu,TACrscu)
            TACW=TACrscu/max(TATrscu,TACrscu)

        #Stop
        TAArscu=1
        TAGrscu=1
        TGArscu=1
        TAAW=1
        TAGW=1
        TGAW=1

        #His
        if ((CAT+CAC)/2)>0:
            CATrscu=CAT/((CAT+CAC)/2)
            CACrscu=CAC/((CAT+CAC)/2)
            CATW=CATrscu/max(CATrscu,CACrscu)
            CACW=CACrscu/max(CATrscu,CACrscu)

        #Gln
        if ((CAA+CAG)/2)>0:
            CAArscu=CAA/((CAA+CAG)/2)
            CAGrscu=CAG/((CAA+CAG)/2)
            CAAW=CAArscu/max(CAArscu,CAGrscu)
            CAGW=CAGrscu/max(CAArscu,CAGrscu)

        #Asn
        if ((AAT+AAC)/2)>0:
            AATrscu=AAT/((AAT+AAC)/2)
            AACrscu=AAC/((AAT+AAC)/2)
            AATW=AATrscu/max(AATrscu,AACrscu)
            AACW=AACrscu/max(AATrscu,AACrscu)

        #Lys
        if ((AAA+AAG)/2)>0:
            AAArscu=AAA/((AAA+AAG)/2)
            AAGrscu=AAG/((AAA+AAG)/2)
            AAAW=AAArscu/max(AAArscu,AAGrscu)
            AAGW=AAGrscu/max(AAArscu,AAGrscu)

        #Asp
        if ((GAT+GAC)/2)>0:
            GATrscu=GAT/((GAT+GAC)/2)
            GACrscu=GAC/((GAT+GAC)/2)
            GATW=GATrscu/max(GATrscu,GACrscu)
            GACW=GACrscu/max(GATrscu,GACrscu)

        #Glu
        if ((GAA+GAG)/2)>0:
            GAArscu=GAA/((GAA+GAG)/2)
            GAGrscu=GAG/((GAA+GAG)/2)
            GAAW=GAArscu/max(GAArscu,GAGrscu)
            GAGW=GAGrscu/max(GAArscu,GAGrscu)

        #Cys
        if ((TGT+TGC)/2)>0:
            TGTrscu=TGT/((TGT+TGC)/2)
            TGCrscu=TGC/((TGT+TGC)/2)
            TGTW=TGTrscu/max(TGTrscu,TGCrscu)
            TGCW=TGCrscu/max(TGTrscu,TGCrscu)

        #Trp
        TGGrscu=1
        TGGW=1

        #Arg
        if ((CGT+CGC+CGA+CGG+AGA+AGG)/6)>0:
            CGTrscu=CGT/((CGT+CGC+CGA+CGG+AGA+AGG)/6)
            CGCrscu=CGC/((CGT+CGC+CGA+CGG+AGA+AGG)/6)
            CGArscu=CGA/((CGT+CGC+CGA+CGG+AGA+AGG)/6)
            CGGrscu=CGG/((CGT+CGC+CGA+CGG+AGA+AGG)/6)
            AGArscu=AGA/((CGT+CGC+CGA+CGG+AGA+AGG)/6)
            AGGrscu=AGG/((CGT+CGC+CGA+CGG+AGA+AGG)/6)
            CGTW=CGTrscu/max(CGTrscu,CGCrscu,CGArscu,CGGrscu,AGArscu,AGGrscu)
            CGCW=CGCrscu/max(CGTrscu,CGCrscu,CGArscu,CGGrscu,AGArscu,AGGrscu)
            CGAW=CGArscu/max(CGTrscu,CGCrscu,CGArscu,CGGrscu,AGArscu,AGGrscu)
            CGGW=CGGrscu/max(CGTrscu,CGCrscu,CGArscu,CGGrscu,AGArscu,AGGrscu)
            AGAW=AGArscu/max(CGTrscu,CGCrscu,CGArscu,CGGrscu,AGArscu,AGGrscu)
            AGGW=AGGrscu/max(CGTrscu,CGCrscu,CGArscu,CGGrscu,AGArscu,AGGrscu)

        #Gly
        if ((GGT+GGC+GGA+GGG)/4)>0:
            GGTrscu=GGT/((GGT+GGC+GGA+GGG)/4)
            GGCrscu=GGC/((GGT+GGC+GGA+GGG)/4)
            GGArscu=GGA/((GGT+GGC+GGA+GGG)/4)
            GGGrscu=GGG/((GGT+GGC+GGA+GGG)/4)
            GGTW=GGTrscu/max(GGTrscu,GGCrscu,GGArscu,GGGrscu)
            GGCW=GGCrscu/max(GGTrscu,GGCrscu,GGArscu,GGGrscu)
            GGAW=GGArscu/max(GGTrscu,GGCrscu,GGArscu,GGGrscu)
            GGGW=GGGrscu/max(GGTrscu,GGCrscu,GGArscu,GGGrscu)

        i=0
        piW=1
        Lcodoncount=0
        CAI=0
        triplet=''
        while i<len(nseq):
            if len(triplet)<3:
                triplet+=nseq[i]
                i+=1
            else:
                if triplet=='TTT':
                    piW=piW*TTTW
                    Lcodoncount+=1
                elif triplet=='TTC':
                    piW=piW*TTCW
                    Lcodoncount+=1
                elif triplet=='TTA':
                    piW=piW*TTAW
                    Lcodoncount+=1
                elif triplet=='TTG':
                    piW=piW*TTGW
                    Lcodoncount+=1
                elif triplet=='CTT':
                    piW=piW*CTTW
                    Lcodoncount+=1
                elif triplet=='CTC':
                    piW=piW*CTCW
                    Lcodoncount+=1
                elif triplet=='CTA':
                    piW=piW*CTAW
                    Lcodoncount+=1
                elif triplet=='CTG':
                    piW=piW*CTGW
                    Lcodoncount+=1
                elif triplet=='ATT':
                    piW=piW*ATTW
                    Lcodoncount+=1
                elif triplet=='ATC':
                    piW=piW*ATCW
                    Lcodoncount+=1
                elif triplet=='ATA':
                    piW=piW*ATAW
                    Lcodoncount+=1
                elif triplet=='ATG':
                    piW=piW*ATGW
                elif triplet=='GTT':
                    piW=piW*GTTW
                    Lcodoncount+=1
                elif triplet=='GTC':
                    piW=piW*GTCW
                    Lcodoncount+=1
                elif triplet=='GTA':
                    piW=piW*GTAW
                    Lcodoncount+=1
                elif triplet=='GTG':
                    piW=piW*GTGW
                    Lcodoncount+=1
                elif triplet=='TCT':
                    piW=piW*TCTW
                    Lcodoncount+=1
                elif triplet=='TCC':
                    piW=piW*TCCW
                    Lcodoncount+=1
                elif triplet=='TCA':
                    piW=piW*TCAW
                    Lcodoncount+=1
                elif triplet=='TCG':
                    piW=piW*TCGW
                    Lcodoncount+=1
                elif triplet=='CCT':
                    piW=piW*CCTW
                    Lcodoncount+=1
                elif triplet=='CCC':
                    piW=piW*CCCW
                    Lcodoncount+=1
                elif triplet=='CCA':
                    piW=piW*CCAW
                    Lcodoncount+=1
                elif triplet=='CCG':
                    piW=piW*CCGW
                    Lcodoncount+=1
                elif triplet=='ACT':
                    piW=piW*ACTW
                    Lcodoncount+=1
                elif triplet=='ACC':
                    piW=piW*ACCW
                    Lcodoncount+=1
                elif triplet=='ACA':
                    piW=piW*ACAW
                    Lcodoncount+=1
                elif triplet=='ACG':
                    piW=piW*ACGW
                    Lcodoncount+=1
                elif triplet=='GCT':
                    piW=piW*GCTW
                    Lcodoncount+=1
                elif triplet=='GCC':
                    piW=piW*GCCW
                    Lcodoncount+=1
                elif triplet=='GCA':
                    piW=piW*GCAW
                    Lcodoncount+=1
                elif triplet=='GCG':
                    piW=piW*GCGW
                    Lcodoncount+=1
                elif triplet=='TAT':
                    piW=piW*TATW
                    Lcodoncount+=1
                elif triplet=='TAC':
                    piW=piW*TACW
                    Lcodoncount+=1
                elif triplet=='TAA':
                    piW=piW*TAAW
                elif triplet=='TAG':
                    piW=piW*TAGW
                elif triplet=='CAT':
                    piW=piW*CATW
                    Lcodoncount+=1
                elif triplet=='CAC':
                    piW=piW*CACW
                    Lcodoncount+=1
                elif triplet=='CAA':
                    piW=piW*CAAW
                    Lcodoncount+=1
                elif triplet=='CAG':
                    piW=piW*CAGW
                    Lcodoncount+=1
                elif triplet=='AAT':
                    piW=piW*AATW
                    Lcodoncount+=1
                elif triplet=='AAC':
                    piW=piW*AACW
                    Lcodoncount+=1
                elif triplet=='AAA':
                    piW=piW*AAAW
                    Lcodoncount+=1
                elif triplet=='AAG':
                    piW=piW*AAGW
                    Lcodoncount+=1
                elif triplet=='GAT':
                    piW=piW*GATW
                    Lcodoncount+=1
                elif triplet=='GAC':
                    piW=piW*GACW
                    Lcodoncount+=1
                elif triplet=='GAA':
                    piW=piW*GAAW
                    Lcodoncount+=1
                elif triplet=='GAG':
                    piW=piW*GAGW
                    Lcodoncount+=1
                elif triplet=='TGT':
                    piW=piW*TGTW
                    Lcodoncount+=1
                elif triplet=='TGC':
                    piW=piW*TGCW
                    Lcodoncount+=1
                elif triplet=='TGA':
                    piW=piW*TGAW
                elif triplet=='TGG':
                    piW=piW*TGGW
                elif triplet=='CGT':
                    piW=piW*CGTW
                    Lcodoncount+=1
                elif triplet=='CGC':
                    piW=piW*CGCW
                    Lcodoncount+=1
                elif triplet=='CGA':
                    piW=piW*CGAW
                    Lcodoncount+=1
                elif triplet=='CGG':
                    piW=piW*CGGW
                    Lcodoncount+=1
                elif triplet=='AGT':
                    piW=piW*AGTW
                    Lcodoncount+=1
                elif triplet=='AGC':
                    piW=piW*AGCW
                    Lcodoncount+=1
                elif triplet=='AGA':
                    piW=piW*AGAW
                    Lcodoncount+=1
                elif triplet=='AGG':
                    piW=piW*AGGW
                    Lcodoncount+=1
                elif triplet=='GGT':
                    piW=piW*GGTW
                    Lcodoncount+=1
                elif triplet=='GGC':
                    piW=piW*GGCW
                    Lcodoncount+=1
                elif triplet=='GGA':
                    piW=piW*GGAW
                    Lcodoncount+=1
                elif triplet=='GGG':
                    piW=piW*GGGW
                    Lcodoncount+=1
                else:
                    print(triplet)
                    print('CALCULATION ERROR!')
                    sys.exit()
                triplet=''

        #print(piW)
        #print(CAI)
        CAI=pow(piW,1/Lcodoncount)
        info[infoindex]['CAI']=CAI

        triplet=''
        TTT=TTC=TTA=TTG=TCT=TCC=TCA=TCG=0
        TAT=TAC=TGT=TGC=TGG=CTT=CTC=CTA=0
        CTG=CCT=CCC=CCA=CCG=CAT=CAC=CAA=0
        CAG=CGT=CGC=CGA=CGG=AGA=AGG=ATT=0
        ATC=ATA=ATG=ACT=ACC=ACA=ACG=AAT=0
        AAC=AAA=AAG=AGT=AGC=GTT=GTC=GTA=0
        GTG=GCT=GCC=GCA=GCG=GAT=GAC=GAA=0
        GAG=GGT=GGC=GGA=GGG=TAA=TAG=TGA=0
        Phe=Leu=Ile=Met=Val=Ser=Pro=Thr=0
        Ala=Tyr=Stop=His=Gln=Asn=Lys=Asp=0
        Glu=Cys=Trp=Arg=Gly=0

        #Phe
        TTTrscu=TTCrscu=0

        #Leu
        TTArscu=TTGrscu=CTTrscu=CTCrscu=CTArscu=CTGrscu=0

        #Ile
        ATTrscu=ATCrscu=ATArscu=0

        #Met
        ATGrscu=0

        #Val
        GTTrscu=GTCrscu=GTArscu=GTGrscu=0

        #Ser
        TCTrscu=TCCrscu=TCArscu=TCGrscu=AGTrscu=AGCrscu=0

        #Pro
        CCTrscu=CCCrscu=CCArscu=CCGrscu=0

        #Thr
        ACTrscu=ACCrscu=ACArscu=ACGrscu=0

        #Ala
        GCTrscu=GCCrscu=GCArscu=GCGrscu=0

        #Tyr
        TATrscu=TACrscu=0

        #Stop
        TAArscu=TAGrscu=TGArscu=0

        #His
        CATrscu=CACrscu=0

        #Gln
        CAArscu=CAGrscu=0

        #Asn
        AATrscu=AACrscu=0

        #Lys
        AAArscu=AAGrscu=0

        #Asp
        GATrscu=GACrscu=0

        #Glu
        GAArscu=GAGrscu=0

        #Cys
        TGTrscu=TGCrscu=0

        #Trp
        TGGrscu=0

        #Arg
        CGTrscu=CGCrscu=CGArscu=CGGrscu=AGArscu=AGGrscu=0

        #Gly
        GGTrscu=GGCrscu=GGArscu=GGGrscu=0

        #Phe
        TTTW=TTCW=0

        #Leu
        TTAW=TTGW=CTTW=CTCW=CTAW=CTGW=0

        #Ile
        ATTW=ATCW=ATAW=0

        #Met
        ATGW=0

        #Val
        GTTW=GTCW=GTAW=GTGW=0

        #Ser
        TCTW=TCCW=TCAW=TCGW=AGTW=AGCW=0

        #Pro
        CCTW=CCCW=CCAW=CCGW=0

        #Thr
        ACTW=ACCW=ACAW=ACGW=0

        #Ala
        GCTW=GCCW=GCAW=GCGW=0

        #Tyr
        TATW=TACW=0

        #Stop
        TAAW=TAGW=TGAW=0

        #His
        CATW=CACW=0

        #Gln
        CAAW=CAGW=0

        #Asn
        AATW=AACW=0

        #Lys
        AAAW=AAGW=0

        #Asp
        GATW=GACW=0

        #Glu
        GAAW=GAGW=0

        #Cys
        TGTW=TGCW=0

        #Trp
        TGGW=0

        #Arg
        CGTW=CGCW=CGAW=CGGW=AGAW=AGGW=0

        #Gly
        GGTW=GGCW=GGAW=GGGW=0
        
        info.append({'geneinfo':line,'CAI':0})
        genecount+=1
        infoindex+=1
        continue
    else:
        line=line.rstrip()
        nseq+=line

for i in range(len(info)-1):
    print('Geneinfo: ',info[i]['geneinfo'],' CAI: ',info[i]['CAI'])
