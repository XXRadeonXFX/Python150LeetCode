
def remove_elem(nums,val):
    i = 0
    j = 0
    
    while j < len(nums) and i < len(nums):
        if nums[j] == val:
            j += 1
        else :
            nums[i] = nums[j]
            i += 1
            j += 1
    return i 


# nums= [3, 2, 2, 3, 4, 2]
# val = 2


nums=[0, 1, 2, 2, 3, 0, 4, 2]
val = 2

remove_elem(nums,val)
