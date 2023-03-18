import requests

# Replace 'your_api_key' with your own API key from DraftKings
api_key = 'your_api_key'

# Set the URL for the DraftKings API
url = f'https://api.draftkings.com/partners/v1/events?format=json&includePromotions=true&includeState=true'

# Set the parameters for the API request
params = {
    'api_key': api_key,
    'includePromotions': 'true',
    'includeState': 'true'
}

# Send the API request and get the response
response = requests.get(url, params=params)

# Parse the JSON data in the response
data = response.json()

# Extract the relevant data from the response
for event in data['events']:
    print(event['name'])
    print(event['eventStartTime'])
    for market in event['markets']:
        print(market['name'])
        for outcome in market['outcomes']:
            print(outcome['name'])
            print(outcome['price'])
