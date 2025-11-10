class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[k-1]:
                nums[k]=nums[i]
                k += 1                
        return k


################################################################################
"""
Let me explain it in the **simplest way possible**!

## Think of it like organizing books on a shelf

Imagine you have duplicate books and want to keep only one copy of each:

**Your rule:** "If this book is different from the last unique book I kept, add it to my 'keep' pile"

## The Two Pointers

```
k     = "Where should I put the NEXT unique book?"
k-1   = "What was the LAST unique book I kept?"
i     = "Which book am I looking at RIGHT NOW?"
```

## Step-by-Step Example

```
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
```

**Start:**
```
[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
 ^
k=1 (next spot to fill)
```
- Last unique book: `0` (at position 0)

**i=1: Looking at `0`**
```
[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
 ^  ^
 |  i
k-1 (last unique)
```
- Question: "Is `0` different from my last unique `0`?"
- Answer: NO! Skip it.

**i=2: Looking at `1`**
```
[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
 ^     ^
 |     i
k-1
```
- Question: "Is `1` different from my last unique `0`?"
- Answer: YES! 
- Action: Put `1` in position `k` (position 1)
- Result: `[0, 1, 1, 1, 1, 2, 2, 3, 3, 4]`
- Now k=2, so next unique goes to position 2

**i=3,4: Looking at `1`, `1`**
- Both are same as our last unique (`1`), so skip them

**i=5: Looking at `2`**
```
[0, 1, 1, 1, 1, 2, 2, 3, 3, 4]
    ^           ^
    |           i
   k-1
```
- Question: "Is `2` different from my last unique `1`?"
- Answer: YES!
- Action: Put `2` in position 2
- Result: `[0, 1, 2, 1, 1, 2, 2, 3, 3, 4]`

## Final Result
```
[0, 1, 2, 3, 4, _, _, _, _, _]
 └─────k=5────┘
 These are the unique ones!
```
"""
################################################################################
