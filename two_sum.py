array = [3,5,-4,8,11,-1,1,6]
targetSum = 10

def twoSum(array,targetSum):
    for i in range(len(array)):
        x = targetSum-array[i]
        if x in array and x!=array[i]:
            return array[i],x
            
    
    return []

# def twoSum(array,targetSum):
#     for num in array:
#         x = targetSum - num
#         if x in array and x!=num:
#             return [num,x]
            
    
#     return []


num = twoSum(array, targetSum)
print(num)