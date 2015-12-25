#encoding=utf-8

from cutter import *

import codecs
#處理編碼的套件

text = codecs.open("data/text3.txt","r","utf-8")
#讀取存成TXT檔的文字，讀入後統一轉成UTF-8格式
'''
text_new =""
for line in text.readlines():
    text_new += "".join(line.split('\n'))
#在這邊先做一個小處理，把不同行的文章串接再一起，如果未來要做一些去除標點符號的處理也會是在這邊。
'''

text_new = text.read()

cutter = Cutter()

words_freqs = cutter.cut(text_new, 4)

for i in words_freqs:
    if(i[1] > 2):
        print i[0],i[1]
