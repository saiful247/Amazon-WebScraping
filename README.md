# Amazon-WebScraping
For this web scraping i used BeautifulSoup, Selenium

# Strictly Education Perpose Only 

# Amazon is not allowing developers to scrap there data on the website. The html classes , ids changing automatically with time. so you need to mimic the server. for this use below code
# Add headers to mimic a browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}

# If you encounter : The HTTP status code 429 indicates "Too Many Requests." This means Amazon is
# rate-limiting your requests because they suspect automated activity. To resolve this, you can take one of the following steps:

# 1. Add a delay between requests to avoid sending too many requests in a short period.
import time
time.sleep(2)  # Wait 2 seconds between requests

# 2. Use a rotating proxy service to switch IP addresses and avoid detection
pip install fake-useragent
from fake_useragent import UserAgent
import requests

ua = UserAgent()

headers = {
     "User-Agent": ua.random  # Randomly pick a User-Agent
}
page = requests.get(url, headers=headers)

# 3. Use a headless browser like Selenium to scrape the data

# 4. Increase the Time Between Requests
import random
import time
time.sleep(random.uniform(2, 7))  # Wait between 2-5 seconds randomly
