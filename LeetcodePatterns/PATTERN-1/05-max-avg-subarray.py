# numbers = [1,2,3,4,5]
# k = 3

# numbers = [1, 12, -5, -6, 50, 3]
# k = 4

# numbers = [-5, -2, -8, -1]
# k = 2

# numbers = []
# k = 0

numbers= [1,2,3]
k=10


def max_avg_subarray(numbers,k):
    if k==0 or len(numbers) ==0 or k > len(numbers) :
        return None
    i = 0 
    j = k  
    mx = sum(numbers[i:j]) / k
    while j <= len(numbers):
        if mx < sum(numbers[i:j]) /k :
            mx= sum(numbers[i:j]) / k
            
        j += 1 
        i +=1

    return mx    

max_avg_subarray(numbers,k)
