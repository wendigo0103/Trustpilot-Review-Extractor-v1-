
# ⭐ Trustpilot Review Extractor

A simple Python script to scrape reviews and star ratings from [Trustpilot](https://www.trustpilot.com) using Selenium and ChromeDriver.

---

## 🔍 Features

- Extracts reviews and their star ratings (1 to 5 stars)
- Scrapes multiple pages (default: 5)
- Runs headlessly (no browser window opens)
- Saves results to a clean CSV file

---

## ⚙️ Requirements

Install the dependencies before running:

```bash
pip install pandas selenium webdriver-manager
```

Make sure **Google Chrome** is installed on your system.

---

## ▶️ How to Use

1. Run the script:

```bash
python trustpilot_scraper.py
```

2. When prompted, **enter a Trustpilot review URL**, like:

```bash
https://www.trustpilot.com/review/allplants.com
```

3. The script will scrape reviews and save them to:

```
trustpilot_reviews.csv
```

---

## ✏️ Customization Guide

### ✅ 1. Filter by Star Rating

By default, the script extracts **all reviews from 1-star to 5-star**.

If you want only certain ratings (e.g. negative reviews), open the script and find this section:

```python
# ⭐️ If you want to scrape only specific ratings, like 1 to 3 stars, modify this line:
# Example: "?stars=1&stars=2&stars=3" → will get only negative/neutral reviews
if "stars=" not in base_input_url:
    base_input_url += "&stars=1&stars=2&stars=3&stars=4&stars=5" if "?" in base_input_url else "?stars=1&stars=2&stars=3&stars=4&stars=5"
```

To get only 1–3 star reviews, **change it to**:

```python
base_input_url += "?stars=1&stars=2&stars=3"
```

To get only 5-star reviews:

```python
base_input_url += "?stars=5"
```

---

### 🔄 2. Change the Number of Pages to Scrape

By default, it scrapes **5 pages**. You can change this:

```python
max_pages = 5
```

Change `5` to however many pages you want to scrape.

---

## 📁 Output

- The extracted data is saved in: `trustpilot_reviews.csv`
- Format:

| Review                  | Rating |
|-------------------------|--------|
| "Great service..."      | 5      |
| "Very bad experience..."| 1      |

---

## 🧑‍💻 Author

Made by **Roshan**  
Lightweight. Efficient. Practical.  
Perfect for sentiment analysis, review filtering, or dataset creation.

---

## 📌 Disclaimer

This tool is for educational and research purposes only. Always check Trustpilot's Terms of Use before scraping large volumes of data.
