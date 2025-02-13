import requests
from pprint import pprint

API_URL = "https://quoteapi.pythonanywhere.com/quotes/"

print(f"\nTo query a movie quote, please enter a movie title.\n")

# user_input = input("Please enter a movie title: ")

response = requests.get(API_URL)

if response.status_code != 200:
    print("Error: Unable to retrieve movie quotes")

quotes_data = response.json()
pprint(quotes_data)

