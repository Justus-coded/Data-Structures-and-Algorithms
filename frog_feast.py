x = [1,4,5]
s=[2,3,5]
y = [2,3,5]



def frog(x,s,y):
    
    out = []
    new = dict(zip(x,s))
    for i,s in new.items():
        count = 0
        for j in y:
            #print(i,j,s)
            if abs(i-j) <= s:
                count+=1
            else:
                pass
            
        out.append(count)    
    return out


# x=[3]
# s=[5]
# y=[7,1,2,6,4,5,3,0,8]
print(frog(x,s,y))