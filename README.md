# Movie Quotes Microservice

CS 361 Microservice A for teammate that provides movie quotes information via HTTP/JSON communication via Flask. It 
returns relevant data such as movie quote, movie title, actor/character who spoke the quote, and genre. 

## To programmatically REQUEST data from Microservice A
To programmatically REQUEST data from Microservice A, include this function in your Python file:

```python
import requests

def get_movie_info(u_input):
    url = 'http://127.0.0.1:5000/get_movie_quote'
    params = {'input': u_input}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return response.json()

movie = "Batman Begins"
get_movie_info(movie)
```
When the `get_movie_info(u_input)` function is called, it requests movie data from Microservice A using the input 
provided `(u_input)`.

## To programmatically RECEIVE data from Microservice A
To programmatically RECEIVE data from Microservice A, store `get_movie_info(u_input)` into a variable to access the 
contents of the JSON that is returned from the call. 

```python
import requests

def get_movie_info(u_input):
    url = 'http://127.0.0.1:5000/get_movie_quote'
    params = {'input': u_input}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return response.json()

movie = "Batman Begins"
response_data = get_movie_info(movie)
```
Here, ```response_data``` contains the JSON with all the movie details, including the quote. Here's an example of what the response data looks
like:

```json
      {
        "id": 9,
        "quote": "It's not who I am underneath, but what I do that defines me.",
        "movie_title": "Batman Begins",
        "actor_name": "Christian Bale (Bruce Wayne/Batman)",
        "category": "Superhero/Action",
        "publish_date": "2005",
        "source": "Batman Begins",
        "context": "Batman's philosophy on identity and actions.",
        "rating": "Null",
        "language": "English",
        "author": "Christopher Nolan (Director/Screenwriter of the film)",
        "author_bio": "Christopher Nolan is a British-American filmmaker known for his work in the Batman trilogy."
      }
```

## To get the history of all quotes queried so far
In a running session, to get a list of all the quotes that have been queried, pass ```"history"``` as an argument into 
```get_movie_info(u_input)```.

```python
import requests

def get_movie_info(u_input):
    url = 'http://127.0.0.1:5000/get_movie_quote'
    params = {'input': u_input}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return response.json()

quotes_history = get_movie_info("history")
```

The ```quotes_history``` variable contains a list of all the queried movie quotes in JSON format. Here's an example of what the
response data looks like:
```
[
{'Batman Begins': "It's not who I am underneath, but what I do that defines "
                   'me.'},
{'The Karate Kid': 'Wax on, wax off.'}
]
```

## To get the popularity statistics of quotes by genre
In a running session, to see the genre popularity of quotes queried, pass ```"stats"``` as an argument into 
```get_movie_info(u_input)```.

```python
import requests

def get_movie_info(u_input):
    url = 'http://127.0.0.1:5000/get_movie_quote'
    params = {'input': u_input}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return response.json()

quotes_popularity_stats = get_movie_info("stats")
```

The ```quotes_popularity_stats``` variable contains a dictionary of genre count in JSON format. Here's an example of 
what the response data looks like:
```
{'Drama/Action': 1, 'Superhero/Action': 1}
```

## UML Sequence Diagram 