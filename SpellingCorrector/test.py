
def multipy(y):
	print('multipy')
	return y*y
"函数参数的multipy只计算一次"
def testFunc(x,y=multipy(10)):
	return x*y

#print(testFunc(20))
#print(testFunc(10))

def testMax(x):
	return countDic[x]
countDic = {'a':10,'b':10,'c':3,'d':3}
"dict countDic迭代是key .values()迭代是values .items()是key，value对"
for x in countDic: #key 如果想两个，需要countDic.items()
	print(x)  # a b c d

"max sorted 的时间复杂度??查找dict中value的时间复杂度??查找key是o(1)"
print(max(countDic,key=testMax)) #'a'
print(max(countDic,key=lambda x:countDic[x])) #a
maxvalues = max(countDic.values())
print([k for k,v in countDic.items() if v==maxvalues])  #这个时间复杂度也不低
print(sorted(countDic,key=lambda d:countDic[d],reverse=True)) #['a', 'b', 'c', 'd']
print(sorted(countDic.items(),key=lambda d:d[1],reverse=True)) #[('a', 10), ('b', 10), ('c', 3), ('d', 3)]
