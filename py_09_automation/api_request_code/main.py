# import necessary libraries
import requests

# define base URL
base_url = "https://api.upcitemdb.com/prod/trial/lookup"

# define parameters
parameters = {"upc": "025000044908"}

# make API request, passing in base URL and parameters
response = requests.get(base_url, params=parameters)

# print out the response URL 
print(response.url)