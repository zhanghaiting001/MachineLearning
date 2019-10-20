
import sys
INF = sys.maxsize  #the largest supported length of containers

"图存在数组中"
Map = [[0,1,12,INF,INF,INF],[INF,0,9,3,INF,INF],[INF,INF,0,INF,5,INF],[INF,INF,4,0,13,15],[INF,INF,INF,INF,0,4],[INF,INF,INF,INF,INF,0]]


def getMinDistance(Map,v0):
	v0 -= 1 #顶点储存的时候序号-1。
	N = len(Map)
	dis =[INF] * N
	vis =[0] *N
	vis[v0] = 1
	for i in range(N):
		dis[i] = Map[v0][i]
	indexlist = [[v0+1] for i in range(N)] #+1代表顶点编号
	for j in range(N-1):
		minDis = INF
		temp = -1
		for i in range(N):
			if vis[i] ==0 and dis[i] < minDis:
				minDis = dis[i]
				temp = i
		if temp == -1:
			break  #有不连通的时候，更新完了，退出
		print(temp)
		vis[temp] = 1
		for i in range(N):
			if dis[i] > dis[temp]+Map[temp][i]:
				dis[i] = dis[temp]+Map[temp][i]
				indexlist[i] =[]
				"=直接赋值，会让两个list改变同步，所以用列表解析式，浅拷贝，单元素可以，涉及复杂对象就会失败"
				indexlist[i] = [j for j in indexlist[temp]]    #从temp转折，temp之前的转折点已经确认好
				indexlist[i].append(temp+1) #+1代表顶点编号
	print(dis)
	print(indexlist)

getMinDistance(Map,1)


