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


'''
🔄 ROUND 1: I moves to position 1
[1, 1, 2, 2, 3]
 ↑  ↑
 J  I
I: "Hey J! I found toy 1 at position 1"
J: "I already have toy 1 at my position (position 0)"
I: "Is 1 different from 1? NO!"
J: "Then I don't need it! Stay where you are, J!"
I: "Okay, I'll just move to the next toy"
Action: Only I moves → I goes to position 2

🔄 ROUND 2: I moves to position 2
[1, 1, 2, 2, 3]
 ↑     ↑
 J     I
I: "Hey J! I found toy 2 at position 2"
J: "I have toy 1 at my position (position 0)"
I: "Is 2 different from 1? YES!"
J: "That's NEW! I need to save it!"
'''
