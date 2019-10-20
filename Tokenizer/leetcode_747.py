import sys
class Solution:
    def networkDelayTime(self, times, N, K):
        INF = sys.maxsize
        Map = [[INF] * (N+1) for i in range(N+1)]
        for i in range(N+1):
            Map[i][i] =0
        for i in range(len(times)):
            u,v,w= times[i] 
            Map[u][v] = w
        #print(Map)
        dis = [INF] * (N+1)  #dis[0] = INF,最后删掉就好
        dis[0] = 0 #遍历不到
        vis = [0] * (N+1) #vis[0]  遍历不到
        vis[K] = 1 #1代表已经遍历过了
        for i in range(1,N+1):
            dis[i] = Map[K][i] 
        for i in range(N-1):
            minDis = INF
            temp = -1
            for j in range(1,N+1):
                if vis[j]==0 and dis[j]<minDis:
                    minDis = dis[j]
                    temp = j
            if temp == -1:
                return -1
            vis[temp] = 1
            for j in range(1,N+1):                    
                dis[j] = min(dis[j],dis[temp]+Map[temp][j])
        maxtime = max(dis)
        if maxtime == INF:
            maxtime = -1
        return maxtime
s = Solution()
times = [[2,4,10],[5,2,38],[3,4,33],[4,2,76],[3,2,64],[1,5,54],[1,4,98],[2,3,61],[2,1,0],\
    [3,5,77],[5,1,34],[3,1,79],[5,3,2],[1,2,59],[4,3,46],[5,4,44],[2,5,89],[4,5,21],[1,3,86],[4,1,95]]
times1 =[[2,1,1],[2,3,1],[3,4,1]]
s.networkDelayTime(times1,4,2)