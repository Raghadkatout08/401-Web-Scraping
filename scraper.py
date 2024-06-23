import requests 
from bs4 import BeautifulSoup
import json

def extract_books(category_url):

    response = requests.get(category_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    category_name = soup.find('div', class_='page-header').text.strip() if soup.find('div', class_='page-header') else "Unknown Category"

    books_list = []

    books = soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')

    for book in books:
        title = book.find('h3').find('a')['title'] if book.find('h3') and book.find('h3').find('a') else "No Title"
        rating = book.find('p', class_='star-rating')['class'][1] if book.find('p', class_='star-rating') else "No Rating"
        price = book.find('p', class_='price_color').text.strip() if book.find('p', class_='price_color') else "No Price"
        availability = book.find('p', class_='instock availability').text.strip() if book.find('p', class_='instock availability') else "No Availability"
        availability = ' '.join(availability.split())

        books_list.append({
            'title': title,
            'rating': rating,
            'price': price,
            'availability': availability
        })

    return {"type": category_name, "data": books_list}

def main():
    category_urls = {
        "Sequential Art": "https://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html",
        "Fiction": "https://books.toscrape.com/catalogue/category/books/fiction_10/index.html",
        "Fantasy": "https://books.toscrape.com/catalogue/category/books/fantasy_19/index.html"
    }

    all_books_data = []

    for category, url in category_urls.items():
        books_data = extract_books(url)
        all_books_data.append(books_data)

    with open('json_data.json', 'w') as json_file:
        json.dump(all_books_data, json_file, indent=2)


def count_books_by_rating(data, rating):
    return sum(1 for category in data for book in category['data'] if book['rating'] == rating)


if __name__ == "__main__":
    main()

    with open('json_data.json', 'r') as file:
        books_data = json.load(file)


    rating_count = count_books_by_rating(books_data, "Five")
    print(f"Number of books with a Five stars rating: {rating_count}")