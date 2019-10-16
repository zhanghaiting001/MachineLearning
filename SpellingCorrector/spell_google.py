"""Spelling Corrector in Python 3; see http://norvig.com/spell-correct.html

Copyright (c) 2007-2016 Peter Norvig
MIT license: www.opensource.org/licenses/mit-license.php
"""

################ Spelling Corrector 

import re
from collections import Counter

def words(text): return re.findall(r'\w+', text.lower())

WORDS = Counter(words(open('big.txt').read()))

def P(word, N=sum(WORDS.values())): #sum() 会不会每次执行？？
    "Probability of `word`." #这就是一行字符串，只是运行一下，不影响任何变量，不建议这样注释
    return WORDS[word] / N  #去掉N速度基本也没有什么提升。

def correction(word): 
    "Most probable spelling correction for word."
    return max(candidates(word), key=P)

def candidates(word): 
    "Generate possible spelling corrections for word."
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])

def known(words): 
    "The subset of `words` that appear in the dictionary of WORDS."
    return set(w for w in words if w in WORDS)  #set去重   列表解析

def edits1(word):
    "All edits that are one edit away from `word`."
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]  #n+1   len(word)=n
    deletes    = [L + R[1:]               for L, R in splits if R]  #n
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1] #n-1  R[2] index out of range  R[2:] '' 没有字符
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters] #n*26
    inserts    = [L + c + R               for L, R in splits for c in letters] #(n+1)*26   403
    #print(len(set(deletes + transposes + replaces + inserts)))
    #print(len(deletes + transposes + replaces + inserts))
    return set(deletes + transposes + replaces + inserts)  #speling list 403 set 390   数量都是可以计算的

def edits2(word): 
    "All edits that are two edits away from `word`."
    #print(len(set(e2 for e1 in edits1(word) for e2 in edits1(e1))))
    #print('edit2',len([e2 for e1 in edits1(word) for e2 in edits1(e1)]))
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))  #speling set 70184 list 162150

################ Test Code 

def unit_tests():
    assert correction('speling') == 'spelling'              # insert
    assert correction('korrectud') == 'corrected'           # replace 2
    assert correction('bycycle') == 'bicycle'               # replace
    assert correction('inconvient') == 'inconvenient'       # insert 2
    assert correction('arrainged') == 'arranged'            # delete
    assert correction('peotry') =='poetry'                  # transpose
    assert correction('peotryy') =='poetry'                 # transpose + delete
    assert correction('word') == 'word'                     # known
    assert correction('quintessential') == 'quintessential' # unknown
    assert words('This is a TEST.') == ['this', 'is', 'a', 'test']
    assert Counter(words('This is a test. 123; A TEST this is.')) == (
           Counter({'123': 1, 'a': 2, 'is': 2, 'test': 2, 'this': 2}))
    assert len(WORDS) == 32198 #32192
    assert sum(WORDS.values()) == 1115585 #1115504
    assert WORDS.most_common(10) == [
     ('the', 79809), #79808
     ('of', 40024),
     ('and', 38312),#38311
     ('to', 28765),
     ('in', 22023),#22020
     ('a', 21124),
     ('that', 12512),
     ('he', 12401),
     ('was', 11410),
     ('it', 10681)]
    assert WORDS['the'] == 79809 #79808
    assert P('quintessential') == 0
    #assert 0.07 < P('the') < 0.08
    return 'unit_tests pass'

def spelltest(tests, verbose=False):
    "Run correction(wrong) on all (right, wrong) pairs; report results."
    import time
    start = time.clock()
    good, unknown = 0, 0
    n = len(tests)
    for right, wrong in tests:
        w = correction(wrong)
        good += (w == right)
        if w != right:
            unknown += (right not in WORDS)
            if verbose:
                print('correction({}) => {} ({}); expected {} ({})'
                      .format(wrong, w, WORDS[w], right, WORDS[right]))
    dt = time.clock() - start
    print('{:.0%} of {} correct ({:.0%} unknown) at {:.0f} words per second '
          .format(good / n, n, unknown / n, n / dt))
    
def Testset(lines):
    "Parse 'right: wrong1 wrong2' lines into [('right', 'wrong1'), ('right', 'wrong2')] pairs."
    return [(right, wrong)
            for (right, wrongs) in (line.split(':') for line in lines)
            for wrong in wrongs.split()]

if __name__ == '__main__':
    print(unit_tests())
    spelltest(Testset(open('spell-testset1.txt')))
    spelltest(Testset(open('spell-testset2.txt')))
