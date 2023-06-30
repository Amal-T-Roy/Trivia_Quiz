# Trivia Quiz

A tkinter based trivia quiz that fetches 10 random questions from opentdb API using the requests module.UI provides two buttons to enter True or False as answers .Gives feedback on the answer entered by user(Background turns green if answer is correct and red  if answer  is  wrong).

## Installation

Clone the repository

```bash
git clone https://github.com/Amal-T-Roy/Trivia_Quiz.git
```

## Usage
Run the main.py module.

```bash
python3 main.py
```



## Requests Module
Python HTTP for Humans.Receives 10 questions from the opentdb API in JSON format.The questions are parsed and HTML entities are unescaped.
```bash
pip install requests
```
### Usage
```python
import requests
>>> r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
>>> r.status_code
200
>>> r.headers['content-type']
'application/json; charset=utf8'
>>> r.encoding
'utf-8'
>>> r.text
'{"authenticated": true, ...'
>>> r.json()
{'authenticated': True, ...}
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[GNU General Public License v3.0
](https://github.com/Amal-T-Roy/Trivia_Quiz/blob/main/LICENSE)
