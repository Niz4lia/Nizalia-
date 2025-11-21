import re
s="Iqra.University"
#before using \
match=re.search(r'.',s)
print(match)
#after using\
mat=re.search(r'\.',s)

print(mat)
#[]
string="The quick brown fox jumped over the fence."
pattern="[a-m]"
result=re.findall(pattern, string)
print(result)

#r first letters
regex = r'^The'
strings = ('The quick brown fox', 'The lazy dog', 'A quick brown fox')
for string in strings:
    if re.match(regex, string):
        print(f'Matched: {string}')
    else:
        print(f'Not matched: {string}')

#$ last letters
word='Hello world'
pattern=r"ld$"
match=re.search(pattern,word)
if match:
    print("Match found!")
else:
    print("Match not found")

#.
stri="The quick brown fox jumped over the fence."
patterm=r'brown.fox'
mat=re.search(patterm,stri)
if mat:
    print("Match found!")
else:
    print("Match not found")

#|
pat=r'a|b'
sti=['acd','bcd','acb','xyz']
mats=[s for s in sti if re.search(pat,s)]
print(mats)

#?
pa=r'ab?c'
sti=['ac','acb','abbc','xyzc']

ma=[s for s in sti if re.search(pa,s)]
print(ma)

#*
p=r'ab*c'
st=['ac','acb','abbc','xyzc']

ma=[s for s in st if re.search(p,s)]
print(ma)

import re
#{,}
se = r'a{2,4}'   
li = ['aac', 'abbc']
matches = [s for s in li if re.search(se, s)]
print(matches)

#r'(a|b)cd'
import re
patn = r'(a|b)cd'
strigs = ['acd', 'bcd', 'ccd', 'abcd', 'cd']
mch = [s for s in strigs if re.search(patn, s)]
print(mch)

#with digits
l=r'\d'
p=['abc','a12','123']
mc = [s for s in p if re.search(l, s)]
print(mc)

#Non Digits
l=r'\D'
p=['abc','a12','123']
mc = [s for s in p if re.search(l, s)]
print(mc)

#with spaces
l=r'\s'
p=['Hello world','a12','nice\n']
mc = [s for s in p if re.search(l, s)]
print(mc)

#without spaces
l=r'\S'
p=['Hello world','a12','nice\n']
mc = [s for s in p if re.search(l, s)]
print(mc)