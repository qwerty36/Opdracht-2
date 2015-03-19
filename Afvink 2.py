###############################################################################
##Afvinkopdracht 2, Blok 3, Richard Jansen HAN University Of Applied Sciences##
##9-03-2015####################################################################
###############################################################################

from tkinter import *
from tkinter import filedialog
import matplotlib.pyplot as plt

niets=Tk()
file = filedialog.askopenfile()
niets.destroy()
niets.mainloop()
lijst = []
lijst2 = []
codons = []
codonfreq = []
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

def main():
    x = startread(file)
    gimmeinfo(x)
    freq = {}
    freq = Counter(lijst)
    dictmod(freq)
    maakGrafiek()
   
def startread(seq):
    raw_data = ""
    startReading = False
    for regel in seq:
        if startReading:
            raw_data += regel[10:]
        if "ORIGIN" in regel:
            startReading = True
    sequence = raw_data.replace(' ','').replace('\n','').replace('\r','')
    return sequence

def gimmeinfo(seq):
    z, s = 0, 3
    codonseq = ""
    startindex = seq.index("atg")
    print('Startcodon on location: ' +str(startindex))
    for z in range (startindex, (len(seq)-startindex)):
        vanafstart = seq[startindex:]        
        codon = vanafstart[s-3:s]
        codonseq += codon
        if codon in ('taa', 'tga', 'tag'):
            print('Stopcodon on location: ' +str(z//3+startindex))
            break
        else:
            s += 3
    for i in range(0, len(codonseq),3):
        lijst.append(codonseq[i:i+3])

def dictmod(freq):
    lijst2.append(freq.keys())
    for x in freq:
        codons.append(x)
        codonfreq.append(freq[x])
        
def maakGrafiek():
    xlabels = codons
    x = np.arange(len(xlabels))
    y = codonfreq
    plt.xticks(x, xlabels, rotation="vertical")
    plt.bar(x,y)
    
main()