import requests
from bs4 import BeautifulSoup

url = "https://bauskasdzive.lv/kategorija/vietejas-zinas/"
response = requests.get(url)


soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all('div', class_='post')

print(f"Found {len(articles)} articles.\n")

for i, article in enumerate(articles, start=1):
    title_tag = article.find('h2', class_='entry-title')
    if title_tag:
        a_tag = title_tag.find('a')
        if a_tag and a_tag['href']:
            title = a_tag.get_text(strip=True)
            link = a_tag['href']

            print(f"{i}. {title}")
            print(f"URL: {link}")

            article_response = requests.get(link)
            article_soup = BeautifulSoup(article_response.text, "html.parser")

            paragraphs = article_soup.find_all('p')

            print("   Saturs:")
            filter = [
                "Jūsu e-pasta adrese netiks publicēta.Obligātie lauki ir atzīmēti kā*",
                "Komentārs*",
                "Vārds",
                "E-pasts",
                "Tīmekļa vietne",
                "Saglabājiet manu vārdu, e-pasta adresi un vietni šajā pārlūkprogrammā nākamajai reizei, kad vēlēšos pievienot komentāru."
            ]

            for para in paragraphs:
                text = para.get_text(strip=True)
                if text and text not in filter:
                    print(f"      {text}")

            print(" ")
