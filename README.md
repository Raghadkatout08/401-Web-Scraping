# 401-Web-Scraping

This script scrapes book data from the [Books to Scrape](http://books.toscrape.com/) website and saves it into a JSON file. It also counts the number of books with a specific star rating.

## Features
- Extracts book details (title, rating, price, availability) from specified categories.
- Saves the extracted data into a JSON file.
- Counts the number of books with a specified star rating.

## Requirements
- `requests`
- `beautifulsoup4`

You can install the required packages using:
```sh
pip install requests beautifulsoup4
