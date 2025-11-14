'''
PATTERN #1: ARRAYS - Two Pointer Technique
'''


def merge_sorted_array(nums1,nums2,m,n):
    p1 = m-1
    p2 = n-1
    p = len(nums1) -1
    
    while p >= 0 :
        if p1 >= 0 and p2 >= 0 and nums1[p1] >= nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -=1 
        elif p2 >= 0 :
            nums1[p] = nums2[p2]
            p2 -= 1 
        p -= 1


# nums1 = [4, 5, 6, 0, 0, 0]
# nums1 = [1,3,5,0,0,0]
# nums1 = [0]
nums1 = [1, 2, 3, 0, 0, 0]


# m = 3  # First 3 elements are real: [4, 5, 6]
# m = 1
m =3 
# nums2 = [1, 2, 3]
# nums2 = [2,4,6]
# nums2 = [1]
nums2 = [2, 5, 6]

# n = 1
# n = 3  # All 3 elements are real
n=3

merge_sorted_array(nums1,nums2,m,m)

# Note above solution will fail if the elements in the first array are smaller than 2n'd Array :

'''
nums1 = [1, 2, 3, 0, 0, 0]  # nums1 has SMALLER values
nums2 = [4, 5, 6]
m = 3, n = 3
'''

# So to save computation we can use below solution:
# More Memory efficient solution will will only loop till p2 ends ( p2 is the 2nd Array pointer ):
'''
PATTERN #1: ARRAYS - Two Pointer Technique
'''


def merge_sorted_array(nums1,nums2,m,n):
    p1 = m-1
    p2 = n-1
    p = len(nums1) -1
    
    while p2 >= 0 :
        if p1 >= 0 and p2 >= 0 and nums1[p1] >= nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -=1 
        elif p2 >= 0 :
            nums1[p] = nums2[p2]
            p2 -= 1 
        p -= 1


