def duplicate(nums):
    i = 0
    dup = set()
    while i < len(nums):
        if nums[i] in dup:
            return True
        else:
            dup.add(nums[i])
        i += 1
    return False

# Test cases
test_cases = [
    ([1, 2, 3, 1], True, "Has duplicate"),
    ([1, 2, 3, 4], False, "All unique"),
    ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True, "Many duplicates"),
    ([1], False, "Single element"),
    ([], False, "Empty array"),
]

for nums, expected, description in test_cases:
    result = duplicate(nums)
    status = "✅" if result == expected else "❌"
    print(f"{status} {description}")
    print(f"   Input: {nums}")
    print(f"   Got: {result}, Expected: {expected}\n")
