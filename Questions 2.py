#List and Tuples
lst=[1,4,6,8,8,0,92,46,78,99,999,1000]
print(max(lst))
print(min(lst))

nlst=list(set(lst))
print(nlst)
#question3
for n in nlst:
    cou=lst.count(n)
    print(f'no. of {n} = {cou}')

#question5
tu=(3,4,5,6,7,8)
tu2=(0,9,8,10)
concat=tu+tu2
print(concat)

#Dictionaries
st={'Nizalia':25,'Shally':24,'Ayliya':23,'Hijab':18,'Anoosh':22}
total= sum(st.values())
ave=total/len(st)
print(f'Average  = {ave}')

#question2
st['Fatima']=21
print(st)
st.pop("Fatima")
print(st)

#question3
if 'Nizalia' in st:
    print("Nizalia is present in the dictionary")
else:
    print("Nizalia is not present in the dictionary")

#question4
st2={'English':90,'Math':95,'Science':85}
st3={**st, **st2}
print(st3)
#question5

string="Hi, its me!Nizalia."
freq={}
for char in string:
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1
print(freq)