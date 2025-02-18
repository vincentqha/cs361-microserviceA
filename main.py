import requests
from pprint import pprint

API_URL = "https://quoteapi.pythonanywhere.com/quotes/"

response = requests.get(API_URL)

if response.status_code != 200:
    print("Error: Unable to retrieve movie quotes")

quotes_data = response.json()

movies = []
saved_movies = []
quotes = quotes_data["Quotes"][0]
genre_count = {}

for num in range(len(quotes_data["Quotes"][0])):
    movies.append(quotes[num]["movie_title"])

while True:

    print(f"\nTo query a movie quote, please enter a movie title.\n")

    user_input = input("Please enter a movie title: ")

    if user_input in movies:
        movie_index = movies.index(user_input)
        saved_movies.append({movies[movie_index]:quotes[movie_index]["quote"]})

        if quotes[movie_index]["category"] not in genre_count:
            genre_count[quotes[movie_index]["category"]] = 1
        else:
            genre_count[quotes[movie_index]["category"]] += 1

        print(f"The quote from {movies[movie_index]} is: \n\"{quotes[movie_index]["quote"]}\"")

        print(saved_movies)
        print(genre_count)
    else:
        print("The movie you entered does not exist in our database. Please enter a different movie title.")
