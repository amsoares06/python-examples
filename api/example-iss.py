import requests
import json
from datetime import datetime

def linebreak():
    print(f"----------------------------------------")

linebreak()

# Status code 404
response = requests.get("http://api.open-notify.org/this-api-doesnt-exist")
print(f"API not found responde code: {response.status_code}")

linebreak()

# Successful request
response = requests.get("http://api.open-notify.org/astros.json")
print(f"Sucessful request return code: {response.status_code}")

# Print request
print(f"Response: {response.json()}")

linebreak()

# Pretty Print for JSON object
def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

print(f"Pretty print JSON")
jprint(response.json())

linebreak()

# Using an API with Query Parameters
parameters = {
    "lat": 40.71,
    "lon": -74
}

response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters) # http://open-notify.org/Open-Notify-API/ISS-Pass-Times/
print(f"Using an API with Query Parameters")
jprint(response.json())

linebreak()

# Extract the pass times from our JSON object
pass_times = response.json()['response']
print(f"Extract the pass times from our JSON object")
jprint(pass_times)

linebreak()

# use a loop to extract just the five risetime values
risetimes = []

for d in pass_times:
    time = d['risetime']
    risetimes.append(time)

print(f"Risetimes: {risetimes}")

linebreak()

# convert from unix time
times = []
i = 0
print(f"Risetimes:")
for rt in risetimes:
    time = datetime.fromtimestamp(rt)
    times.append(time)
    print(f"Risetime {i+1} : {time}")
    i = i + 1
