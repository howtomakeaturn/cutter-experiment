#encoding=utf-8

import codecs
#處理編碼的套件
import operator
##處理字典檔排序的套件

text = codecs.open("data/text3.txt","r","utf-8")
#讀取存成TXT檔的文字，讀入後統一轉成UTF-8格式

text_new =""
for line in text.readlines():
    text_new += "".join(line.split('\n'))
#在這邊先做一個小處理，把不同行的文章串接再一起，如果未來要做一些去除標點符號的處理也會是在這邊。

class Cutter:

    def __init__(self):
        self.words = [] #存放擷取出來的字詞
        self.words_freq = {} #存放字詞:計算個數

    def ngram(self, text, n): #第一個參數放處理好的文章，第二個參數放字詞的長度單位

        for w in range(len(text)-(n-1)): #要讀取的長度隨字詞長度改變
            self.words.append(text[w:w+n])    #抓取長度w-(n-1)的字串

        for word in self.words:
            if word not in self.words_freq:               #如果這個字詞還沒有被放在字典檔中
                self.words_freq[word] = self.words.count(word) #就開一個新的字詞，裡面放入字詞計算的頻次

        self.words_freq = sorted(self.words_freq.iteritems(),key=operator.itemgetter(1),reverse=True) #change words_freq from dict to list
        return self.words_freq

cutter = Cutter()

words_freqs = cutter.ngram(text_new, 4)

for i in words_freqs:
    if(i[1] > 3):
        print i[0],i[1]
'''

words_freqs = ngram(text_new,2)

for i in words_freqs:
    print i[0],i[1]
'''