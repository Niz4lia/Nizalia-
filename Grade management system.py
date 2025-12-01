
stdgrade = [85, 90, 78, 92, 88, 76, 95, 89]
stdgrade.append(80)
stdgrade.sort()
stdgrade.remove(76) 
print(f'Highest grade is: {max(stdgrade)}')
cou = sum(n > 85 for n in stdgrade)
print(f'The no. of grades higher than 85 are: {cou}')
print(f'The final grades are: {stdgrade}')

