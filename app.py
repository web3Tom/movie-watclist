import datetime

from database import (create_tables, add_movie, add_user, get_movies, get_watched_movies,
                      watch_movie)

menu = """Please select one of the following options:
1) Add new movie.
2) View upcoming movies.
3) View all movies.
4) Watch a movie.
5) View watched movies.
6) Add user to the app.
7) Exit.

Your selection: """
welcome = "Welcome to the watchlist app!"

print(welcome)
create_tables()

# helper functions
def prompt_add_movie():
        title = input("Movie title: ")
        release_date = input("Release date (dd-mm-YYYY): ")
        parsed_date = datetime.datetime.strptime(release_date, "%d-%m-%Y")
        timestamp = parsed_date.timestamp()
        
        add_movie(title, timestamp)

def print_movie_list(heading, movies):
        print(f"-- {heading} movies --")
        for _id, title, release_date in movies:
                movie_date = datetime.datetime.fromtimestamp(release_date)
                human_date = movie_date.strftime("%d %b %Y")
                print(f"{_id}: {title} (on {human_date})")
        print("---- \n")

def print_watched_movies(username, movies):
        print(f"-- Movies Watched by {username} --")
        for movie in movies:
                print(f"{movie[1]}")
        print("--- \n")
        

def prompt_watch_movie():
        username = input("Enter your name: ")
        movie_id = input("Movie ID: ")
        watch_movie(username, movie_id)

def prompt_add_user():
        username = input("Enter your username: ")
        add_user(username)


# main function
while (user_input := input(menu)) != "7":
        if user_input == "1":
                prompt_add_movie()
        elif user_input == "2":
                movies = get_movies(True)
                print_movie_list("Upcoming", movies)
        elif user_input == "3":
                movies = get_movies()
                print_movie_list("All", movies)
        elif user_input == "4":
                prompt_watch_movie()
        elif user_input == "5":
                username = input("Username: ")
                watched_movies = get_watched_movies(username)
                print_watched_movies(username, watched_movies)
        elif user_input == "6":
                prompt_add_user()
        else:
                print("Invalid input, please try again!")

