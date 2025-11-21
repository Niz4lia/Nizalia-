movie = []
n = int(input("Enter number of movies you want to add: "))
for i in range(n):
    movie.append(input(f"Enter {i+ 1} movie title: ").strip())
print("Movies added:", movie)

def remove_movie():
    remove = input("Enter movie title to remove: ").strip()
    movie.remove(remove)
    print("Updated movie list:", movie)

def add_movie():
    add = input("Enter movie title to add: ").strip()
    movie.append(add)
    print("Updated movie list:", movie)

choice = input ("(Add, Remove, exit): ")
if choice == "remove":
    remove_movie()
elif choice== "add":
    add_movie()

count= {}
for s in movie:
    if s:
        alphabate = s[0::] 
        if alphabate  in count:
            count[alphabate] += 1
        else:
            count[alphabate] = 1
                      
print("Alphabet count:")
for alphabate  in count:
    print(f"{alphabate}: {count[alphabate]}")