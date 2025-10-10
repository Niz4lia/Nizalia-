import re
s1="the frozen is the best album"
pattern=r'z' 
result= re.search(pattern, s1)

if result:
    print("Match Found")
else:
    print("Match not found")