# https://leetcode.com/problems/longest-common-prefix/


# BINARY-SEARCH
class Solution:   
    # returns if all the words have the prefix till word_of_min_len[0:mid]
    def isCP(self, strs, leng)->bool:
        sub_stri = strs[0][:leng]
        
        for i in range(1, len(strs)):
            if strs[i][0:leng]!=sub_stri:
                return False
        return True
    
    def longestCommonPrefix(self, strs) -> str:
        if len(strs)==0:
            return ""
        min_len = int(pow(2, 31)-1)
        
        for stri in strs:
            min_len = min(min_len, len(stri))
            
        low = 1
        high = min_len
        
        while low <= high:
            mid = (low+high)//2
            if (self.isCP(strs, mid)):
                low = mid+1
            else:
                high = mid-1
        return strs[0][:(low+high)//2]


# minimum recursion depths exceeded 
# It is a guard against a stack overflow
# Python (or rather, the CPython implementation) doesn't optimize tail recursion, 
# and unbridled recursion causes stack overflows. 
# import sys
# print(sys.getrecursionlimit())
class Solution:
    def prefix_checker(self, strs, low, high):
        if (low>=high):
            return strs[low]
        else:
            mid = low+high//2
            left_prefix = self.prefix_checker(strs, low, mid)
            right_prefix = self.prefix_checker(strs, mid+1, high)
            
        return self.common_prefix(left_prefix, right_prefix)
    
    def common_prefix(self, left, right):
        mini = min(len(left), len(right))
        
        for i in range(mini):
            if left[i]!=right[i]:
                return left[:i]
        return left[:mini]
    
    def longestCommonPrefix(self, strs) -> str:
        if len(strs)==0:
            return ""
        return self.prefix_checker(strs, 0, len(strs)-1)
     

        
        
        
                