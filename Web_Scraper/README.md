# 🌐 Basic Web Scraper

A simple Python script that scrapes headlines and articles from a given website. The app uses requests and BeautifulSoup to download and parse the page, and it can optionally save the extracted data into a CSV file.

## 🚀 Features

- Downloads the HTML of any website.
- Extracts headlines (h1, h2, h3, or common title classes).
- Extracts articles (title, date, and summary when available).
- Saves scraped data into a CSV file.
- Interactive command-line interface with multiple options.

### 🛠️ Requirements

• Python 3.8+

• Install dependencies:

    pip install requests beautifulsoup4

### ▶️ Usage

Run the script:

    python app.py


Follow the prompts:

• Enter the URL of the website you want to scrape.

• Choose an option:

  1 → Extract headlines

  2 → Extract full articles (title, date, summary)

  3 → Exit

• Decide whether to save the extracted data into a CSV file.

### 📈 Example output
    === BASIC WEB SCRAPER ===
    Insert the URL of the website you want to scrape: https://example.com
    
    Downloading the website https://example.com...
    Website downloaded successfully!
    
    Options:
    1. Extract headlines
    2. Extract articles
    3. Exit
    Choose an option (1-3): 1
    
    Extracting headlines...
    
    5 headlines extracted successfully!
    1. Example Headline Number One
    2. Breaking News: Example Story Two
    3. Example Article Number Three
    4. Latest Updates from Example
    5. Example Feature Story Five
    
    Would you like to save the headlines in a CSV file? (y/n): y
    Data saved in headlines.csv successfully!

### 🧩 Functions Overview

• obtain_html(url) → Downloads the HTML of the website using a custom User-Agent.

• extract_news_headlines(html) → Extracts all possible headlines (h1, h2, h3, .title, etc.).

• extract_articles(html) → Extracts structured articles (title, date, summary).

• save_in_csv(data, filename) → Saves scraped data into a CSV file.

• main(html) → Interactive CLI menu.

### 📜 License

This project is licensed under the MIT License.
