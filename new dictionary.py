release = {
    'Thriller': 1982,
    'Back in Black': 1980,
    'The Dark Side of the Moon': 1973,
    'The Bodyguard': 1992,
    'Bat Out of Hell': 1977,
    'Their Greatest': 1976,
    'Saturday Night': 1977,
    'Rumours': 1977,
}
print(release,"\n")

#Accessing dictionary
print(release['Thriller'],"\n") 

#Getting keys and values
print(release.keys(),"\n")
print(release.values(),"\n")

#appending dictionaries
release['Hotel California']= 1976
print(release,"\n")

#Removing items from dictionary
del(release['Thriller'])

if 'Thriller' in release:
    print('Found')