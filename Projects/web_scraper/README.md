📦 Amazon Product Web Scraper

📌 Overview

This is a simple Python web scraper built with Requests and BeautifulSoup to extract product details from Amazon product pages.
It retrieves key product information such as title and price and returns it in a clean, structured dictionary.

⚠️ Note: This project is for educational purposes only. Always follow Amazon’s Terms of Service and robots.txt guidelines when scraping.

🛠 Features

Scrapes product title and price from Amazon product pages.

Uses custom HTTP headers to mimic a real browser request.

Returns product details in a dictionary format for easy integration into other Python scripts.

Simple command-line interface for URL input.

📂 Requirements

Install the required Python libraries:

pip install requests beautifulsoup4 lxml

▶️ How to Run

Save the script as amazon_scraper.py.

Run the script:

python amazon_scraper.py


Enter the Amazon product URL when prompted.

The script will output a dictionary like this:

{'title': 'Example Product Name', 'price': '$29.99'}

📜 Code Flow

Send HTTP request to the given Amazon product URL with custom headers.

Parse HTML content using BeautifulSoup with the lxml parser.

Locate product details using HTML element IDs and classes:

Product Title → id="productTitle"

Price → class="a-price"

Return extracted details in a dictionary format.

🔍 Example Output

Input:

Enter product url: https://www.amazon.com/dp/B08N5WRWNW


Output:

{'title': 'Apple AirPods Pro (2nd Generation)', 'price': '$249.00'}

⚠️ Limitations

Amazon frequently changes its HTML structure, so element selectors may need updates over time.

Amazon may block repeated scraping requests from the same IP. Consider adding timeouts, proxies, or rotating user agents for production use.

Only extracts title and price — other details can be added by modifying the scraper.

📈 Skills Demonstrated

HTTP requests with custom headers

HTML parsing with BeautifulSoup

Data extraction from structured web content

Error handling in web scraping scripts