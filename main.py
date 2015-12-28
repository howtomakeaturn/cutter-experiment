#encoding=utf-8

from cutter import *

import codecs
#處理編碼的套件

text = codecs.open("data/text4.txt","r","utf-8")
#讀取存成TXT檔的文字，讀入後統一轉成UTF-8格式

cutter = Cutter()

text_new = text.read()

cutter = Cutter()

#words_freqs = cutter.cut(text_new, 3)

#for i in words_freqs:
  #  print i

words_freqs = cutter.full_cut(text_new)

for i in words_freqs:
    print i