
wor= str(input("Enter a word: "))
vowels = "a,e,i,o,u,A,E,I,O,U"
quan = 0

for letter in wor:
    if letter in vowels:
        quan += 1
        print(letter)

print("Number of vowels:", quan)