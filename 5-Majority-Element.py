class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        for i in nums:
            if count == 0:
                candidate = i 
                count += 1
            elif candidate == i :
                count += 1 
            else: 
                count -= 1
        return candidate


"""

### 🧩 The Code You’re Using

```python
def majorityElement(nums):
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    return candidate
```

This is **Boyer–Moore Majority Vote Algorithm**.

---

### 💡 Key Idea

This algorithm only works **if** the problem guarantees that a **majority element exists** (i.e. one number appears more than `n/2` times).

If such a guarantee is not true → it may **still return a candidate**, but that candidate is **not necessarily the true majority**.

---

### 🧠 Let’s See What Happens in Your Cases

---

#### 🔹 Case 1: `nums = [2,2,2,2,1,1,1,1]`

| Step | num | candidate | count | explanation |
| ---- | --- | --------- | ----- | ----------- |
| 1    | 2   | 2         | 1     | start       |
| 2    | 2   | 2         | 2     | same number |
| 3    | 2   | 2         | 3     | same        |
| 4    | 2   | 2         | 4     | same        |
| 5    | 1   | 2         | 3     | different   |
| 6    | 1   | 2         | 2     | different   |
| 7    | 1   | 2         | 1     | different   |
| 8    | 1   | 2         | 0     | different   |

✅ Final **candidate = 2**
(but count = 0 means it’s evenly matched overall)

---

#### 🔹 Case 2: `nums = [1,1,1,1,2,2,2,2]`

| Step | num | candidate | count | explanation |
| ---- | --- | --------- | ----- | ----------- |
| 1    | 1   | 1         | 1     | start       |
| 2    | 1   | 1         | 2     | same        |
| 3    | 1   | 1         | 3     | same        |
| 4    | 1   | 1         | 4     | same        |
| 5    | 2   | 1         | 3     | different   |
| 6    | 2   | 1         | 2     | different   |
| 7    | 2   | 1         | 1     | different   |
| 8    | 2   | 1         | 0     | different   |

✅ Final **candidate = 1**

---

### ⚠️ Why Different Results?

Because:

* Boyer–Moore is **order-dependent**.
* It **cancels out pairs of different elements** as it scans.
* Whichever appears first and dominates initially will remain as the final candidate **if counts tie perfectly**.

So:

* `[2,2,2,2,1,1,1,1]` → starts with 2 → returns **2**
* `[1,1,1,1,2,2,2,2]` → starts with 1 → returns **1**

But in both arrays, **no number is actually a true majority (more than n/2 times)**.

---

### ✅ Correct Way (if majority is not guaranteed)

If the majority element might not exist, you must **verify** at the end:

```python
def majorityElement(nums):
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    # verify
    if nums.count(candidate) > len(nums)//2:
        return candidate
    else:
        return None  # No majority element
```

---

### 🔍 Output for Your Lists

```python
nums1 = [2,2,2,2,1,1,1,1]  # → None
nums2 = [1,1,1,1,2,2,2,2]  # → None
```

✅ **No majority element exists in either.**

---

"""


