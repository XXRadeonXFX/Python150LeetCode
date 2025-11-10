class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last = len(nums) - 1
        k = k % last
        count = 0 
        while count < k :
            last_elem = nums[last]
            i = last
            while i > 0 :
                nums[i] = nums[i-1] 
                i -= 1
            nums[0] = last_elem
            count += 1

""" 

## Setup Part

```python
n = len(nums)
```
- `n` stores the length of the array
- Example: if `nums = [1,2,3,4,5,6,7]`, then `n = 7`

```python
k = k % n
```
- This handles cases when `k` is bigger than array length
- Example: If `k = 10` and `n = 7`, rotating 10 times is same as rotating 3 times
- `10 % 7 = 3`, so `k = 3`
- **Why?** Because after every 7 rotations, array comes back to original position!

```python
count = 0
```
- This tracks how many rotations we've done
- We need to do `k` rotations total

---

## Main Loop (Outer While)

```python
while count < k:
```
- This loop runs `k` times
- Each time through this loop = 1 rotation

---

## Inside Each Rotation

### Step 1: Save the Last Element
```python
last_element = nums[n - 1]
```
- `n - 1` is the last index (because array starts at 0)
- Save this element because we'll overwrite it soon

**Example:** `nums = [1,2,3,4,5,6,7]`
- `last_element = 7`

---

### Step 2: Shift Everything to the Right

```python
i = n - 1
while i > 0:
    nums[i] = nums[i - 1]
    i = i - 1
```

Let me show you this step by step:

**Start:** `nums = [1,2,3,4,5,6,7]`, `i = 6`

- **i = 6**: `nums[6] = nums[5]` → `[1,2,3,4,5,6,6]` (7 is gone, 6 copied)
- **i = 5**: `nums[5] = nums[4]` → `[1,2,3,4,5,5,6]`
- **i = 4**: `nums[4] = nums[3]` → `[1,2,3,4,4,5,6]`
- **i = 3**: `nums[3] = nums[2]` → `[1,2,3,3,4,5,6]`
- **i = 2**: `nums[2] = nums[1]` → `[1,2,2,3,4,5,6]`
- **i = 1**: `nums[1] = nums[0]` → `[1,1,2,3,4,5,6]`
- **i = 0**: Loop stops (because `i > 0` is false)

Now array is: `[1,1,2,3,4,5,6]`

---

### Step 3: Put Last Element at Front

```python
nums[0] = last_element
```
- Remember we saved `last_element = 7`
- Now put it at the beginning

**Result:** `[7,1,2,3,4,5,6]` ✅ One rotation complete!

---

### Step 4: Increase Counter

```python
count = count + 1
```
- We finished 1 rotation, so increase counter
- Loop continues until `count = k`

---

## Complete Example

**Input:** `nums = [1,2,3,4,5,6,7], k = 3`

**Rotation 1 (count = 0):**
- Save: `last_element = 7`
- Shift: `[1,1,2,3,4,5,6]`
- Place: `[7,1,2,3,4,5,6]`

**Rotation 2 (count = 1):**
- Save: `last_element = 6`
- Shift: `[7,7,1,2,3,4,5]`
- Place: `[6,7,1,2,3,4,5]`

**Rotation 3 (count = 2):**
- Save: `last_element = 5`
- Shift: `[6,6,7,1,2,3,4]`
- Place: `[5,6,7,1,2,3,4]`

**Final Answer:** `[5,6,7,1,2,3,4]` ✅

---

## Visual Summary

Think of it like a circular conveyor belt:
- Pick up the last item
- Move everyone one step to the right
- Put the last item at the front
- Repeat k times

"""
        
