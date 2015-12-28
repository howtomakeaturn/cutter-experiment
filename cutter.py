#encoding=utf-8

import operator
##處理字典檔排序的套件
import re

class Cutter:

    def __init__(self):
        self.words_freq = {} #存放字詞:計算個數
        self.result = []
        self.pure_texts = []

    def break_by(self, char):
        k = []
        for i in self.pure_texts:
            j = [x.strip() for x in i.split(char)]
            k = k + j

        self.pure_texts = k

    def break_punctuations(self):
        self.break_by(u'，')
        self.break_by(u'。')
        self.break_by(u'「')
        self.break_by(u'」')
        self.break_by(u'『')
        self.break_by(u'』')
        self.break_by(u'…')
        self.break_by(u'：')
        self.break_by(u'、')

    def remove_english_alphabet(self, text):
        result = re.sub('[A-Za-z]+', ' ', text)
        return result

    def remove_arabic_numerals(self, text):
        result = re.sub('[0-9]+', ' ', text)
        return result

    def full_cut(self, text):
        result = []
        result += self.cut(text, 4)
        current_words = result[:]
        self.words_freq = {}
        text2 = text
        for word in current_words:
           text2 = text2.replace(word, '')

        result += self.cut(text2, 3)

        current_words = result[:]
        self.words_freq = {}
        text3 = text2
        for word in current_words:
           text3 = text3.replace(word, '')

        result += self.cut(text3, 2)

        return result

    def break_new_lines(self):
        self.break_by("\n")

    def break_spaces(self):
        self.break_by(" ")

    def cut(self, text, n):
        text = self.remove_english_alphabet(text)

        text = self.remove_arabic_numerals(text)

        self.pure_texts = [text]

        self.break_punctuations()

        self.break_new_lines()

        self.break_spaces()

        self.break_by(u'的')

        for i in self.pure_texts:
            self.eat(i, n)

        return self.get_result()

    def eat(self, text, n): #第一個參數放處理好的文章，第二個參數放字詞的長度單位
        words = [] #存放擷取出來的字詞

        for w in range(len(text)-(n-1)): #要讀取的長度隨字詞長度改變
            words.append(text[w:w+n])    #抓取長度w-(n-1)的字串

        for word in words:
            if word not in self.words_freq:               #如果這個字詞還沒有被放在字典檔中
                self.words_freq[word] = words.count(word) #就開一個新的字詞，裡面放入字詞計算的頻次
            else:
                self.words_freq[word] += words.count(word) #就開一個新的字詞，裡面放入字詞計算的頻次

    def get_result(self):
        words_freq = sorted(self.words_freq.iteritems(),key=operator.itemgetter(1),reverse=True) #change words_freq from dict to list
        result = []

        for i in words_freq:
            if(i[1] > 2):
                result.append(i[0])
        return result

text1 = u'''
大家都知道，台灣的教育體制相當重視排名競爭，在我們自己的求學過程中，也都親身經驗過與同儕相較高下，互比短長的成績競賽。但我們比較不明白的是，這個漫長的競爭過程對我們自己有什麼影響？或者問說，這個競爭體制到底帶給我們什麼樣人格特質，以及什麼樣的社會後果？
'''

text2 = u'''
首先，我們可以簡單的觀察到競爭是以家庭作為動員的單位，而家庭經濟狀況經常決定了諸多學習的條件。舉例來說，我有一位醫生的朋友，考量到英語教育對孩子的重要性，決定把孩子送到全英語（並且標榜「全外師」）的小學念書，在暑假時也會送孩子到英語系國家去體驗生活。可以想見如此教育肯定昂貴，一般家庭不可能付得起如此的教育支出。即便這並不直接保證孩子的將來，但邏輯上來說，這樣的小孩在未來考試時（至少在英語能力上），顯然擁有較多的機會。再者，家庭經濟能力對下一代的影響並不僅止於單一科目，在所謂的多元入學方案中，孩子的確可能因為具有從小習得的某種才藝，而能掌握更多的選擇路徑。
'''

cutter = Cutter()
cutter.eat(text1, 2)
cutter.eat(text2, 2)
result = cutter.get_result()

assert result[0] == u'孩子'
assert result[2] == u'英語'

cutter = Cutter()
result = cutter.cut(text1 + text2, 2)

#assert result[0] == u'孩子'
#assert result[2] == u'英語'
