n=4
n = 4  

for i in range(1, n+1):
    row = ""
    for j in range(n - i):
        row += " "
    row += "*"

    if i > 1:
        for k in range(2 * (i - 1) - 1):
            row += " "
        row += "*"
    
    print(row)

for i in range(n-1, 0, -1):
    row = ""

    for j in range(n - i):
        row += " "
    
    row += "*"
    
    if i > 1:
        for k in range(2 * (i - 1) - 1):
            row += " "
        row += "*"
    
    print(row)