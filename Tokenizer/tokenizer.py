import re

DICT ={}
maxLen = 0
with open('./Data/dict.txt',encoding='utf-8') as file:
  for line in file.readlines():
    word = line.split()
    maxLen = max(maxLen,len(word[0]))
    DICT[word[0]] = int(word[1])
print(maxLen) #pku 17 dict.txt 16


def getDAG(substrs):
  DAG = []
  for substr in substrs:
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
      
      
     
      

      

def cut(string):
  substrs = re.findall(r'\w+',string)
  DAG = getDAG(substrs)



if __name__ == '__main__':
  print(cut("小明硕士毕业于中国科学院计算所缪繆緢，后在日本京都大学深造"))

