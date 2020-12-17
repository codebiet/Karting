from bs4 import BeautifulSoup
import requests

def get_url(search_term):
    temp = 'https://www.amazon.in/s?k={}&ref=nb_sb_noss'
    search_term = search_term.replace(' ', '+')
    url_f = temp.format(search_term)
    url_f += '&page{}'
    return url_f


def extract_record(items):
    try:
        atag = items.h5.span
        title = atag.text.strip()

    except AttributeError:
        title = ''
        atag = ''

    try:
        atag2 = items.h2.a
        description = atag2.text.strip()


    except AttributeError:
        atag2 = ''
        description = ''

    try:
        link = 'https://www.amazon.in/' + atag2.get('href')
    except AttributeError:
        return

    try:
        price_parent = items.find('span', 'a-price')
        price = price_parent.find('span', 'a-offscreen').text
    except AttributeError:
        return

    try:
        og_price_parent = items.find('span', 'a-price a-text-price')
        og_price = og_price_parent.find('span', 'a-offscreen').text
    except AttributeError:
        og_price = ''
    try:
        disc = items.find('span', 'a-color-price').text
    except AttributeError:
        disc = ''

    try:
        rating = items.i.text
    except AttributeError:
        rating = ''

    img = items.img.get('src')

    results = (title, description, link, price, og_price, disc, rating, img)
    return results


# driver= webdriver.Chrome(executable_path= r'C:\Users\Shivangi\Desktop\WebScrapping\chromedriver.exe')

product = input(">>>")
url = get_url(product)
# print(url)

record = []

for page in range(1, 2):
    source = requests.get(url.format(page))
    soup = BeautifulSoup(source.content, 'html.parser')
    result = soup.find_all('div', {'data-component-type': 's-search-result'})

    for item in result:

        r = extract_record(item)
        # print(r)
        if r:
            record.append(r)