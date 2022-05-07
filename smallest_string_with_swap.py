
# https://leetcode.com/problems/smallest-string-with-swaps/

class UnionFind:
    def __init__(self, n):
        self.size = n
        self.parent = [i for i in range(n)]
        
    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]
    
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv: return False
        self.parent[pu] = pv
        return True
    
    def getGroups(self):
        groups = defaultdict(list)
        for u in range(self.size):
            groups[self.find(u)].append(u)
        return groups.values()
        

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs) -> str:
        n, m = len(s), len(pairs)
        uf = UnionFind(n)
        for u, v in pairs:
            uf.union(u, v)
            
        groups = uf.getGroups()
        res = ['-'] * n
        for group in groups:
            chars = [s[i] for i in group]
            chars.sort()
            group.sort()
            for i, c in zip(group, chars):
                res[i] = c
        return "".join(res)



'''
Time: O(NlogN + M), where N is length of string s, M is number of pairs.
Space: O(N)
'''