import re

DICT ={}
maxLen = 0
with open('./Data/dict.txt') as file:
	for line in file.readlines():
		word = line.split()
		maxLen = max(maxLen,len(word[0]))
		DICT[word[0]] = int(word[1])
print(maxLen) #pku 17 dict.txt 16


def getDAG(string):
	substrs = re.findall(r'\w+',string)
	print(substrs)
	DAG = []
	for substr in substrs:
		for i in range(len(substr)):
			subDAG=[]
			for j in range(i+1,len(substr)+1):
				if substr[i:j] in DICT:
					subDAG.append(substr[i:j])
			if not subDAG:
				subDAG.append(substr[i])
				DICT[substr[i]] = 0  #取不存在的word，dict会报错
			DAG.append(subDAG)
	return DAG

def getMaxDistance(DAG):
	for wordlist in DAG:
		for word in wordlist:
			

def cut(string):
	DAG = getDAG(string)



if __name__ == '__main__':
	print(cut("小明硕士毕业于中国科学院计算所缪繆緢，后在日本京都大学深造"))

