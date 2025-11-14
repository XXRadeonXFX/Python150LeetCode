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
