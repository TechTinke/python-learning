# # How to connect to an API using Python

# import requests # Import the requests modules for requests

# base_url = "https://pokeapi.co/api/v2"

# def get_pokemon_info(name):
#     url = f"{base_url}/pokemon/{name}"
#     response = requests.get(url)
#     print(response) # prints out the status code
    
#     if response.status_code == 200:
#         pokemon_data = response.json()
#         print("Data retrieved!")
#         return pokemon_data
#     else:
#         print(f"Failed to retrieve data {response.status_code}")

# pokemon_name = "Typhlosion"
# pokemon_info = get_pokemon_info(pokemon_name)

# if pokemon_info:
#     print(f"Name: {pokemon_info['name'].capitalize()}")
#     print(f"Id: {pokemon_info['id']}")
    # print(f"Height: {pokemon_info['height']}")
#     print(f"Weight: {pokemon_info['weight']}")

# STATUS CODES
# 1. 200 - response was okay

# WORK TO BE DONE
# 1. Weather Data from Open-Meteo
# Use the free Open-Meteo API (https://api.open-meteo.com/v1/forecast).
# Create a function get_weather(lat: float, lon: float) that:
# Makes a GET request with params: latitude, longitude, current_weather=true
# Prints temperature, wind speed, weather code if 200
# Handles non-200 status with error message
# Test with Nairobi coordinates (lat ≈ -1.286, lon ≈ 36.817).

# import requests

# def get_weather(lat:float, lon: float):
#     url = "https://api.open-meteo.com/v1/forecast"
#     params = {"latitude": lat,
#               "longitude": lon,
#               "current_weather": "true"
#     }
#     response = requests.get(url, params=params)

#     if response.status_code == 200:
#         data = response.json()
#         weather = data["current_weather"]

#         print(f"Temperature: {weather['temperature']} degree celcius")
#         print(f"Wind Speed: {weather['windspeed']} km/hr")
#         print(f"Weather Code: {weather['weathercode']}")
#     else:
#         print(f"Failed to retrieve data {response.status_code}")

# get_weather(-1.286, 36.817)



# 2. GitHub User Info
# Create get_github_user(username: str):
# GET https://api.github.com/users/{username}
# If 200, print: name, bio, public_repos, followers
# If 404, print "User not found"
# Handle rate limit (429) with nice message
# Test with your GitHub username or "octocat".

import requests

def get_github_user(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)

    if response.status_code == 200:
        username_info = response.json()

        print(f"Name: {username_info['name']}")
        print(f"Bio: {username_info['bio']}")
        print(f"Public Repos: {username_info['public_repos']}")
        print(f"Followers: {username_info['followers']}")
    elif response.status_code == 404:
        print("User not found")
    elif response.status_code == 429:
        print("Rate limit exceeded. Please try again later")
    else:
        print("The data could not be retrieved")
    
username1 = "TechTinke"
get_github_user(username1)
    


#3. Crypto Price Tracker (partial code)
# Finish this script using CoinGecko API (free, no key needed):

# Pythonimport requests
# import time

# def get_crypto_price(coin_id: str):
#     url = f"https://api.coingecko.com/api/v3/simple/price"
#     params = {
#         "ids": coin_id,
#         "vs_currencies": "usd",
#         "include_24hr_change": "true"
#     }
#     response = requests.get(url, params=params)
#     # Finish: check status, parse JSON, return price + 24h change %
#     # Handle errors (e.g. 404 coin not found)
#     pass

# # Finish: loop to track Bitcoin, Ethereum, Solana every 60 seconds
# # Print: "BTC: $XXXX (24h: +X.XX%)" etc.
# # Run for 5 cycles or until Ctrl+C
# Show real-time-ish price updates in terminal.

# 4. News Headline Fetcher
# Use NewsAPI.org (free tier: https://newsapi.org — you’ll need an API key).
# Create a function get_top_headlines(country="ke", category="technology"):
# GET https://newsapi.org/v2/top-headlines with params
# Print title, source, published date for top 10 articles
# Handle missing API key (403) or no results
# Bonus: add CLI argument for country/category.


# 5. Pokémon Team Builder (expand your example)
# Extend your PokéAPI code:
# Function get_pokemon_details(name) → return dict with name, types, stats, sprite URL
# Function build_team(team_names: list[str]) → get data for 6 Pokémon
# Print team summary: name, types, total base stat
# Handle invalid names (404) gracefully
# Bonus: use @cache decorator to avoid repeated API calls



# 6. Currency Exchange Rate Converter
# Use free ExchangeRate-API (https://www.exchangerate-api.com — free key needed).
# Create convert_currency(amount: float, from_curr: str, to_curr: str):
# GET latest rates
# Calculate converted amount
# Print formatted result
# Add retry logic (3 attempts) on network errors
# Show converting KES to USD, EUR, GBP.


# 7. GitHub Repository Stats Dashboard
# Create a script that:
# Takes a GitHub username
# GET /users/{username}/repos
# For each repo: name, stars, forks, language, last updated
# Sort by stars descending
# Print top 5 repos + total stars across all
# Handle pagination (if >100 repos), 404 user, rate limits.


# 8. IP Geolocation Lookup
# Use free ipapi.co API (https://ipapi.co/{ip}/json/):
# Function get_location(ip="self") → get city, country, lat/lon, timezone
# Print formatted info
# Handle invalid IP or API errors
# Bonus: auto-detect user’s IP if no argument given.


# 9. Open Library Book Search
# Use Open Library API (https://openlibrary.org/search.json?q=...):
# Function search_books(query: str, limit=5)
# GET search results
# For each: title, author_name, first_publish_year, cover URL
# Print nice list
# Handle no results or network issues
# Bonus: download cover image if available (use requests.get + save to file).

# 10. Mini API Client with Retry & Logging (longer project)
# Build a reusable ApiClient class:
# __init__(self, base_url, api_key=None)
# Method get(self, endpoint, params=None, retries=3) → handles GET with retry on 5xx errors
# Logs every request + status + time taken
# Raises custom ApiError on failure
# Use it to fetch data from two different APIs (e.g. PokeAPI + Open-Meteo).
# Show retry working on simulated flaky endpoint.