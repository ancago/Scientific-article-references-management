# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 09:20:21 2018

CONDITIONS!!!!
1. at the beginning of string must be \n
2. at the end of string CAN'T be \n
3. at the end, there must be: "                                                "
takes in a list of numerated references
changes numbers of references according to a given dictionary= {OLD number: NEW number}
adds '.' at the end of line if it's not there BUT!!! not to the last position in references


@author: Anna
"""
string= """
13. Van Laere K, Casteels C, Dhollander I, Goffin K, Grachev I, et al. Widespread decrease of type 1 cannabinoid receptor availability in Huntington disease in vivo. J Nucl Med. 2010; 51:1413–7.
181. Blázquez C, Chiarlone A, Sagredo O, et al. Loss of striatal type 1 cannabinoid receptors is a key pathogenic factor in Huntington's disease. Brain. 2011; 134(Pt 1): 119-36.
182. Kalifa S, Polston EK, Allard JS, et al. Distribution patterns of cannabinoid CB1 receptors in the hippocampus of APPswe/PS1ΔE9 double transgenic mice. Brain Res. 2011; 1376: 94-100.
183. Westlake TM, Howlett AC, Bonner TI, et al. Cannabinoid receptor binding and messenger RNA expression in human brain: an in vitro receptor autoradiography and in situ hybridization histochemistry study of normal aged and Alzheimer's brains. Neuroscience. 1994; 63(3): 637-52.
184. Lee JH, Agacinski G, Williams JH, et al. Intact cannabinoid CB1 receptors in the Alzheimer's disease cortex. Neurochem Int. 2010; 57(8): 985-9.
185. Ludányi A, Eross L, Czirják S, et al. Downregulation of the CB1 cannabinoid receptor and related molecular elements of the endocannabinoid system in epileptic human hippocampus. J Neurosci. 2008; 28(12): 2976-90.
186. Guggenhuber S, Monory K, Lutz B, et al. AAV vector-mediated overexpression of CB1 cannabinoid receptor in pyramidal neurons of the hippocampus protects against seizure-induced excitoxicity. PLoS One. 2010; 5(12): e15707.
187. Panikashvili D, Simeonidou C, Ben-Shabat S, et al. An endogenous cannabinoid (2-AG) is neuroprotective after brain injury. Nature. 2001; 413(6855): 527-31.
188. Wettschureck N, van der Stelt M, Tsubokawa H, et al. Forebrain-specific inactivation of Gq/G11 family G proteins results in age-dependent epilepsy and impaired endocannabinoid formation. Mol Cell Biol. 2006; 26(15):5888-94.
189. Maccarrone M, Rossi S, Bari M, et al. Anandamide inhibits metabolism and physiological actions of 2-arachidonoylglycerol in the striatum. Nat Neurosci. 2008; 11(2): 152-9.
190. Rossi S, De Chiara V, Musella A, et al. Preservation of striatal cannabinoid CB1 receptor function correlates with the antianxiety effects of fatty acid amide hydrolase inhibition. Mol Pharmacol. 2010; 78(2): 260-8.
191. Tarakanov AO, Fuxe KG. Triplet puzzle: homologies of receptor heteromers. J Mol Neurosci. 2010; 41(2): 294-303.
192. Rios C, Gomes I, Devi LA. mu opioid and CB1 cannabinoid receptor interactions: reciprocal inhibition of receptor signaling and neuritogenesis. Br J Pharmacol. 2006; 148(4): 387-95.
193. Gorzalka BB, Hill MN. Putative role of endocannabinoid signaling in the etiology of depression and actions of antidepressants. Prog Neuropsychopharmacol Biol Psychiatry. 2011; 35(7): 1575-85.
194. Beyer CE, Dwyer JM, Piesla MJ, et al. Depression-like phenotype following chronic CB1 receptor antagonism. Neurobiol Dis. 2010; 39(2): 148-55.
195. Santucci V, Storme JJ, Soubrié P, et al. Arousal-enhancing properties of the CB1 cannabinoid receptor antagonist SR 141716A in rats as assessed by electroencephalographic spectral and sleep-waking cycle analysis. Life Sci. 1996; 58(6): PL103-10.
196. Haller J, Bakos N, Szirmay M, et al. The effects of genetic and pharmacological blockade of the CB1 cannabinoid receptor on anxiety. Eur J Neurosci. 2002;16:1395–8.
197. Patel S, Hillard CJ. Pharmacological evaluation of cannabinoid receptor ligands in a mouse model of anxiety: further evidence for an anxiolytic role for endogenous cannabinoid signaling. J Pharmacol Exp Ther. 2006; 318: 304–11.
198. Zavatti M, Carnevale G, Benelli A, et al. Effects of the cannabinoid antagonist SR 141716 on sexual and motor behaviour in receptive female rats. Clin Exp Pharmacol Physiol. 2011; 38(11): 771-5.
199. Verty AN, McGregor IS, Mallet PE. Consumption of high carbohydrate, high fat, and normal chow is equally suppressed by a cannabinoid receptor antagonist in non-deprived rats. Neurosci Lett. 2004; 354(3): 217-20.
200. Hill MN, Gorzalka BB. Increased sensitivity to restraint stress and novelty-induced emotionality following long-term, high dose cannabinoid exposure. Psychoneuroendocrinology. 2006; 31(4): 526-36.
201. Cota D, Steiner MA, Marsicano G, et al. Requirement of cannabinoid receptor type 1 for the basal modulation of hypothalamic-pituitary-adrenal axis function. Endocrinology. 2007; 148(4): 1574-81.
202. Hill MN, McLaughlin RJ, Pan B, et al. Recruitment of prefrontal cortical endocannabinoid signaling by glucocorticoids contributes to termination of the stress response. J Neurosci. 2011; 31(29): 10506-15.
203. Lee S, Kim DH, Yoon SH, et al. Sub-chronic administration of rimonabant causes loss of antidepressive activity and decreases doublecortin immunoreactivity in the mouse hippocampus. Neurosci Lett. 2009; 467: 111–116.
204. Landfield PW, Cadwallader LB, Vinsant S. Quantitative changes in hippocampal structure following long-term exposure to delta-9-tetrahydrocannabinol: possible mediation by glucocorticoid systems. Brain Res. 1988;443:47–62.
205. Reich CG, Taylor ME, McCarthy MM. Differential effects of chronic unpredictable stress on hippocampal CB1 receptors in male and female rats. Behav Brain Res. 2009; 203(2): 264-9.
206. McLaughlin RJ, Hill MN, Bambico FR, et al. Prefrontal cortical anandamide signaling coordinates coping responses to stress through a serotonergic pathway. Eur Neuropsychopharmacol. 2012; 22(9): 664-71.
207. Cassano T, Gaetani S, Macheda T, et al. Evaluation of the emotional phenotype and serotonergic neurotransmission of fatty acid amide hydrolase-deficient mice. Psychopharmacology (Berl). 2011; 214(2): 465-76.
208. Bambico FR, Hattan PR, Garant JP, et al. Effect of delta-9-tetrahydrocannabinol on behavioral despair and on pre- and postsynaptic serotonergic transmission. Prog Neuropsychopharmacol Biol Psychiatry. 2012; 38(1): 88-96.
209. Kearn CS, Greenberg MJ, DiCamelli R, et al. Relationships between ligand affinities for the cerebellar cannabinoid receptor CB1 and the induction of GDP/GTP exchange. J Neurochem. 1999; 72(6): 2379-87.
210. Resstel LB, Tavares RF, Lisboa SF, et al. 5-HT1A receptors are involved in the cannabidiol-induced attenuation of behavioural and cardiovascular responses to acute restraint stress in rats. Br J Pharmacol. 2009; 156(1): 181-8.
211. Matsuda LA, Lolait SJ, Brownstein MJ, et al. Structure of a cannabinoid receptor and functional expression of the cloned cDNA. Nature. 1990; 346(6284): 561-4.
212. Rock EM, Bolognini D, Limebeer CL, et al. Cannabidiol, a non-psychotropic component of cannabis, attenuates vomiting and nausea-like behaviour via indirect agonism of 5-HT(1A) somatodendritic autoreceptors in the dorsal raphe nucleus. Br J Pharmacol. 2012; 165(8): 2620-34.
213. Zanelati TV, Biojone C, Moreira FA, et al. Antidepressant-like effects of cannabidiol in mice: possible involvement of 5-HT1A receptors. Br J Pharmacol. 2010; 159(1): 122-8.
214. Tao R, Ma Z. Neural Circuit in the Dorsal Raphe Nucleus Responsible for Cannabinoid-Mediated Increases in 5-HT Efflux in the Nucleus Accumbens of the Rat Brain. ISRN Pharmacol. 2012; 2012(): 276902.
215. Elbatsh MM, Moklas MA, Marsden CA, et al. Antidepressant-like effects of Δ⁹-tetrahydrocannabinol and rimonabant in the olfactory bulbectomised rat model of depression. Pharmacol Biochem Behav. 2012; 102(2): 357-65.
216. Koethe D, Llenos IC, Dulay JR, et al. Expression of CB1 cannabinoid receptor in the anterior cingulate cortex in schizophrenia, bipolar disorder, and major depression. J Neural Transm (Vienna). 2007; 114(8): 1055-63.
217. Giuffrida A, Leweke FM, Gerth CW, et al. Cerebrospinal anandamide levels are elevated in acute schizophrenia and are inversely correlated with psychotic symptoms. Neuropsychopharmacology. 2004; 29(11): 2108-14.
218. Leweke FM. Anandamide dysfunction in prodromal and established psychosis. Curr Pharm Des. 2012; 18(32): 5188-93.
219. Wong DF, Kuwabara H, Horti AG, et al. Quantification of cerebral cannabinoid receptors subtype 1 (CB1) in healthy subjects and schizophrenia by the novel PET radioligand [11C]OMAR. Neuroimage. 2010; 52(4): 1505-13.
220. Large M, Sharma S, Compton MT, et al. Cannabis use and earlier onset of psychosis: a systematic meta-analysis. Arch Gen Psychiatry. 2011; 68(6): 555-61.
221. D'Souza DC, Perry E, MacDougall L, et al. The psychotomimetic effects of intravenous delta-9-tetrahydrocannabinol in healthy individuals: implications for psychosis. Neuropsychopharmacology. 2004; 29(8): 1558-72.
222. D'Souza DC, Abi-Saab WM, Madonick S, et al. Delta-9-tetrahydrocannabinol effects in schizophrenia: implications for cognition, psychosis, and addiction. Biol Psychiatry. 2005; 57(6): 594-608.
223. Rais M, van Haren NE, Cahn W, et al. Cannabis use and progressive cortical thickness loss in areas rich in CB1 receptors during the first five years of schizophrenia. Eur Neuropsychopharmacol. 2010; 20(12): 855-65.
224. Fusar-Poli P, Crippa JA, Bhattacharyya S, et al. Distinct effects of {delta}9-tetrahydrocannabinol and cannabidiol on neural activation during emotional processing. Arch Gen Psychiatry. 2009; 66(1): 95-105.
225. Zuardi AW, Crippa JA, Hallak JE, et al. A critical review of the antipsychotic effects of cannabidiol: 30 years of a translational investigation. Curr Pharm Des. 2012; 18(32): 5131-40.
226. Kuepper R, Ceccarini J, Lataster J, et al. Delta-9-tetrahydrocannabinol-induced dopamine release as a function of psychosis risk: 18F-fallypride positron emission tomography study. PLoS One. 2013; 8(7): e70378.
227. Bossong MG, van Berckel BN, Boellaard R, et al. Delta 9-tetrahydrocannabinol induces dopamine release in the human striatum. Neuropsychopharmacology. 2009; 34(3): 759-66.
228. Pertwee RG. The diverse CB1 and CB2 receptor pharmacology of three plant cannabinoids: delta9-tetrahydrocannabinol, cannabidiol and delta9-tetrahydrocannabivarin. Br J Pharmacol. 2008; 153(2): 199-215.
229. Russo EB, Burnett A, Hall B, et al. Agonistic properties of cannabidiol at 5-HT1a receptors. Neurochem Res. 2005; 30(8): 1037-43.
230. Kathmann M, Flau K, Redmer A, et al. Cannabidiol is an allosteric modulator at mu- and delta-opioid receptors. Naunyn Schmiedebergs Arch Pharmacol. 2006; 372(5): 354-61.
231. Bisogno T, Hanus L, De Petrocellis L, et al. Molecular targets for cannabidiol and its synthetic analogues: effect on vanilloid VR1 receptors and on the cellular uptake and enzymatic hydrolysis of anandamide. Br J Pharmacol. 2001; 134(4): 845-52.
                                                                                                  """

#D={}
#NEW=[]
#OLD=[]
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

x=0
REFERENCES=[]
Ref_string=''
TEMP=''
INTS=['0','1','2','3','4','5','6','7','8','9']
LIST_STRING=list(string)

for i in range(len(LIST_STRING)):
    LENG=len(LIST_STRING)
    if LIST_STRING[i]=="\n":
        if LIST_STRING[i-1]!='.':
            if LIST_STRING[i-1]==' ':
                if LIST_STRING[i-2]!='.':
                    LIST_STRING.insert(i-1,'.')
                    del(LIST_STRING[-1])
            elif LIST_STRING[i-1] in INTS:
                LIST_STRING.insert(i,'.')
                del(LIST_STRING[-1])
            else:
                print('SOME UNEXPECTED END OF LINE')
    else:
        pass
    if LIST_STRING[i]=="\n":
        while LIST_STRING[i]!=".":
            if LIST_STRING[i] in INTS:
                TEMP+=LIST_STRING[i]
#                print(TEMP)
                del(LIST_STRING[i])
                LIST_STRING.append(' ')
                x+=1
#                print(len(LIST_STRING)) 
            else:
                i+=1
        if LIST_STRING[i]==".":
            num=DD[int(TEMP)]
#            num=str(num)
            LIST_STRING.insert(i,str(num))
#            for y in LIST_STRING:
#                print(y,end='')
                    
        if len(LIST_STRING)-LENG==1:                
            del(LIST_STRING[-1])
        elif len(LIST_STRING)-LENG==2:
            del(LIST_STRING[-1])
            del(LIST_STRING[-1])
        else:
            pass            
            
        TEMP=''
        x=0
  
#    print(len(LIST_STRING))            
for y in LIST_STRING:
#    if y !='\n':
#        Ref_string+=y
#    else:
#        REFERENCES.append(Ref_string)
##        REFERENCES.sort()
#        Ref_string=''
#for k in REFERENCES:
    print(y,end='')
