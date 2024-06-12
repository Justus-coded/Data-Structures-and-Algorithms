array = [5,1,22,25,6,-1,8,10]
sequence = [1,6,-1,10]

def isValidSubsequence(array, sequence):
    # Write your code here.
    j = 0
    for i in range(len(array)):
        if array[i]==sequence[j]:
            j+=1
        if j == len(sequence):
            return True
    return False

# def val_sub(array, subsequence):
#     new = []
#     if len(subsequence)>len(array):
#         return False
#         for num in subsequence:
#             if num in array:
#                 new.append(num)
#         if new==subsequence and len(new)==len(subsequence):
#             return True
#         else:
#             return False


            
num = isValidSubsequence(array, sequence)
print(num)