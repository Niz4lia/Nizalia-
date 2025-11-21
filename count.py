import time
tim = int(input("Enter time in seconds: "))
for i in range(tim, 0, -1):
    print(i)
    time.sleep(1)
print("Time's up!")