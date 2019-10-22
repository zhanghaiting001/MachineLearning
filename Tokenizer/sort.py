from random import randint
import timeit

def generateRandomArray(n,min,max):
	return [randint(min,max) for x in range(n)]

def generateNearlyOrderedArray(n,swapTimes):
	arr = [i for i in range(n)]
	for j in range(swapTimes):
		pos1 = randint(0,n-1)
		pos2 = randint(0,n-1)
		arr[pos1],arr[pos2] = arr[pos2],arr[pos1]
	return arr

def isSorted(nums):
	for i in range(len(nums)-1):
		if nums[i] > nums[i+1]:
			return False
	return True

def testSort(func,nums):
	nums = func(nums)
	assert isSorted(nums), "排序算法错误\n"
"nums1=nums[:] 拷贝，改变nums1不会改变nums,nums1=nums，改变任何一个两个都会变。"


"nums.sort(reverse=False) 排序，默认顺序从小到大的顺序排列" #比较性能
"由小到大排序"
def bubbleSort(nums):
	n = len(nums)
	swap = False
	for i in range(n-1):
		swap = False
		for j in range(n-i-1):
			if nums[j+1] < nums[j]:
				nums[j],nums[j+1] = nums[j+1],nums[j]
				swap = True
			#print(nums)
		#print("one time")
		if not swap:
			print("if no swap,end early")
			break
	#print(nums)
	return nums

def selectionSort(nums): #选择排序，最好也是O(n^2)
	n = len(nums)
	for i in range(n-1):
		maxindex = 0
		for j in range(1,n-i):
			if nums[j] > nums[maxindex]:  #不稳定，为了稳定 >= 就会得到最后一个最大值，稳定
				maxindex = j
		nums[maxindex],nums[n-1-i] = nums[n-1-i],nums[maxindex]
		#print(nums)
	#print(nums)
	return nums

def insertionSort(nums): #从前往后插入，最好也是O(n^2) 从前往后也稳定
	n = len(nums)
	for i in range(1,n):
		for j in range(i):
			if nums[i] < nums[j]:
				nums[i],nums[j] = nums[j],nums[i]
	#print(nums)
	return nums

def insertionSort1(nums): #从后往前插入，最好是O(n)   从后往前稳定
	n = len(nums)
	for i in range(1,n):
		index = i
		for j in range(i-1,-1,-1):
			if nums[index] < nums[j]: #交换多次，也可以只后移nums[j]直到找到合适的index插入，不写了
				nums[index],nums[j] = nums[j],nums[index]
				index = j
			else:
				break
	#print(nums)
	return nums

"上面三种排序为O(n^2)"




func1 = insertionSort1
nums1 = generateRandomArray(10,2,50)

if __name__ == '__main__':
	#print(generateRandomArray(10,2,50))
	nums = [3,44,38,5,36,2,4]
	nums1 = [1,2,3,4,5,21]
	#bubbleSort(nums)
	#selectionSort(nums)
	insertionSort1(nums)
	t1 = timeit.Timer('testSort(func1,nums1)','from sort import testSort,func1,nums1')
	print('func1:%s s' %t1.timeit(number=1))