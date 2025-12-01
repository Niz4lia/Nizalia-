
movies = [
    {"title": "Inception", "genre": "sci-fi", "year": 2010},
    {"title": "Titanic", "genre": "romance", "year": 1997},
    {"title": "The Dark Knight", "genre": "action", "year": 2008},
    {"title": "Interstellar", "genre": "sci-fi", "year": 2014},
    {"title": "La La Land", "genre": "musical", "year": 2016},
    {"title": "Gladiator", "genre": "action", "year": 2000},
]

def recommend_by_genre(genre):
    results = [m for m in movies if m["genre"] == genre.lower()]
    if not results:
        print("No movies found for that genre.")
    else:
        for m in results:
            print(f"- {m['title']} ({m['year']})")

def search_movie(name):
    results = [m for m in movies if name.lower() in m["title"].lower()]
    if not results:
        print("No match found.")
    else:
        for m in results:
            print(f"- {m['title']} ({m['genre']}, {m['year']})")

def random_movie():
    import random
    m = random.choice(movies)
    print(f"🎥 Watch: {m['title']} ({m['genre']}, {m['year']})")

while True:
    print("\n🎬 MOVIE RECOMMENDER")
    print("1. Recommend by genre")
    print("2. Search movie")
    print("3. Random pick")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        recommend_by_genre(input("Enter genre: "))
    elif choice == "2":
        search_movie(input("Enter movie name: "))
    elif choice == "3":
        random_movie()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")