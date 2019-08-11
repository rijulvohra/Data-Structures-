def pythagorean_triplet(nums):
    for i in range(0,len(nums)):
        nums[i] = nums[i]*nums[i]
    
    nums.sort()
    i = len(nums) - 1 
    f = 0
    r = i-1
    for i in range(i,-1,-1):
        if nums[f] + nums[r] < nums[i] and f!=r:
            f += 1 
        if nums[f] + nums[r] > nums[i] and f!=r:
            r -= 1
        if nums[f] + nums[r] == nums[i] and f!=r:
            return True
        if f == r:
            f = 0
            r = i-1
    else:
        return False

nums = [int(i) for i in input().split()]
print(pythagorean_triplet(nums))
    
    
