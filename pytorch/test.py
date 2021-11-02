import nltk
import matplotlib.pyplot as plt
from nltk.corpus import gutenberg as gb

def validate_zipf(text,ranklimit):
    fdist=nltk.FreqDist([w for w in text if w.isalpha()])
    x=range(ranklimit)
    freq=[]
    for key in fdist.keys():
       freq.append(fdist[key])
    y=sorted(freq,reverse=True)[:ranklimit]
    plt.plot(x,y)
    plt.savefig('./ex.jpg', bbox_inches='tight', dpi=300)

def test():
    text=gb.words(fileids=['shakespeare-hamlet.txt'])
    validate_zipf(text,150)
test()