import re
text='This a random text'
match=re.search(r'random',text)
print(match)
print('matched text: ',match.group())
print("start index",match.start())
print("end index",match.end())

pattern=r'a'
mat=re.search(pattern,"This is a school")
print(mat)
if mat:
    print("matched text: ",mat.group())