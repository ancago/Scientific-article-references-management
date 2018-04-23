# -*- coding: utf-8 -*-
"""

Created on Sun Feb 25 22:41:04 2018
@author: Anna
"""

#NEW=[]
#OLD=[]
#D={}
#
#for i in range(1,291):
#    NEW.append(i)
##print(len(NEW))
#
#for i in range(5,14):
#    OLD.append(i)
#for i in range(30,311):
#    OLD.append(i)
##print(len(OLD))
#    
#for i in OLD:
#    D[i]=NEW[OLD.index(i)]
##print(D)

string="""
	especially 2-AG, are rising [187,188]. T..iption of CB1R gene - CNR1 [13,181]. In Alzheimer’s disease, the levels of CB1R protein ... unaffected [182,183,184]. .... excitotoxicity [185,186].
	No alterations ........ disorder patients [216]. However, ....atients [217,218]. Moreover, ...s pallidus [219]. Different cannabinoids may exert opposite effects ... for developing this disorder [220,221,222]. Patients with schizophrenia ... reach in CB1R [223].
	C.........o reduce anxiety [224]. Additionally, it ameliorates hyperlocomotion, as well as .... deficits [225]. Schizophrenia is .... [226,227]. The action of....acts as FAAH inhibitor [228,229,230,231].
	.....in rodents [193,194,195,196,197]. Chronic CB1R inhibition .... [198,199]. Depressed ... concentration [200,201,202]. 
	....of neurons in the hippocampus [194,203,204]. Interestingly, .... both groups [205].
	The ..... for AEA catabolism [206]. Deficiency of FAAH ...... [207]. An analogous effect ..activating CB1R [190,233,234,235,236]. .... Although, there are..... [208,209,210]. Interestingly, .... subtype [211,212,213]. Some .... serotonin in nucleus accumbens [214]. These data indicate ..
	Although, CB1R inhibitors .... this effect [215]. 
       
"""
TXT=[]
INDEX=[]
INTS=['0','1','2','3','4','5','6','7','8','9']
L=[]
x=0
TEMP=[]
LIST_STRING=list(string)

for i in range(len(LIST_STRING)):
    if i in INDEX:
        i+=1
    else:
        INDEX.append(i)
        char = LIST_STRING[i]
        if char=='[':
            while char!=']':
                TXT.append(char)
                i+=1
                INDEX.append(i)
                char=LIST_STRING[i]     
            if char==']':
                
                TXT.append(char)
#                print(len(TXT),'txt')
                for j in range(len(''.join(TXT))):
                    num=''.join(TXT)[j]
                    if num in INTS:
                        TEMP.append(int(num))
#                        print(TEMP)
                        x+=1
                    else:
                        if x==3:
                            TEMP=int(TEMP[0])*100+int(TEMP[1])*10+int(TEMP[2])
                            if TEMP not in L:
                                L.append(TEMP)
#                            print(L)
                        elif x==2:
                            TEMP=int(TEMP[0])*10+int(TEMP[1])
                            if TEMP not in L:
                                L.append(TEMP)
#                            print(L)
                        elif x==1:
                            TEMP=int(TEMP[0])
                            if TEMP not in L:
                                L.append(TEMP)
                        else:
                            pass
                        x=0
                        TEMP=[]
                        
                TXT=[]

DD={}
w=1
for h in L:
    DD[h]=w
    w+=1

            
#print(L)
print(DD)
                
                