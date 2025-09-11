import os 
import json


FILENAME = "movies.json"

def load_movies():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r", encoding="utf-8") as f :
        return josn.load(f)
    
def save_movies(movies):
    with open(FILENAME, "w", encoding="utf-8") as f :
        json.dump(movies, f, indent = 2)
        
def add_movies(movies):
    title = input("enter the movie name: ").strip().lower()
    
    if any(movie["title"] for movie in movies):
        print("Movies alreday exists")
        return
    genre = input ("Genre: ").strip().lower()
    try:
        rating = float(input("enter rating(0-10): "))
        if not (0 <= rating <= 10):
            raise ValueError
    except ValueError:
        print("Please enter valid number")
        return
    movies.append({"title": title,"genre": genre, "rating": rating})
    save_movies(movies)
    print("Movies added *")
    
def view_movie(movies):
    if not movies:
        print("No movies in db")
        return 
    for movie in movies:
        print(f"{movies["title"]} --- {movies["genre"]} -- {movie["rating"]}")
    print("-"*30)
    
def search_movies(movies):
    term = input("Enter the title or gegre: ").strip().lower()
    
    results = [
        movies for movie in movies
        if term in movie['title'].lower() or term in movie
        ['genre'].lower
     ]
    if not results:
        print("No matching movies")
        return
    print(f"Found {len(results)} result(s)")
    
    for movie in results:
        print(f"{movies["title"]} --- {movies["genre"]} -- {movie["rating"]}")
        
def run_movie_db():
    movies = load_movies()
    
    while True:
        print("\n MyMovieDB")
        print("1. Add movies")
        print("2. View All movies")
        print("3. Search Movie")
        print("4. Exit")
        
        choice = input("chhose an option (1-4): ").strip()
        match choice:
            case "1": add_movies(movies)
            case "2": view_movie(movies)
            case "3": search_movies(movies)
            case "4": break
            case _: print("enter valid choice")
            
if __name__ == "__main__":
    run_movie_db()
            
    
