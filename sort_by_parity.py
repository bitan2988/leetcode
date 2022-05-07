# https://leetcode.com/problems/sort-array-by-parity/

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]: 
        fwd = 0
        back = len(nums)-1
        while(fwd<back):
            while(fwd<len(nums) and not(nums[fwd]&1)):
                fwd +=1
            while(back>-1 and nums[back]&1):
                back -=1
                
            if(fwd<back):
                temp = nums[fwd]
                nums[fwd] = nums[back]
                nums[back] = temp
                
        return nums
            
            
        