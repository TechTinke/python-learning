# # How to connect to an API using Python
# Params(parameters) - key value pairs appended to a url as a query string
# API key - usique string that identifies and authentictes you when making requests to an API.


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

# import requests

# def get_github_user(username):
#     url = f"https://api.github.com/users/{username}"
#     response = requests.get(url)

#     if response.status_code == 200:
#         username_info = response.json()

#         print(f"Name: {username_info['name']}")
#         print(f"Bio: {username_info['bio']}")
#         print(f"Public Repos: {username_info['public_repos']}")
#         print(f"Followers: {username_info['followers']}")
#     elif response.status_code == 404:
#         print("User not found")
#     elif response.status_code == 429:
#         print("Rate limit exceeded. Please try again later")
#     else:
#         print("The data could not be retrieved")
    
# username1 = "TechTinke"
# get_github_user(username1)
    


#3. Crypto Price Tracker (partial code)
# Finish this script using CoinGecko API (free, no key needed):

# import requests
# import time

# def get_crypto_price(coin_id: str):
#     url = f"https://api.coingecko.com/api/v3/simple/price"
#     params = {
#         "ids": coin_id,
#         "vs_currencies": "usd",
#         "include_24hr_change": "true"
#     }
#     response = requests.get(url, params=params)

#     if response.status_code == 200:
#         data = response.json()

#         if coin_id in data:
#             price = data[coin_id]['usd']
#             change = data[coin_id]['usd_24h_change']
#             return price, change
#         else:
#             print(f"Coin {coin_id} not found!")

#     elif response.status_code == 404:
#         print("f{response.status_code} coin not found")
#     else:
#         print("Coin data could not be retrieved")

# get_crypto_price("bitcoin")

# 4. News Headline Fetcher
# Use NewsAPI.org (free tier: https://newsapi.org (f9dcca8357714870a84147e52b4107f0)).
# Create a function get_top_headlines(country="ke", category="technology"):
# GET https://newsapi.org/v2/top-headlines with params
# Print title, source, published date for top 10 articles
# Handle missing API key (403) or no results
# Bonus: add CLI argument for country/category.

# import requests # to make the HTTP GET request to NewsAPI
# from datetime import datetime # to reformat the date
# import argparse # to handle CLI arguments

# API_KEY = "f9dcca8357714870a84147e52b4107f0"

# def get_top_headlines(country="ke", category="technology"):
#     url = "https://newsapi.org/v2/top-headlines"
#     params = {"country": country,
#               "category": category,
#               "pageSize": 10,
#               "apiKey": API_KEY}
# # params(country, category, pageSize and apiKey) are what you send to the API to tell it what data you want
# # Response fields(title, source and published date) are what the API sends back to you in response to your request
#     response = requests.get(url, params=params)

#     if response.status_code == 200:
#         data = response.json() # Converts the raw response into a Python dictionary

#             #         {
#             # "status": "ok",
#             # "totalResults": 10,
#             # "articles": [
#             #     {
#             #     "title": "...",
#             #     "source": {"id": "bbc", "name": "BBC News"},
#             #     "publishedAt": "2024-01-15T09:30:00Z"
#             #     }
#             # ]
#             # }
#         articles = data.get("articles", []) # safely extracts the articles list and returns an empty list if the key("articles") is missing 
#     elif response.status_code == 401 or response.status_code == 403: # Error code 401 or 403 means authentication failed # Error code 500 means server error # Error code 429 means rate limited
#     #elif response.status_code in (401, 403):
#         print("Error: Invalid or missing API key.")
#         return
#     else:
#         print(f"Error {response.status_code}: Could not retrieve headlines.")
#         return
#     if not articles:
#         print(f"No articles founds for {country} under {category}")
#         return
    
#     print(f"\nTop {len(articles)} {category.upper()} headlines [{country.upper()}]")
#     print("-" * 60)

