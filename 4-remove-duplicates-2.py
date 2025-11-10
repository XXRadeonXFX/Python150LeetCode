class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        k=2 
        for i in range( 2, len(nums) ):
            if nums[i] != nums[k-2]:
                nums[k] = nums[i]
                k+=1
        return k 



"""
## ✅ CORRECT Walkthrough

```
nums = [1, 1, 1, 2, 2, 3]
```

**i = 2: Looking at `1`**
```
[1, 1, 1, 2, 2, 3]
 ^     ^
k-2    i
k=2
```
- Compare: `nums[2]=1` vs `nums[k-2]=nums[0]=1`
- SAME → Skip, **k stays at 2**

**i = 3: Looking at `2`**
```
[1, 1, 1, 2, 2, 3]
 ^        ^
k-2       i
k=2 (still!)
```
- Compare: `nums[3]=2` vs `nums[k-2]=nums[0]=1`
- DIFFERENT → Add it!
- `nums[2] = 2` → `[1, 1, 2, 2, 2, 3]`
- **Now k = 3** (incremented)

**i = 4: Looking at `2`**
```
[1, 1, 2, 2, 2, 3]
    ^        ^
   k-2       i
k=3
```
- Compare: `nums[4]=2` vs `nums[k-2]=nums[1]=1`
- DIFFERENT → Add it!
- `nums[3] = 2` → `[1, 1, 2, 2, 2, 3]`
- **Now k = 4**

**i = 5: Looking at `3`**
```
[1, 1, 2, 2, 2, 3]
       ^        ^
      k-2       i
k=4
```
- Compare: `nums[5]=3` vs `nums[k-2]=nums[2]=2`
- DIFFERENT → Add it!
- `nums[4] = 3` → `[1, 1, 2, 2, 3, 3]`
- **Now k = 5**

---
"""
