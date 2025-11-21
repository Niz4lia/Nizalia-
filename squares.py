osq=[]
for x in range(1,21):
    if x%2==1:
        osq.append(x**2)
print("Odd Squares: ",osq)
s=sum(osq)
print('Sum of all odd squares is:',s)

esq=[]
for x in range(1,21):
    if x%2==0:
        esq.append(x**2)
print("Even Squares: ",esq)
e=sum(esq)
print('Sum of all even squares is:',e)
