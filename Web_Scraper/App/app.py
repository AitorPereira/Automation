import csv
import html
import requests
from bs4 import BeautifulSoup

#This function will obtain the HTML code of the website
def obtain_html(url):
    try:
        #Configure an User-Agent to avoid being blocked by the website
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }

        #Make the request to the website
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code == 200:
            return response.text
        else:
            print (f"Error obtaining the HTML code of the website: Code {response.status_code}")
            return None
    
    except Exception as e:
        print (f"Error obtaining the website: {e}")
        return None

def extract_news_headlines(html):
    #Create a BeautifulSoap object to analyze the HTML code
    soup = BeautifulSoup(html, 'html.parser')

    #Find every headline in the website
    #Note: These selectors are general and may need to be adjusted for specific websites
    headlines = []

    #Search for h1,h2,h3 elements that could contain the headlines
    for heading in soup.find_all(['h1','h2','h3']):
        #Filter out elements that seems to be headlines (e.g. certain length or specific classes)
        if heading.text.strip() and len(heading.text.strip()) > 15:
            headlines.append(heading.text.strip())

    for element in soup.select('.title, .headline, .article-title, .news-title'):
        if element.text.strip() and element.text.strip() not in headlines:
            headlines.append(heading.text.strip())
    
    return headlines

def extract_articles(html):
    #    #Create a BeautifulSoap object to analyze the HTML code
    soup = BeautifulSoup(html, 'html.parser')

    #List to store the articles
    articles = []

    #To avoid duplicates
    seen_titles = set()

    #Find every article in the website
    #Note: These selectors are general and may need to be adjusted for specific websites
    for article_element in soup.select('article, .article, .post, .news-item'):
        article = {}

        #Extract title
        title_elem = article_element.find(['h1', 'h2', 'h3']) or article_element.select_one('.title, .headline')
        if title_elem:
            title = title_elem.text.strip()
            if title in seen_titles:
                continue #Skip duplicates
            article['title'] = title
            seen_titles.add(title)
        else:
            continue #If there is no article, continue

        #Extract date if it's available
        date_elem = article_element.select_one('date, .time, .published, .timestamp')
        article['date'] = date_elem.text.strip() if date_elem else ""

        #Extract summary if it's available
        summary_elem = article_element.select_one('.summary, .except, .description, .snippet, p')
        article['summary'] = summary_elem.text.strip() if summary_elem else ""

        #Add to article list
        articles.append(article)

    return articles

def save_in_csv(data, filename):
    try:
        if not data:
            print("There is no data to save")
            return False
        
        #Obtain the columns names of the first dictionary
        columns = data[0].keys()

        #Write the data in a CSV file
        with open(filename, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=columns)
            writer.writeheader() #Writing headlines
            writer.writerows(data) #Writing data rows

        print (f"Data saved in {filename} successfully!")
        return True
    
    except Exception as e:
        print (f"Error saving the data in {filename}: {e}")
        return False



def main(html):
    print ("=== BASIC WEB SCRAPER ===")
    
    url = input("Insert the URL of the website you want to scrape: ")

    print (f"Downloading the website {url}...")
    html = obtain_html(url)

    if not html:
        print("It was not possible to download the website")
        return 
    
    print("Website downloaded successfully!")
    
    print("n\Options:")
    print("1. Extract headlines")
    print("2. Extract articles")
    print("3. Exit")

    option = input("Choose an option (1-3): ")

    if option == "1":
        print ("Extracting headlines...")
        headlines = extract_news_headlines(html)

        print (f"\n {len(headlines)} headlines extracted successfully!")
        for i, title in enumerate(headlines, 1):
            print (f"{i}. {title}")
        
        #Save headlines in a CSV file
        if headlines and input("\nWould you like to save the headlines in a CSV file? (y/n): ").lower() == "y":
            #Convert headlines to a list of dictionaries
            data = [{'number': i, 'title': title} for i, title in enumerate(headlines, 1)]
            save_in_csv(data, "headlines.csv")

    elif option == "2":
        print ("Extracting headlines...")
        articles = extract_articles(html)

        print (f"\n {len(articles)} headlines extracted successfully!")
        for i, article in enumerate(articles, 1):
            print (f"{i}. {article.get('title','no title')}")
            if article.get('date'):
                print (f"   Date: {article['date']}")
            elif article.get('summary'):
                print (f"   Summary: {article['summary']}")
        
        #Save headlines in a CSV file
        if articles and input("\nWould you like to save the articles in a CSV file? (y/n): ").lower() == "y":
            #Convert headlines to a list of dictionaries
            save_in_csv(articles, "articles.csv")

    elif option == "3":
        print("Goodbye")
        return

    else:
        print ("Invalid option")

if __name__ == "__main__":
    main(html)
