import pyshorteners

def shorten_url(url):
    return pyshorteners.Shortener().tinyurl.short(url)

# Take user input for the original URL
original_url = input("Enter the URL you want to shorten: ")

# Get the shortened URL
short_url = shorten_url(original_url)

# Display the stylish output
print("\nShortening your link... 🌐")
print("Original URL:", original_url)
print("Shortened URL:", short_url)
print("\nShare this cool link with your friends! 🚀")
