def caesarCipherEncryptor(string, key):
    # Write your code here.
    char = 'abcdefghijklmnopqrstuvwxyz'
    # string ='xyz'
    # key=2
    new_letter= []
    newKey = key%26
    alphabet = list(char)
    for letter in string:
        new_letter.append(getNewLetter(letter,newKey,alphabet))
    return "".join(new_letter)

def getNewLetter(letter,key,alphabet):
    newLetterCode = alphabet.index(letter)+key
    return alphabet[newLetterCode%26]

# for letter in string:
#     #print(letter)
#     code=alphabet.index(letter)+key
#     print(code)



string ='xyz'
key=2
print(caesarCipherEncryptor(string,key))












# print(len(char))
# dic = {}
# for i in range(len(char)):
#     #print(char[i],i+1)
#     dic[char[i]]=i+1

#     digit = string[-1]
    
#     new_key =dic[digit]+key
#     if new_key>26:
#         mod =new_key%26
#         list(range(1,mod+1))
#     else:



# print(dic[digit]+key)
# print (dic[digit])

#print(dic)

