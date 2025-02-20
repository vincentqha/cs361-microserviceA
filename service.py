import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

API_URL = "https://quoteapi.pythonanywhere.com/quotes/"

response = requests.get(API_URL)

if response.status_code != 200:
    print("Error: Unable to retrieve movie quotes")

data = response.json()

movies = []
saved_movies = []
quotes = data["Quotes"][0]
genre_count = {}

for num in range(len(quotes)):
    movies.append(quotes[num]["movie_title"])


@app.route('/get_movie_quote', methods=['GET'])
def query_movie_quotes():

    user_input = request.args.get('input')

    if user_input in movies:
        movie_index = movies.index(user_input)
        movie_data = quotes[movie_index]

        saved_movies.append({movies[movie_index]: movie_data["quote"]})

        if quotes[movie_index]["category"] not in genre_count:
            genre_count[movie_data["category"]] = 1
        else:
            genre_count[movie_data["category"]] += 1

        print(f"\nResponding with data...")
        return jsonify(movie_data)

    elif user_input == "history":

        print(f"\nResponding with data...")
        return jsonify(saved_movies)

    elif user_input == "stats":

        print(f"\nResponding with data...")
        return jsonify(genre_count)

    else:
        return jsonify({"Error": "Movie does not exist in database"}), 404


if __name__ == '__main__':
    print("Movie Quotes Service")
    print("========================")
    print("Running on http://localhost:5000")
    app.run(port=5000)

