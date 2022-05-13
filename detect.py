import requests, json
import config

key = config.api_key
endpoint = config.endpoint
location = config.location

params = {
    'api-version': '3.0'
}

headers = {
    'Ocp-Apim-Subscription-Key': key,
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json'
}

text = input("Please enter a string:")

body = [{
    'text': text
}]

request = requests.post(endpoint, params=params, headers=headers, json=body)
response = request.json()

print(response)

language = (response[0]['language'])
certainty = (response[0]['score'])

print('The text is in '+ language + ' with a confidence score of ' + str(round(certainty)*100) + '%')
