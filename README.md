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
```
The return data from this function can be stored in a variable where you can access key-values like quote, movie_title, 
and category. 