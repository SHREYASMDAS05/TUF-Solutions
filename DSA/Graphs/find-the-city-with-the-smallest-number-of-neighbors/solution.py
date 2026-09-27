class Solution:
    def findCity(self, n, m, edges, distanceThreshold):
        dist = [[float('inf')]*n for i in range(n)]
        for i in range(n):
            dist[i][i] = 0
        for u , v , w in edges:
            dist[u][v] = w
            dist[v][u] = w
        for k in range(n):
            for i in range(n):
                for j in range(n):

                    dist[i][j] = min(dist[i][j] , dist[i][k] + dist[k][j])

        res = [0] * (n)
        for i in range(n):
            cnt = 0
            for j in range(n):
                if dist[i][j] <= distanceThreshold:
                    cnt += 1
            res[i] = cnt
        min_count = float('inf')
        ans = -1

        for i in range(n-1 , -1 , -1):
            if res[i] < min_count:
                min_count = res[i]
                ans = i

        return ans
