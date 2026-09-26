class Solution:
    def isBipartite(self, V, edges):
        colour = [-1] * V 
        adj = [[] for i in range(V)]
        for u , v in edges:
            adj[u].append(v)
            adj[v].append(u)
    
        for i in range(V):
            if colour[i] != -1:
                continue
            colour[i] = 0 
            q  = deque()
            q.append(i)
            while q:
                node = q.popleft()
                for nei in adj[node]:
                    if colour[nei] == -1:
                        if colour[node] == 0 :
                            colour[nei] = 1
                            q.append(nei)
                        else:
                            colour[nei] = 0
                            q.append(nei)
                    else:
                        if colour[nei] == colour[node]:
                            return False
            
        return True
                    



        