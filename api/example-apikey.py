import requests
import sys

def linebreak():
    print(f"----------------------------------------")

# VARS
words = 5
paragraphs = 2
format = 'json' # {json, html, text}
url = "https://alexnormand-dino-ipsum.p.rapidapi.com"
with open ("api/apikey", "r") as f:
    apikey = f.read().splitlines()
apikey = apikey[0]

# Get responde passing all required parameters
response = requests.get(f"{url}/?format={format}&words={words}&paragraphs={paragraphs}",
 headers={
   #"X-RapidAPI-Host": "alexnormand-dino-ipsum.p.rapidapi.com",
   "X-RapidAPI-Key": f"{apikey}"
 }
)
print(response.text)

linebreak()

# Using params argument - prefereable
params = {"words": {words}, "paragraphs": {paragraphs}, "format": {format}}

response = requests.get(f"{url}/",params=params,
 headers={
   #"X-RapidAPI-Host": "alexnormand-dino-ipsum.p.rapidapi.com",
   "X-RapidAPI-Key": f"{apikey}"
 }
)
print(response.text)
