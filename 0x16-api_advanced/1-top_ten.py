#!/usr/bin/python3
"""
Script to print hot posts on a given Reddit subreddit.
"""

import sys
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    # Construct the URL for the subreddit's hot posts in JSON format
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"

    # Define headers for the HTTP request, including User-Agent
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    # Define parameters for the request, limiting the number of posts to 10
    params = {
        "limit": 10
    }

    # Send a GET request to the subreddit's hot posts page
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    # Check if the response status code indicates a not-found error (404)
    if response.status_code == 404:
        print("None")
        return

    try:
        # Parse the JSON response and extract the 'data' section
        results = response.json().get("data")
        
        # Print the titles of the top 10 hottest posts
        for child in results.get("children"):
            print(child.get("data").get("title"))
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

