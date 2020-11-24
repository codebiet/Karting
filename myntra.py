from bs4 import BeautifulSoup
import requests

def get_url(search_term):
    template= 'https://www.myntra.com/{}'
    search_term= search_term.replace(' ','-')
    url_f= template.format(search_term)
    url_f+= '?p={}'
    return url_f

def extract_record(term):

    atag= term.find('div', 'product-productMetaInfo')
    title= atag.h3.text.strip()

    atag2= atag.find('h4','product-product')
    description= atag2.text.strip()

    link = 'https://www.myntra.com/'+ term.a.get('href')

    try:
        image= term.img.get('src')        
    except AttributeError:
        return

    

    try:
        atag3= term.find('div','product-price')
        price= atag3.find('span','product-discountedPrice').text.strip()

        
    except AttributeError:
        return

    
    try:
        discprice= atag3.find('span','product-strike').text.strip()
        disc= atag3.find('span','product-discountPercentage').text.strip()
    except AttributeError:
        disc=''
        discprice=''
    

    results= (title, description,link,price, discprice,disc,image)
    return results



product= input('ENTER THE PRODUCT OF YOUR CHOICE')
url= get_url(product)
print(url)
    
record=[]

for page in range(1,2):
    source= requests.get(url.format(page))
    soup= BeautifulSoup(source.content, 'html.parser')
    result= soup.find_all('li',{'class':'product-base'})

    for item in result:

        r= extract_record(item)
        print(r)
        if r:
            record.append(r)












