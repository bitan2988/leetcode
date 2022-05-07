# https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution:
    def maxOperations(self, nums, k: int) -> int:
        nums.sort()
        low = 0
        high = len(nums)-1
        count = 0
        while(low < high):
            if nums[low]+nums[high]==k:
                low +=1
                high -=1
                count +=1
            elif nums[low]+nums[high]>k:
                high -=1
            else:
                low +=1
        return count
                

'''
The abstract problem asks to count the number of disjoint pairs with a given sum k.
For each possible value x, it can be paired up with k - x.
The number of such pairs equals to min(count(x), count(k-x)), 
unless that x = k / 2, where the number of such pairs will be floor(count(x) / 2).
'''

def max_k_sum_pairs(nums, k):
    count_dict = {}
    for num in nums:
        if num in count_dict.keys():
            count_dict[num] +=1
        else:
            count_dict[num] = 1
    
    max_pairs = 0

    for num in nums:
        diff = k-num
        if num == diff:
            max_pairs += (count_dict[num]//2)
        elif diff in count_dict.keys():
            min_val = min(count_dict[num], count_dict[diff])
            max_pairs = max_pairs + min_val
            count_dict[num] = count_dict[num]-min_val
            count_dict[diff] = count_dict[diff]-min_val

            
        
        