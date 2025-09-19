# 🚨 Price Notifier 💰

A Python application that allows you to track product prices from different websites. You can add products, set a target price, refresh prices, and receive notifications when the current price meets your target.  

⚠️ Note: This tool currently works with **static HTML pages**. For websites that load prices dynamically with JavaScript, you may need to use APIs or automation tools like Selenium/Playwright.

---

## 🚀 Features

- Add products with a name, URL, and target price.
- Extract prices using **CSS selectors** or predefined common selectors.
- Works with thousands separators `,` or `.`.
- Saves all tracked products in a JSON file.
- Refresh prices and keep a **price history log**.
- Remove products from the tracking list.
- Lightweight and fully implemented in Python.

---

### 🛠️ Requirements

- Python 3.8+
- Libraries:
  - `requests`
  - `beautifulsoup4`

Install dependencies with:

    ```bash
    pip install -r requirements.txt

__________________________________________________________________________________________________________________________________________________________________________________
### ▶️ Usage

Run the script:

    python app.py

Steps performed by the script:

1.	Add a product by entering:
   
  •	Product name
    
  •	Product URL
   
  •	Target price
   
  •	(Optional) CSS selector for extracting the price
   
  •	(Optional) Thousands separator format

2.	Display all tracked products and their current prices.

3.	Refresh all prices and update price history.
   
4.	Remove a product from tracking.

5.	Exit the application.
__________________________________________________________________________________________________________________________________________________________________________________
### 📈 Example output
    === PRICE NOTIFIER ===
    
    Options:
    1. Add a new product to track
    2. Display tracked products
    3. Refresh prices
    4. Remove product
    5. Exit
    
    Insert the name of the product: Laptop
    Insert the URL of the product: https://example.com/product123
    Insert your target price for the product: 600
    Would you like to select your CSS selector? (y/n): n
    What separates the price? (. or ,) [By default ',']: ,
    
    Product 'Laptop' has been added successfully
__________________________________________________________________________________________________________________________________________________________________________________
### 🧩 Functions Overview

•	get_prices() → Extracts the product price from a URL using CSS selectors or predefined selectors.

•	add_product() → Adds a new product to the tracking list and stores it in a JSON file.

•	refresh_price() → Updates the current price and maintains a price history.

•	remove_product() → Deletes a product from the tracking list.

•	load_product() / save_product() → Handles reading and writing the tracked products file.

### 📜 License

This project is licensed under the MIT License.
