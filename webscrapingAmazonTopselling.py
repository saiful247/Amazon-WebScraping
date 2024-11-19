import random
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup

# URL of the Amazon Best Sellers page
url = "https://www.amazon.com/gp/bestsellers/electronics/ref=zg_bs_electronics_sm"

# Add headers to mimic a browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}

# Fetch the page content
page = requests.get(url, headers=headers)

if page.status_code == 200:
    soup = BeautifulSoup(page.content, 'html.parser')

    # Initialize DataFrame
    df = pd.DataFrame(columns=["Rank", "Product", "Review Count", "Price"])

    # Find all product cards
    products = soup.find_all("div", class_="a-cardui")

    # Counter for limiting data extraction
    count = 0

    for product in products:
        if count >= 10:
            break  # Limit to 10 products

        try:
            # Extract rank
            rank = product.find("span", class_="zg-bdg-text").text.strip()
            rank = int(rank.replace("#", ""))  # Remove # and convert to int

            # Extract product name
            product_name = product.find(
                "div", class_="_cDEzb_p13n-sc-css-line-clamp-3_g3dy1").text.strip()

            # Extract review count
            review_count = product.find(
                "span", class_="a-size-small").text.strip()
            review_count = int(review_count.replace(",", ""))  # Remove commas

            # Extract price
            price = product.find("span", class_="p13n-sc-price").text.strip()
            price = float(price.replace("$", "").replace(
                ",", ""))  # Remove dollar sign,comma

            # Add to DataFrame
            df.loc[count] = [rank, product_name, review_count, price]
            count += 1
        except AttributeError:
            continue  # Skip products with missing data

    # Display the DataFrame
    # print(df)
    df.to_csv('top_10_amazon_products.csv')

else:
    print(f"Failed to fetch the page. Status code: {page.status_code}")


# The HTTP status code 429 indicates "Too Many Requests." This means Amazon is
# rate-limiting your requests because they suspect automated activity. To resolve this, you can take the following steps:
# 1. Add a delay between requests to avoid sending too many requests in a short period.
# import time
# time.sleep(2)  # Wait 2 seconds between requests

# 2. Use a rotating proxy service to switch IP addresses and avoid detection
# pip install fake-useragent
# from fake_useragent import UserAgent
# import requests

# ua = UserAgent()

# headers = {
#     "User-Agent": ua.random  # Randomly pick a User-Agent
# }

# page = requests.get(url, headers=headers)

# 3. Use a headless browser like Selenium to scrape the data

# 4. Increase the Time Between Requests

time.sleep(random.uniform(2, 7))  # Wait between 2-5 seconds randomly
