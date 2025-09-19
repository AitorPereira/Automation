from app import PriceNotifier

# NOTE:
# This app currently works only with static HTML content.
# Some websites (e.g., MercadoLibre, Amazon) load prices dynamically with JavaScript.
# Since we are using `requests` + `BeautifulSoup`, we only fetch the initial HTML,
# not the dynamically rendered content. That's why sometimes `price` appears as
# "Not available" even if you see it in the browser.
# 
# To handle dynamic pages, we would need tools like Selenium, Playwright,
# or an API if the website provides one.


def display_product(app_notify):
    """ Displays a list of tracked products """
    products = app_notify.load_product()

    if not products:
        print ("\nThere are no tracked prices set")
        return
    
    print (f"\n=== TRACKED PRODUCTS ({len(products)}) ===")

    for i, product in enumerate(products, 1):
        current_price = app_notify.get_prices(
            product['url'],
            product.get('selector_css'),
            product.get('thousands_separator', ',')
            )
        if current_price:
            product['current_price'] = current_price
        else:
            product['current_price'] = "Not available"

        print(f"\n{i}. {product['name']}")
        print(f"    URL: {product['url']}")
        print(f"    Current price: {product.get('current_price', 'Not available')}")
        print(f"    Target price: {product['target_price']}")

        #Display recent price history if it exists
        if product.get('price_history'):
            print("     Record of recent prices:")
            for entry_product in product['price_history'][-3:]: #Display the last 3
                print(f"    {entry_product['date']} : {entry_product['price']}")

def main():
    #Main Function
    print("=== PRICE NOTIFIER ===")

    #Create an instance of the PriceNotifier class
    app_notify = PriceNotifier()

    while True:
        print("\nOptions:")
        print("1. Add a new product to track")
        print("2. Display tracked products")
        print("3. Refresh prices")
        print("4. Remove product")
        print("5. Exit")

        option = input("Select your option (1-5): ")
        if option == "1":
            #Add a new product
            name = input("\nInsert the name of the products: ")
            url = input("Enter the URL product: ")
            target_price = float(input("Enter your target price for the product: "))

            use_selector = input("Would you like to provide a CSS selector? (y/n): ").lower() == 'y'
            selector_css = None

            if use_selector:
                selector_css = input("Enter the CSS selector for the price: ")

            #Ask for the thousands separator
            thousands_separator = input("What character separates the thousands in the price? (. or ,) [default ',']: ").strip()
            if thousands_separator not in ['.',',']:
                thousands_separator = ','
                print ("Using the default thousands separator: ','")
                
            result = app_notify.add_product(name, url, target_price, selector_css, thousands_separator)

            if result:
                print(f"\nProduct '{name}' has been added succesfully")
            else:
                print(f"\nUnable to add product '{name}' (it may already exist)")

        
        elif option == "2":
            #Display products"
            display_product(app_notify)

        elif option == "3":
            print ("\nRefreshing prices for all products...")
            refreshed_products = app_notify.refresh_price()

            if refreshed_products:
                print(f"\n{len(refreshed_products)} item/s were found under your target price!")
                for product in refreshed_products:
                    print(f"- {product['name']}: Current price {product['current_price']}")
            else:
                print("\nNo significant price changes were found")

        elif option == "4":
            #Remove a product
            display_product(app_notify)

            products = app_notify.load_product()
            if products:
                try:
                    index = int(input("\Enter the product number to delete: "))
                    if app_notify.remove_product(index):
                        print (f"\nProduct #{index} has been removed succesfully")
                    else:
                        print (f"\nUnable to remove product #{index}")
                except ValueError:
                    print(f"Please, enter a valid number")
            else:
                print("\nThere are no products to remove")

        elif option == "5":
            #Exit
            print("\nThank you for using Price Notifier!")
            break

        else:
            print("\nInvalid option. Please, select a number from 1 to 5.")

if __name__ == "__main__":
    main()
