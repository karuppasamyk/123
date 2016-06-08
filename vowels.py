vowels= raw_input()[::-1]
print(vowels)
vowel= ['a' , 'e' , 'i' , 'o' , 'u']
rev = []
for i in vowels:
    if i not in vowel:
        rev.append(i)
print ''.join(rev)
