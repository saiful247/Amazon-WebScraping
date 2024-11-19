from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
import random

# Configure Selenium
options = Options()
options.add_argument("--headless")  # Run in headless mode
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36")

# Initialize WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Amazon URL
url = "https://www.amazon.com/gp/bestsellers/electronics/ref=zg_bs_electronics_sm"

# Open the page
driver.get(url)
time.sleep(random.uniform(2, 5))  # Random delay to avoid rate-limiting

# Initialize DataFrame
df = pd.DataFrame(columns=["Rank", "Product", "Review Count", "Price"])

# Find all product cards
products = driver.find_elements(By.CSS_SELECTOR, "div.a-cardui")

# Counter for limiting data extraction
count = 0

for product in products:
    if count >= 10:  # Limit to top 10 products
        break

    try:
        # Extract rank
        rank = product.find_element(
            By.CSS_SELECTOR, "span.zg-bdg-text").text.strip()
        rank = int(rank.replace("#", ""))  # Remove # and convert to int

        # Extract product name
        product_name = product.find_element(
            By.CSS_SELECTOR, "div._cDEzb_p13n-sc-css-line-clamp-3_g3dy1").text.strip()

        # Extract review count
        review_count = product.find_element(
            By.CSS_SELECTOR, "span.a-size-small").text.strip()
        review_count = int(review_count.replace(",", ""))  # Remove commas

        # Extract price
        price = product.find_element(
            By.CSS_SELECTOR, "span.p13n-sc-price").text.strip()
        price = float(price.replace("$", "").replace(
            ",", ""))  # Remove dollar sign and commas

        # Add to DataFrame
        df.loc[count] = [rank, product_name, review_count, price]
        count += 1
    except Exception as e:
        print(f"Error while processing a product: {e}")
        continue

# Close the browser
driver.quit()

# Save to CSV
df.to_csv('top_10_amazon_products.csv', index=False)

# Print the DataFrame
print(df)
