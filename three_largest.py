array = [10,5,9,10,12]

def three_largest_num(arr):
    # j=1
    # for i in range(len(arr)):
    #     if arr[i]>=arr[j]:
    #         arr[i] = arr[j]

    #         j+=1
    #     else:
    #         pass
    # return arr[-1]
    output = [float('-inf')]*4
    print(output)
    for num in array:
        output[0] = num
        print(output)
        output.sort()
    return output[-3:]

    # result =[float('-inf')]*3
    # for i in range(len(arr)):
    #     if arr[i]>result[2]:
    #         result[0]=result[1]
    #         result[1]=result[2]

    #         result[2]=arr[i]
            
    #     elif arr[i]>result[1]:
    #         result[0] = result[1]
    #         result[1]=arr[i]

    #     elif arr[i]>result[0]:
    #         result[0]=arr[i]
    
    # return result

print(three_largest_num(array))
