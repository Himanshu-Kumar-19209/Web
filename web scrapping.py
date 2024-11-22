import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the website to scrape
url = 'http://books.toscrape.com/'

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the data you want to scrape
    books = []
    for book in soup.find_all('article', class_='product_pod'):
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        availability = book.find('p', class_='instock availability').text.strip()
        
        books.append({
            'Title': title,
            'Price': price,
            'Availability': availability
        })

    # Create a DataFrame from the scraped data
    df = pd.DataFrame(books)

    # Save the DataFrame to a CSV file
    df.to_csv('books.csv', index=False)
    print("Data saved to books.csv")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")