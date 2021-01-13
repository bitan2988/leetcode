#https://leetcode.com/problems/first-missing-positive/

#https://www.youtube.com/watch?v=-lfHWWMmXXM



#nums =  [1,1]
nums = [1]
i = 0
while (i<len(nums)):
  val = nums[i]
  if (val>=len(nums) or val<=0 or val==(i+1) or nums[val-1]==nums[i]):
    i +=1
  else:
      nums[val-1], nums[i] = nums[i], nums[val-1]
print(nums)
flag = 1
for i in range(len(nums)):
  #print("i ",i)
  if (nums[i]<=0 or nums[i]!=(i+1)):
    flag = 0 
    break
#rint("i outside = ",i)
if (flag):
  print(i+2)
else:
  print(i+1)