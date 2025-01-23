import requests
from bs4 import BeautifulSoup

def scrape_books():
    base_url = "http://books.toscrape.com/"
    books = []

    try:
        response = requests.get(base_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        book_containers = soup.find_all('article', class_='product_pod')

        for book in book_containers:
            title = book.h3.a['title']
            price = book.find('p', class_='price_color').text
            availability = book.find('p', class_='instock availability').text.strip()

            books.append({
                'title': title,
                'price': price,
                'availability': availability
            })

        print(f"Scraped {len(books)} books from {base_url}:\n")
        for i, book in enumerate(books, 1):
            print(f"{i}. {book['title']} - {book['price']} ({book['availability']})")

    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch the webpage: {e}")

scrape_books()
