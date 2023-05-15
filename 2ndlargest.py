def secondlargest(arr):
    arr.sort()
    return arr[-2]
    
arr = [1,2,4,8,56,99,35]
print("the second largest number is ", secondlargest(arr) )