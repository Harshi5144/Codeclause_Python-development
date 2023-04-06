import string
import random

# Function to generate a random short code
def generate_short_code(length):
    # Set of characters to choose from for the short code
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    # Generate the random short code
    return ''.join(random.choice(chars) for _ in range(length))

# Dictionary to store the long URL and its corresponding short code
url_dict = {}

# Function to shorten a URL
def shorten_url(long_url):
    # Check if the long URL is already in the dictionary
    if long_url in url_dict:
        return url_dict[long_url]
    # If not, generate a random short code
    short_code = generate_short_code(6)
    # Add the long URL and short code to the dictionary
    url_dict[long_url] = short_code
    # Return the short URL
    return f'http://example.com/{short_code}'

# Example usage
long_url = input()
short_url = shorten_url(long_url)
print(f'Long URL: {long_url}')
print(f'Short URL: {short_url}')
