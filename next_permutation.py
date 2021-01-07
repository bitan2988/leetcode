nums = [1, 2, 3]
flag = 0
if (len(nums)<2):
    pass
else:
    for i in range(len(nums)-1,0,-1):
        if (nums[i-1]<=nums[i]):
            l = i-1
            flag = 1
            break
    if (i==0):
        print("i==0")
        nums.reverse()
        print(nums)
        pass
    else:
        if (flag):
            for i in range(len(nums)-1,l,-1):
                if(nums[i]>nums[l]):
                    nums[l], nums[i] = nums[i], nums[l]
                    break
            nums = nums[:l+1] + nums[l+1:]
            print("flag != 0 but not i")
            print(nums)
        else:
            print("flag = 0 but not i")
            print(nums)
            nums = nums[::-1]
            print(nums)
