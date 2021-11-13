from bs4 import BeautifulSoup
import requests
from url import my_url

# print(my_url) - debugging purposes

html_text = requests.get(my_url).text
# print(html_text)
# show html(txt)

soup = BeautifulSoup(html_text, 'lxml')
products = soup.find_all('div', class_='col-md-4 country')

# print(product)

count = 0

# text.replace(" ", ""): removes spaces, strip(): removes empty lines
for product in products:
    count += 1
    country_name = product.find('h3', class_='country-name').text.replace(' ', '').strip()
    country_capital = product.find('span', class_='country-capital').text
    country_population = product.find('span', class_='country-population').text
    print(f'''{count}.country: {country_name}
        capital: {country_capital}
        population: {country_population}
''')

