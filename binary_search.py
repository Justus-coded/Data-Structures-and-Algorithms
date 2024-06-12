array = [0,1,21,33,45,45,61,71,72,73]
target=33

def bin(arr,tar):
    l=0
    r= len(arr)-1

    while l<=r:
        m = l+r//2
        #mat = arr[m]

        if tar==arr[m] :
            return m
        elif tar < arr[m]:
            r=m-1
        else:
            l =m+1

print(bin(array,target))
