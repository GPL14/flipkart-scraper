import requests
from bs4 import BeautifulSoup
from db_config import connect_db

search_url = "https://www.flipkart.com/search?q=mobile+phones"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

response = requests.get(search_url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

conn = connect_db()
cursor = conn.cursor()

products = soup.find_all("div", class_="_1AtVbE")

for item in products:
    name_tag = item.find("div", class_="_4rR01T")
    price_tag = item.find("div", class_="_30jeq3")
    rating_tag = item.find("div", class_="._3LWZlK")

    if name_tag and price_tag:
        name = name_tag.get_text(strip=True)
        price = price_tag.get_text(strip=True)
        rating = rating_tag.get_text(strip=True) if rating_tag else "N/A"

        cursor.execute(
            "INSERT INTO products (name, price, rating) VALUES (%s, %s, %s)",
            (name, price, rating)
        )

conn.commit()
cursor.close()
conn.close()

print("✅ Scraping complete. Data saved to MySQL.")
