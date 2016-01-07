#encoding=utf-8

from cutter import *

import codecs
#處理編碼的套件

files = ['data/text1.txt', 'data/text2.txt', 'data/text3.txt', 'data/text4.txt', 'data/text5.txt', 'data/text6.txt', 'data/text7.txt']

import csv

spamWriter = csv.writer(open('output/result.csv', 'wb'))

for f in files:
    text = codecs.open(f,"r","utf-8")
    #讀取存成TXT檔的文字，讀入後統一轉成UTF-8格式

    cutter = Cutter()

    text_new = text.read()

    cutter = Cutter()

    words_freqs = cutter.full_cut(text_new)

    spamWriter.writerow([s.encode("utf-8") for s in words_freqs])

    for s in words_freqs:
        if len(s) > 3:
            print s
