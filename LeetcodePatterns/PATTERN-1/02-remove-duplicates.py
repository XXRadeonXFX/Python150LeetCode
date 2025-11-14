def remove_duplicates(nums):
    i = 0
    j = 1
    while j < len(nums) and i < len(nums):
        if nums[i] != nums[j]:
            nums[i+1] = nums[j]
            i += 1
        j+= 1

    return i + 1
    
nums = [1,2,2,2,2,2, 3]
remove_duplicates(nums)
