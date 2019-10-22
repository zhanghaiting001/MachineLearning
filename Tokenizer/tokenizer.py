import re
import math

DICT ={}
#maxLen = 0
with open('./Data/dict.txt',encoding='utf-8') as file:
  for line in file.readlines():
    word = line.split()
    #maxLen = max(maxLen,len(word[0]))
    DICT[word[0]] = int(word[1])
#print(maxLen) #pku 17 dict.txt 16


def getDAG(substr):
  DAG = {}
  for i in range(len(substr)):
    indexDAG = []
    for j in range(i,len(substr)):
      if substr[i:j+1] in DICT:
        indexDAG.append(j)
    if not indexDAG:
      indexDAG.append(i)
      DICT[substr[i]] = 0
    DAG[i] = indexDAG
  #print(DAG)
  return DAG
  '''
  for substr in substrs: #所有句子组成的list，上面改为一个句子，循环放在外面。 另外下面的j= 上面j+1，为了与jieba保持一致，结果是对的。
    subDAG = []
    for i in range(len(substr)):
      indexDAG=[]
      for j in range(i+1,len(substr)+1):
        if substr[i:j] in DICT:
          #subDAG.append(substr[i:j])
          indexDAG.append(j)
      if not indexDAG:
        indexDAG.append(i+1)   #substr[i:i+1]
        DICT[substr[i]] = 0  #取不存在的word，dict会报错   
      subDAG.append(indexDAG)
    DAG.append(subDAG)
  print(DAG)
  print(len(DAG))
  return DAG
  '''
def getMaxLen(DAG,substr): #动态规划求最大路径
  N = len(substr)
  route = {}
  route[N] = (0,0)
  total = sum(DICT.values())
  logtotal = math.log(total)
  for i in range(N-1,-1,-1):
    route[i] = max((math.log(DICT[substr[i:x+1]] or 1)-logtotal+route[x+1][0],x) for x in DAG[i])
  #print(route)
  return route

"动态规划求最大路径，未求出，动态规划最大和最小路径不一样。jieba从右到左求最大概率词，动态规划，未找到对应抽象的题目"
'''
def getMaxDistance(DAG,substrs):
  for n in range(len(DAG)):
    lenString = len(DAG(n))
    substr = substrs[n]
    subDAG = DAG[n]
    subDis = [[0]*lenString for i in range(lenString)]   # n*n 
    maxDis = 0
    for i in range(lenString):
      for j in subDAG[i]:
        subDis[i][j] = DICT[substr[i:j]]
        if i :
          subDis[0][j] = max(subDis[0][i]+subDis[i][j],subDis[0][j])
'''
def getWordsList(route,substr):
  index = 0
  wordsList =[]
  while index<len(substr):
    i = route[index][1]
    wordsList.append(substr[index:i+1])
    index = i+1
  #print(wordsList)
  return wordsList

      

      

def cut(string):
  substrs = re.findall(r'\w+',string)
  for substr in substrs:
    DAG = getDAG(substr)
    route = getMaxLen(DAG,substr)
    yield getWordsList(route,substr)


if __name__ == '__main__':
  sentense = "我来到北京清华大学,我在清华大学上学"
  for words in cut(sentense):
    print(words)

