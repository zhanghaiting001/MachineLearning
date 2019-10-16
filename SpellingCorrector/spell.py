import re
from collections import Counter

def words(text):
	return re.findall(r'\w+',text.lower()) 

#WORDS = Counter(words(open('big.txt').read()))  #file没有close

with open('big.txt') as f:
	#text = f.read()   #这样要分配内存？应该是都要分配的
	#print(type(text),len(text),type(words(text)))  # str , 6488666 ,list
	WORDS = Counter(words(f.read()))   
#print(type(WORDS),len(WORDS))  # 32198
#print(WORDS['a']) #返回 a的次数  21124
#print(WORDS.most_common(10)) #显示次数最多的10个单词及次数
#print(sum(WORDS.values()))

#print(WORDS['qbwe23'])  #访问的不存在时，返回0 dict时，dict.get(key,default=None),直接dict['qbwe23']会报错

#从WORDS数量来说，构造 距离相近的单词，远比每个计算速度快的多！！！太慢了
def getNearstWords(string):
	dis ={}
	for word, _ in WORDS.items():
		dis[word]=minDistance(string,word)
	sortedDis = sorted(dis.items(),key=lambda d:d[1])
	#print(sortedDis[:20])
	n = sortedDis[0][1]
	candidate ={}
	for i in range(len(sortedDis)):
		if sortedDis[i][1] == n:
			candidate[sortedDis[i][0]] = WORDS[sortedDis[i][0]]
		else:
			break
	#print(candidate)
	sortedCandi = sorted(candidate.items(),key=lambda d:d[1],reverse=True)
	return sortedCandi[0][0]


def minDistance(word1,word2):
	m = len(word1)
	n = len(word2)
	dis= [[0] * (n+1) for _ in range(m+1)]

	for i in range(m+1):
		for j in range(n+1):
			if i==0:
				dis[i][j] = j
			elif j==0:
				dis[i][j] = i
			else:
				if word1[i-1]==word2[j-1]:
					dis[i][j] = min(dis[i-1][j]+1,dis[i][j-1]+1,dis[i-1][j-1])
				else:
					dis[i][j] = min(dis[i-1][j]+1,dis[i][j-1]+1,dis[i-1][j-1]+1)
				#if dis[i][j] >2:  #因为有 i=1 j=8 的情况，所以完全不行  动态规划，没法只找1,2编辑距离的词。
				#	return m+n  #
	return dis[i][j]


def test(string):
	if WORDS[string] > 0:
		return string
	else:
		return getNearstWords(string)

def spelltest(tests, verbose=False):
    "Run correction(wrong) on all (right, wrong) pairs; report results."
    import time
    start = time.clock()
    good, unknown = 0, 0
    n = len(tests)
    for right, wrong in tests:
        w = test(wrong)
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
	print(test('qbwe23'))
	print(test('helo'))  #必须要小写
	print(test('the'))
	print(test('speling'))
	print(test('korrectud'))
	print(test('bycycle'))
	print(test('inconvient'))
	print(test('arrainged'))
	print(test('peotry')) #entry 应该 poetry  考虑transpose
	print(test('peotryy')) #petya 应该poetry
	print(test('word'))  
	print(test('quintessential'))  #essential  #距离大于2可以不判断了
	spelltest(Testset(open('spell-testset1.txt')))
	#spelltest(Testset(open('spell-testset2.txt')))
