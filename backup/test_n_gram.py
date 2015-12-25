#!encoding=utf-8

def list2freqdict(mylist):
    mydict=dict()
    for ch in mylist:
        mydict[ch]=mydict.get(ch,0)+1
    return mydict

sentence=u'吃葡萄不吐葡萄皮，不吃葡萄倒吐葡萄皮。'
chlist=[ch for ch in sentence]

#print(chlist)
chfreqdict=list2freqdict(chlist)
#print(chfreqdict)

from operator import itemgetter
chfreqsorted=sorted(chfreqdict.items(), key=itemgetter(1), reverse=True)
#print(chfreqsorted)

def list2bigram(mylist):
    return [mylist[i:i+2] for i in range(0,len(mylist)-1)]

def list2trigram(mylist):
    return [mylist[i:i+3] for i in range(0,len(mylist)-2)]

chbigram=list2bigram(chlist)
chtrigram=list2trigram(chlist)
#print(chbigram)
#print(chtrigram)

def bigram2freqdict(mybigram):
    mydict=dict()
    for (ch1,ch2) in mybigram:
        mydict[(ch1,ch2)]=mydict.get((ch1,ch2),0)+1
    return mydict

def trigram2freqdict(mytrigram):
    mydict=dict()
    for (ch1,ch2,ch3) in mytrigram:
        mydict[(ch1,ch2,ch3)]=mydict.get((ch1,ch2,ch3),0)+1
    return mydict

bigramfreqdict=bigram2freqdict(chbigram)
trigramfreqdict=trigram2freqdict(chtrigram)

#print bigramfreqdict

#print trigramfreqdict

def freq2report(freqlist):
    chs=str()
    print('Char(s)\tCount')
    print('=============')
    for token, num in freqlist.iteritems():
#    for (token,num) in freqlist:
        if num > 2:
            for ch in token:
                chs=chs+ch
            print chs + ' ' + str(num)
            chs=''
    return

#freq2report(chfreqsorted)
#freq2report(bigramfreqdict)
#freq2report(trigramfreqdict)

def makeBiGram(text):
    chlist=[ch for ch in text]
    t = list2bigram(chlist)
    t = bigram2freqdict(t)
    #print t
    freq2report(t)

file = open('text2.txt', 'r')
text = file.read().decode('utf-8')

makeBiGram(text)

file = open('text1.txt', 'r')
text = file.read().decode('utf-8')

makeBiGram(text)