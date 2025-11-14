def find_two_sum(numbers,target):
    i=0
    j=len(numbers) -1
    while i < j:
        if numbers[i] + numbers[j] > target:
            j -= 1        
        elif numbers[i] + numbers[j] < target:
            i += 1
        elif numbers[i] + numbers[j] == target:
            return [i + 1 ,j + 1]

# numbers =[2, 3, 4, 7, 11]
# target = 9

# numbers = [1,2,3,4,5]
# target = 100

numbers = [2,3,5]
target = 10

find_two_sum(numbers,target) 






----------------------< LOGIC >---------------------------
"""
Visual Example:
Array: [2, 3, 4, 7, 11]
Target: 9

Initial:
[2, 3, 4, 7, 11]
 ↑           ↑
left       right

Check: 2 + 11 = 13
Is 13 == 9? NO
Is 13 > 9? YES (too big!)
Action: Move right LEFT (make sum smaller)

Step 2:
[2, 3, 4, 7, 11]
 ↑        ↑
left    right

Check: 2 + 7 = 9
Is 9 == 9? YES! ✅
Found it! Return indices [0, 3]

Why This Works:
Key Insight: Array is SORTED!

Left pointer starts at smallest number
Right pointer starts at largest number

Logic:

If sum < target → Need bigger sum → Move left RIGHT ➡️
If sum > target → Need smaller sum → Move right LEFT ⬅️
If sum == target → Found it! 🎉


Complete Walkthrough:
Array: [1, 2, 3, 4, 5, 6]
Target: 10

Round 1:
[1, 2, 3, 4, 5, 6]
 ↑              ↑
 L              R

Sum: 1 + 6 = 7
7 < 10? YES (too small!)
Move L right →

Round 2:
[1, 2, 3, 4, 5, 6]
    ↑           ↑
    L           R

Sum: 2 + 6 = 8
8 < 10? YES (too small!)
Move L right →

Round 3:
[1, 2, 3, 4, 5, 6]
       ↑        ↑
       L        R

Sum: 3 + 6 = 9
9 < 10? YES (too small!)
Move L right →

Round 4:
[1, 2, 3, 4, 5, 6]
          ↑     ↑
          L     R

Sum: 4 + 6 = 10
10 == 10? YES! ✅
Found it! Return [3, 5] (0-indexed)
"""
