import requests
from pprint import pprint

API_URL = "https://quoteapi.pythonanywhere.com/quotes/"

print(f"\nTo query a movie quote, please enter a movie title.\n")

# user_input = input("Please enter a movie title: ")

response = requests.get(API_URL)

if response.status_code != 200:
    print("Error: Unable to retrieve movie quotes")

quotes_data = response.json()
pprint(quotes_data["Quotes"][0][0]["movie_title"])

# quotes_data["Quotes"][0][object_num][property]
# print(len(quotes_data["Quotes"][0]))
# print(quotes_data["Quotes"][0][81])

movies = []

for num in range(len(quotes_data["Quotes"][0])):
    movies.append(quotes_data["Quotes"][0][num]["movie_title"])

