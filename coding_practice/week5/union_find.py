"""
Number of Connected Components in an Undirected Graph - LeetCode #323
"""

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py: return False
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        return True

def countComponents(n, edges):
    uf = UnionFind(n)
    count = n
    for u,v in edges:
        if uf.union(u,v):
            count -= 1
    return count

# Test
print(countComponents(5, [[0,1],[1,2],[3,4]])) # 2
