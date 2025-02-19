from pprint import pprint
import requests


def get_movie_info(u_input):
    url = 'http://127.0.0.1:5000/get_movie_quote'
    params = {'input': u_input}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return response.json()


if __name__ == '__main__':

    while True:
        user_input = input("Please enter movie title: ")
        movie_info = get_movie_info(user_input)

        print(f"\nThe JSON received from service.py: ")
        pprint(movie_info)
        print()

        if user_input == "quit":
            print(f"\nQuitting...")

            break
