import pandas as pd
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# ------------------------
# Trustpilot Review Extractor v1
# Author: Roshan LLizu Samuel
# ------------------------

# Step 1: Ask the user to enter a Trustpilot URL (e.g., https://www.trustpilot.com/review/allplants.com)
base_input_url = input("Enter Trustpilot URL: ").strip()

# Step 2: Add star rating filters to get only 1-5 star reviews
# ⭐️ If you want to scrape only specific ratings, like 1 to 3 stars, modify this line:
# Example: "?stars=1&stars=2&stars=3" → will get only negative/neutral reviews
# Default here: fetches ALL ratings (1 to 5 stars)
if "stars=" not in base_input_url:
    base_input_url += "&stars=1&stars=2&stars=3&stars=4&stars=5" if "?" in base_input_url else "?stars=1&stars=2&stars=3&stars=4&stars=5"

# Step 3: Set Chrome to headless mode (no browser window pops up)
chrome_options = Options()
chrome_options.add_argument("--headless")

# Step 4: Automatically set up Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Step 5: Initialize storage for reviews and ratings
reviews, ratings = [], []
max_pages = 5  # Change this to scrape more or fewer pages

# Step 6: Loop through multiple pages
for page in range(1, max_pages + 1):
    full_url = f"{base_input_url}&page={page}" if "?" in base_input_url else f"{base_input_url}?page={page}"
    print(f"Scraping page {page}: {full_url}")
    driver.get(full_url)
    time.sleep(3)  # Wait for content to load

    # Step 7: Extract review text and star ratings
    review_elements = driver.find_elements(By.CSS_SELECTOR, '[data-service-review-text-typography]')
    rating_elements = driver.find_elements(By.CSS_SELECTOR, '[data-service-review-rating]')

    if not review_elements:
        print("No more reviews found.")
        break

    for review, rating in zip(review_elements, rating_elements):
        text = review.text.strip()
        star = rating.get_attribute('data-service-review-rating')
        if text and star:
            reviews.append(text)
            ratings.append(int(star))

# Step 8: Clean up
driver.quit()

# Step 9: Save the data to a CSV file
df = pd.DataFrame({'Review': reviews, 'Rating': ratings})
filename = "trustpilot_reviews.csv"
df.to_csv(filename, index=False)

# Step 10: Confirmation
print(f"\n✅ Done. {len(df)} reviews saved to {filename}.")
print("Saved at:", os.path.abspath(filename))
