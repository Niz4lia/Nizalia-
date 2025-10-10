tem=int(input("Enter the Temperature : "))
un=str(input('Enter the unit of temperature (c, k, f): '))

if un=='c':
    ke=tem+273
    print('In Kelvin',ke)
    fa=tem*9/5+32
    print("In Farenheit: ",fa)

elif un=='k':
    fa=1.8*(tem-273)+32
    print('In Farenheit:',fa)
    ce=tem-273
    print('In celsius: ',ce)

elif un=='f':
     ce=(tem-32)*5/9
     print('In celsius: ',ce)
     ke=tem-32/1.8+273
     print('In Kelvin',ke)

else:
    print('Error in Unit')