import requests
from pprint import pprint

API_URL = "https://quoteapi.pythonanywhere.com/quotes/"

response = requests.get(API_URL)

if response.status_code != 200:
    print("Error: Unable to retrieve movie quotes")

quotes_data = response.json()

# quotes_data["Quotes"][0][object_num][property]
# print(len(quotes_data["Quotes"][0]))
# print(quotes_data["Quotes"][0][81])

movies = []
quotes = quotes_data["Quotes"][0]

for num in range(len(quotes_data["Quotes"][0])):
    movies.append(quotes[num]["movie_title"])

print(f"\nTo query a movie quote, please enter a movie title.\n")

user_input = input("Please enter a movie title: ")

if user_input in movies:
    movie_index = movies.index(user_input)
    print(f"The quote from {movies[movie_index]} is: \"{quotes[movie_index]["quote"]}\"")
else:
    print("The movie you entered does not exist in our database. Please enter a different movie title.")
