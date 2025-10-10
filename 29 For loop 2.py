dates=(1982, 1899, 1973, 2000)

i=0
year=dates[0]
while (year!=1973):
    print(year)
    i=i+1
    year=dates[i]
print("It took",i,"repetitions to get out of the loop")