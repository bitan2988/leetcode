# https://leetcode.com/problems/backspace-string-compare/

class Solution(object):
    def backspaceCompare(self, S, T):
        
        s_org = ""
        skip = 0
        for i in range(len(S)-1, -1, -1):
            if S[i]=='#':
                skip +=1
            elif skip>0:
                skip -=1
            else:
                s_org +=S[i]
                
        t_org = ""
        skip = 0
        for i in range(len(T)-1, -1, -1):
            if T[i]=='#':
                skip +=1
            elif skip>0:
                skip -=1
            else:
                t_org +=T[i]
                
        if s_org == t_org:
            return True
        else:
            return False