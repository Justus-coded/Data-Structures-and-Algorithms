string ='aba'

#print(string[::-1])
def palin(string):
    new =''

    for i in reversed(range(len(string))):
        new+=(string[i])
        #if string[i]==string[-i]:
        print(new)
    return string == new
    #return False

print(palin(string))
