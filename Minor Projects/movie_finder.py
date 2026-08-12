"""
Movie Info Finder (OMDb API)
------------------------------
Searches for a movie by title using the OMDb API and displays
its plot, rating, cast, and other details.

SETUP:
1. Get a free API key from https://www.omdbapi.com/apikey.aspx
2. Set it as an environment variable before running:
     Windows (PowerShell):  $env:OMDB_API_KEY="your_key_here"
     Mac/Linux:              export OMDB_API_KEY="your_key_here"
   Or just paste it into the API_KEY variable below (not recommended
   for shared/public code, but fine for personal local use).

Install dependency:
    pip install requests

Usage: python 18_movie_finder.py
"""

import os
import requests

API_KEY = "76e4f77a"
BASE_URL = "http://www.omdbapi.com/"


def fetch_movie(title):
    params = {"apikey": API_KEY, "t": title, "plot": "full"}
    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return None


def print_movie(data):
    if data.get("Response") == "False":
        print(f"Not found: {data.get('Error')}")
        return

    print("\n" + "=" * 50)
    print(f"{data.get('Title')} ({data.get('Year')})")
    print("=" * 50)
    print(f"Genre:     {data.get('Genre')}")
    print(f"Director:  {data.get('Director')}")
    print(f"Actors:    {data.get('Actors')}")
    print(f"Runtime:   {data.get('Runtime')}")
    print(f"IMDb Rating: {data.get('imdbRating')}/10")
    print(f"\nPlot: {data.get('Plot')}")

    ratings = data.get("Ratings", [])
    if ratings:
        print("\nOther ratings:")
        for r in ratings:
            print(f"  {r['Source']}: {r['Value']}")


def main():
    print("=== MOVIE INFO FINDER ===")

    if not API_KEY:
        print("\nNo API key found. Set the OMDB_API_KEY environment variable")
        print("or edit the API_KEY variable in this script before running.\n")
        return

    while True:
        title = input("\nEnter a movie title (or 'q' to quit): ").strip()
        if title.lower() == "q":
            print("Goodbye!")
            break
        if not title:
            continue

        data = fetch_movie(title)
        if data:
            print_movie(data)


if __name__ == "__main__":
    main()
