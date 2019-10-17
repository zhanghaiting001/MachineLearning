from collections import Counter
import re


with open('./Data/pku_training.utf8','r') as file:
	text = file.read()
	words = re.findall(r'\w+',text)
	"\w能匹配汉字，字母数字下划线或着希腊字母，俄文等等"
	WORDS = Counter(words)
	print(len(WORDS))
	print(WORDS.most_common(10))
with open('./Data/dict_pku.txt','w',encoding='utf-8') as file:
	for word,count in WORDS.items():
		file.write(word+'\t'+str(count)+'\n')
