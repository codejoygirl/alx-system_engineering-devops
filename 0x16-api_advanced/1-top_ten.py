#!/usr/bin/python3
"""Contains top_ten function"""
import requests
import sys


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        print("None")
        return

    try:
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            for child in data['data']['children']:
                if 'data' in child and 'title' in child['data']:
                    print(child['data']['title'])
        else:
            print("None")
    except ValueError:
        print("None")

# Check if the script is being run directly
if __name__ == "__main__":
    # Ensure the correct number of command-line arguments are provided
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py subreddit_name")
    else:
        # Call the top_ten function with the provided subreddit name
        top_ten(sys.argv[1])

