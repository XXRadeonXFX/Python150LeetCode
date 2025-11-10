class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last = len(nums) -1 
        k = k % last

        self.reverse(nums,0,last-1)
        self.reverse(nums,0,k-1)
        self.reverse(nums,k,last-1)

    
    def reverse(self, nums , start , stop):
        while start < stop:
            nums[start], nums[stop] = nums[stop], nums[start]
            start += 1 
            stop -= 1

""" 

## The Main Idea

Instead of moving elements one by one (which is slow), we use a **clever trick with reversing**!

---

## Part 1: The `reverse` Helper Function

```python
def reverse(self, nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1
```

This function reverses a portion of the array from `start` to `end`.

**Example:** Reverse `[1,2,3,4,5]` from index 0 to 4

- **Step 1:** Swap `nums[0]` and `nums[4]` → `[5,2,3,4,1]`
- **Step 2:** Swap `nums[1]` and `nums[3]` → `[5,4,3,2,1]`
- **Step 3:** `start = 2, end = 2` (they meet, stop!)

**Result:** `[5,4,3,2,1]` ✅

---

## Part 2: The Main `rotate` Function

```python
n = len(nums)
k = k % n
```
- `n` = length of array
- `k % n` handles when k is larger than array size

---

### The 3-Step Magic Formula

Let's use: `nums = [1,2,3,4,5,6,7], k = 3`

We want to get: `[5,6,7,1,2,3,4]`

---

### **Step 1: Reverse the ENTIRE array**

```python
self.reverse(nums, 0, n - 1)
```

- Reverse from index `0` to `6` (entire array)
- `[1,2,3,4,5,6,7]` → `[7,6,5,4,3,2,1]`

**Why?** This puts the elements that need to go to the front (5,6,7) near the front, but in wrong order!

---

### **Step 2: Reverse the FIRST k elements**

```python
self.reverse(nums, 0, k - 1)
```

- Reverse from index `0` to `2` (first 3 elements)
- `[7,6,5,4,3,2,1]` → `[5,6,7,4,3,2,1]`

**Why?** This fixes the order of the first k elements! Now `5,6,7` are in correct positions!

---

### **Step 3: Reverse the REMAINING elements**

```python
self.reverse(nums, k, n - 1)
```

- Reverse from index `3` to `6` (last 4 elements)
- `[5,6,7,4,3,2,1]` → `[5,6,7,1,2,3,4]`

**Why?** This fixes the order of the rest of the array!

---

## Visual Summary

```
Original:           [1, 2, 3, 4, 5, 6, 7]

Step 1 (Reverse all):      [7, 6, 5, 4, 3, 2, 1]
                            └─────┘ └─────────┘
                            mess!    mess!

Step 2 (Reverse first k):  [5, 6, 7, 4, 3, 2, 1]
                            └─────┘ 
                            Fixed!   still mess

Step 3 (Reverse rest):     [5, 6, 7, 1, 2, 3, 4]
                            └─────┘ └─────────┘
                            Perfect! Perfect!
```

---

## Why Is This Fast?

- **Your old code:** O(n × k) - shifts array k times
- **This code:** O(n) - only 3 passes through array

Each reverse operation goes through part of the array once, so:
- Step 1: Goes through n elements
- Step 2: Goes through k elements  
- Step 3: Goes through (n-k) elements
- **Total: n + k + (n-k) = 2n operations** = O(n) ✅

---

## Another Example

`nums = [1,2,3,4,5], k = 2`

**Step 1:** Reverse all → `[5,4,3,2,1]`  
**Step 2:** Reverse first 2 → `[4,5,3,2,1]`  
**Step 3:** Reverse last 3 → `[4,5,1,2,3]` ✅

Expected: Last 2 elements (4,5) moved to front! ✅

---

"""
        
