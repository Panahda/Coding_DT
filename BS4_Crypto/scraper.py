from url import url
from bs4 import BeautifulSoup
import requests
import time


def find_user_input():
    user_input = True
    user_list = []
    counter = 1
    print("ur cryto(s), input 'end' to stop")
    while user_input:
        inp = input(f'>{counter}. ').upper()
        counter += 1
        if inp == 'END':
            user_input = False
            print(f"Filtering {user_list}")
            return user_list
        else:
            user_list.append(inp)


def find_crypto(ulist):
    html_text = requests.get(url).text
    # print(html_text)
    soup = BeautifulSoup(html_text, 'lxml')
    cryptos = soup.find_all('a', class_='_1dSou6YbrT4POv2E7HhT6L _1xXfNLFwNTyQ6I-5fxKNSI')
    for index, crypto in enumerate(cryptos):
        crypto_full = crypto.find('h2').text
        crypto_tag = crypto.find('span', class_='ef9HsjqnGRgxFmqbXxd0e').text

        crypto_name = crypto_full.replace(crypto_tag, '')
        crypto_price = crypto.find('span', class_='_3XNm6CSrchU-MNbu1Zh3m2').text
        crypto_diff = crypto.find('span', class_='color-short').text
        more_info = url + crypto['href']

        for i in ulist:
            if i in crypto_name.upper():
                with open(f'results/{index}_{crypto_name}.txt', 'w') as f:
                    f.write(f'{crypto_tag}: {crypto_name} \n')
                    f.write(f'{crypto_price} {crypto_diff} \n')
                    f.write(f'for more info: {more_info} \n')
                    print(f'File Saved {index}_{crypto_name}')


if __name__ == '__main__':
    u_list = find_user_input()
    while True:
        find_crypto(u_list)
        time_wait = 1
        print(f'waiting {time_wait}mins...')
        time.sleep(time_wait * 60)
