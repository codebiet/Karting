from bs4 import BeautifulSoup
import requests

def get_url(search_term):
    template= 'https://www.shopclues.com/search?q={}&sc_z=1111&z=0&count=10&user_id=&user_segment=default'
    search_term= search_term.replace(' ','%20')
    url_f= template.format(search_term)
    return url_f

def extract_record(term):
    try:
        title= term.h2.text.strip()
        description= ''
        link= 'https:'+ term.a.get('href')
    except AttributeError:
        return
    
    try:
        atag= term.find('div','ori_price')
        price= atag.find('span','p_price').text.strip()
        disc= atag.find('span','prd_discount').text.strip()
        atag3= term.find('div','old_prices')
        discprice= atag3.find('span').text.strip()
    except AttributeError:
        price=''
        disc=''
        discprice=''
    
    image= term.img.get('src')

    results=(title, description,link,price,discprice,disc,image)

    return results





product= input('ENTER THE PRODECT')
url= get_url(product)
print(url)

record=[]

while(len(record)<=100):
    source= requests.get(url)
    soup= BeautifulSoup(source.content, 'html.parser')
    result= soup.find_all('div',{'class':'column col3 search_blocks'})

    for item in result:

        r= extract_record(item)
        print(r)
        if r:
            record.append(r)