#     for i, article in enumerate(articles, start=1):
#         title = article.get("title", "No title")
#         source = article.get("source", {}).get("name", "Unknown source")
#         published = article.get("publishedAt", "")
#         if published:
#             published = datetime.strptime(published, "%Y-%m-%dT%H:%M:%SZ")
#             published = published.strftime("%d %b %Y, %H:%M UTC")

#         print(f"{i}. {title}")
#         print(f"Source: {source} | Published: {published}")
#         print()
# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description="Fetch top news headlines.")
#     parser.add_argument("--country", default="ke", help="Country code (default: ke)")
#     parser.add_argument("--category", default="technology",
#                         help="Category: business, entertainment, health, science, sports, technology (default: technology)")
#     args = parser.parse_args()

#     get_top_headlines(country=args.country, category=args.category)

# python requestapidata.py --country us --category technology - this command is run from the terminal for calling the function from the terminal


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

# import requests

# API_KEY = "a829e4836c22d656daf84ff9"

# def convert_currency(amount: float, from_curr:str, to_curr:str):
#     url = f"https://v6.exchangerate-api.com/v6/a829e4836c22d656daf84ff9/latest/{from_curr}"
#     for attempt in range(3):
#         try:
#             api_response = requests.get(url)
#             break
#         except requests.exceptions.RequestException:
#             print(f"Attempt {attempt + 1} failed, retrying ...")
#             if attempt == 2:
#                 print("All 3 attempts failed. Check your network connection and try again later!")
#                 return
    
#     if api_response.status_code == 200:
#         data = api_response.json()
#         conversion_rates = data.get("conversion_rates", [])
#         to_rate = conversion_rates.get(to_curr)

#         if to_rate:
#             converted_amount = amount * to_rate
#             print(f"{amount} {from_curr} = {converted_amount:.2f} {to_curr}")
#         else:
#             print("That currency does not exist")
#             return
#     elif api_response.status_code == 401 or api_response.status_code == 403:
#         print("Error: Missing or invalid API Key!")
#         return
#     elif api_response.status_code == 429:
#         print("Rate Limit exceeded, Please try again later")
#         return
#     else:
#         print("Could't not retrieve API data")

# convert_currency(709890, "KES", "USD")
# convert_currency(190000, "KES", "EUR")
# convert_currency(625500, "KES", "GBP")


# 7. GitHub Repository Stats Dashboard
# Create a script that:
# Takes a GitHub username
# GET /users/{username}/repos
# For each repo: name, stars, forks, language, last updated
# Sort by stars descending
# Print top 5 repos + total stars across all
# Handle pagination (if >100 repos), 404 user, rate limits.

import requests

def repo_stats(username):
    url = f"https://api.github.com/users/{username}/repos"
    api_response = requests.get(url)

    if api_response.status_code == 200:
        repo_data = api_response.json()
        repo_data = sorted(repo_data, key=lambda repo: repo["stargazers_count"], reverse=True)
        #         # Long way
        # def get_stars(repo):
        #     return repo["stargazers_count"]

        # # Short way (lambda)
        # lambda repo: repo["stargazers_count"]
        
    elif api_response.status_code == 429:
        print("Rate limit exceeded! Please try again later")
        return
    elif api_response.status_code == 404:
        print(f"Error: {username} could not be found")
        return
    else:
        print("API data could not be retrieved")
        return
    
    total_stars = 0
    for repo in repo_data:
     total_stars = total_stars + repo["stargazers_count"]
    
    for i, repo in enumerate(repo_data, start=1):
        name = repo["name"]
        stars = repo["stargazers_count"]
        forks = repo["forks"]
        language = repo["language"]
        last_updated = repo["updated_at"]
        

        print(f"{i}. {name}")
        print(f"Stars: {stars} | Forks: {forks} | Language: {language} | Last Updated: {last_updated}")
        print(" ")

        if i == 5:
            break
    print(f"Total stars across all repos: {total_stars}")

repo_stats("github")
print()
print("----------")
print()
repo_stats("facebook")
print()
print("----------")
print()
repo_stats("microsoft")




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