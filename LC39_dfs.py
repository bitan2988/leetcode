#https://www.youtube.com/watch?v=irFtGMLbf-s
#DFS


def dfs(res, comb, candidates, target, start):
    if (target==0):
        temp = []
        for i in range(len(comb)):    #shallow copy and deep copy
            temp.append(comb[i])
        res.append(temp)
        return
    for i in range(start,len(candidates)):
        if (candidates[i]>target):
            break
        if target-candidates[i]>=0:
            comb.append(candidates[i])
            dfs(res, comb, candidates, target-candidates[i],i)
            comb.pop()  #restoring for next call




if __name__ == "__main__":
    candidates = [2,6,4,3,7]
    target  = 7
    res = []
    if (len(candidates)==0):
        print("NULL")
    candidates.sort()
    comb = []
    dfs(res, comb, candidates,target, 0)

    print(res)
