from django.shortcuts import render
from . import forms, models
from bs4 import BeautifulSoup
import requests
from django.http import HttpResponseRedirect
from .models import Search
from django.shortcuts import redirect

# Create your views here.


def get_url_shopclues(search_term):
    template = 'https://www.shopclues.com/search?q={}&sc_z=1111&z=0&count=10&user_id=&user_segment=default'
    search_term = str(search_term).replace('<QuerySet [<Search: ', '%20')
    search_term = search_term.replace(">]>", "")
    url_f = template.format(search_term)
    return url_f

def extract_record_shopclues_link(term):
    try:
        title = term.h2.text.strip()
        description = ''
        link = 'https:' + term.a.get('href')
    except AttributeError:
        return
    return link


def extract_record_shopclues_desc(term):
    try:
        title = term.h2.text.strip()
        description = ''
        link = 'https:' + term.a.get('href')
    except AttributeError:
        return
    try:
        atag = term.find('div', 'ori_price')
        price = atag.find('span', 'p_price').text.strip()
        disc = atag.find('span', 'prd_discount').text.strip()
        atag3 = term.find('div', 'old_prices')
        discprice = atag3.find('span').text.strip()
    except AttributeError:
        price = ''
        disc = ''
        discprice = ''
    image = term.img.get('src')
    results = (title, description, link, price, discprice, disc, image)
    return title

def extract_record_shopclues_price(term):
    try:
        title = term.h2.text.strip()
        description = ''
        link = 'https:' + term.a.get('href')
    except AttributeError:
        return
    try:
        atag = term.find('div', 'ori_price')
        price = atag.find('span', 'p_price').text.strip()
        disc = atag.find('span', 'prd_discount').text.strip()
        atag3 = term.find('div', 'old_prices')
        discprice = atag3.find('span').text.strip()
    except AttributeError:
        price = ''
        disc = ''
        discprice = ''
    image = term.img.get('src')
    results = [title, description, link, price, discprice, disc, image]
    return price


def extract_record_shopclues_image(term):
    try:
        title = term.h2.text.strip()
        description = ''
        link = 'https:' + term.a.get('href')
    except AttributeError:
        return
    try:
        atag = term.find('div', 'ori_price')
        price = atag.find('span', 'p_price').text.strip()
        disc = atag.find('span', 'prd_discount').text.strip()
        atag3 = term.find('div', 'old_prices')
        discprice = atag3.find('span').text.strip()
    except AttributeError:
        price = ''
        disc = ''
        discprice = ''
    image = term.img.get('src')
    results = (title, description, link, price, discprice, disc, image)
    return image

def get_url_amazon(search_term):
    temp = 'https://www.amazon.in/s?k={}&ref=nb_sb_noss'
    search_term = str(search_term).replace('<QuerySet [<Search: ', '+')
    search_term = search_term.replace(">]>", "")
    url_f = temp.format(search_term)
    url_f += '&page{}'
    return url_f


def extract_record_amazon(items):
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
    results = [title, description, link, price, og_price, disc, rating, img]
    return (link)

def extract_record_amazon_img(items):
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
    return img


def extract_record_amazon_title(items):
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
    return title

def extract_record_amazon_price(items):
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
    return price

def get_url_myntra(search_term):
    template = 'https://www.myntra.com/{}'
    search_term = str(search_term).replace('<QuerySet [<Search: ', '-')
    search_term= search_term.replace('>]>', '')
    url_f = template.format(search_term)
    # url_f += '?p={}'
    return url_f


def extract_record_myntra(term):
    atag = term.find('div', 'product-productMetaInfo')
    title = atag.h3.text.strip()
    atag2 = atag.find('h4', 'product-product')
    description = atag2.text.strip()
    link = 'https://www.myntra.com/' + term.a.get('href')
    try:
        image = term.img.get('src')
    except AttributeError:
        return
    try:
        atag3 = term.find('div', 'product-price')
        price = atag3.find('span', 'product-discountedPrice').text.strip()
    except AttributeError:
        return
    try:
        discprice = atag3.find('span', 'product-strike').text.strip()
        disc = atag3.find('span', 'product-discountPercentage').text.strip()
    except AttributeError:
        disc = ''
        discprice = ''
    results = (title, description, link, price, discprice, disc, image)
    return link

                    ### VIEWS ###


def index(request):
    form1 = forms.SearchBar()
    if request.method == "POST":
        form1 = forms.SearchBar(request.POST)
        if form1.is_valid():
            # product = Search()
            product = (form1.cleaned_data['Search'])
            models.Search = product
            # product.save()
            # form1.save()
        return redirect(result)
    return render(request, 'karting/index.html', {'form1': form1})


def about(request):
    return render(request, r'karting/about.html')


def form_name_view(request):
    form = forms.FormName()
    if request.method == "POST":
        form = forms.FormName(request.POST)
        # if form.is_valid():
            # form.save()
            # obj_message = forms.FormName()
            # obj_message.Name = form.cleaned_data['Name']
            # obj_message.Email = form.cleaned_data['Email']
            # obj_message.Contact = form.cleaned_data['Contact']
            # obj_message.Message = form.cleaned_data['Message']
            # obj_message.save()

        # do something code

    return render(request, 'karting/contact.html', {'form': form})


def result(request):
    product = models.Search
    url = get_url_shopclues(product)
    record_shopclues = []
    while (len(record_shopclues) <= 1):
        source = requests.get(url)
        soup = BeautifulSoup(source.content, 'html.parser')
        result = soup.find_all('div', {'class': 'column col3 search_blocks'})
        for item in result:
            r = extract_record_shopclues_link(item)
            record_shopclues.append(r)

    record_desc_shopclues=[]
    while (len(record_desc_shopclues) <= 1):
        source_desc = requests.get(url)
        soup_desc = BeautifulSoup(source_desc.content, 'html.parser')
        result_desc = soup_desc.find_all('div', {'class': 'column col3 search_blocks'})
        for itemdec in result_desc:
            r_desc = extract_record_shopclues_desc(itemdec)
            record_desc_shopclues.append(r_desc)

    record_price_shopclues=[]
    while (len(record_price_shopclues) <= 1):
        source_price = requests.get(url)
        soup_price = BeautifulSoup(source_price.content, 'html.parser')
        result_price = soup_price.find_all('div', {'class': 'column col3 search_blocks'})
        for itemprice in result_price:
            r_price = extract_record_shopclues_price(itemprice)
            record_price_shopclues.append(r_price)

    record_image_shopclues=[]
    while (len(record_image_shopclues) <= 1):
        source_image = requests.get(url)
        soup_image = BeautifulSoup(source_image.content, 'html.parser')
        result_image = soup_image.find_all('div', {'class': 'column col3 search_blocks'})
        for itemimage in result_image:
            r_image = extract_record_shopclues_image(itemimage)
            record_image_shopclues.append(r_image)
   
    # url1 = get_url_myntra(product)
    # print(url1)
    # record_myntra = []
    # for page in range(1, 2):
    #     source1 = requests.get(url1.format(page))
    #     soup1 = BeautifulSoup(source.content, 'html.parser')
    #     result1 = soup1.find_all('li', {'class': 'product-base'})
    #     print(result1)
    #     for item1 in result1:
    #         r1 = extract_record_myntra(item1)
    #         record_myntra.append(r1)

    url2 = get_url_amazon(product)
    record_amazon = []
    for page1 in range(1,2):
        source2 = requests.get(url2.format(page1))
        soup2 = BeautifulSoup(source2.content, 'html.parser')
        result2 = soup2.find_all('div', {'data-component-type': 's-search-result'})
        for item2 in result2:
            r2 = extract_record_amazon(item2)
            if r2:
                record_amazon.append(r2)
    print(f' LENGTH OF record_amazon IS {len(record_amazon)}')
    record_amazon_title = []
    for page_title in range(1,2):
        source_title_amazon = requests.get(url2.format(page_title))
        soup_title_amazon = BeautifulSoup(source_title_amazon.content, 'html.parser')
        result_title_amazon = soup_title_amazon.find_all('div', {'data-component-type': 's-search-result'})
        for item_title_amazon in result_title_amazon:
            r_amazon_title = extract_record_amazon_title(item_title_amazon)
            if r_amazon_title:
                record_amazon_title.append(r_amazon_title)
    print(f' LENGTH OF record_amazon_title IS {len(record_amazon_title)}')

    record_amazon_img = []
    for page_img in range(1,2):
        source_img_amazon = requests.get(url2.format(page_img))
        soup_img_amazon = BeautifulSoup(source_img_amazon.content, 'html.parser')
        result_img_amazon = soup_img_amazon.find_all('div', {'data-component-type': 's-search-result'})
        for item_img_amazon in result_img_amazon:
            r_amazon_img = extract_record_amazon_img(item_img_amazon)
            if r_amazon_img:
                record_amazon_img.append(r_amazon_img)

    record_amazon_price = []
    for page_price in range(1,2):
        source_price_amazon = requests.get(url2.format(page_price))
        soup_price_amazon = BeautifulSoup(source_price_amazon.content, 'html.parser')
        result_price_amazon = soup_price_amazon.find_all('div', {'data-component-type': 's-search-result'})
        for item_price_amazon in result_price_amazon:
            r_amazon_price = extract_record_amazon_price(item_price_amazon)
            if r_amazon_price:
                record_amazon_price.append(r_amazon_price)
        
    context_dict = {
        'record_shopclues':[i for i in ((record_shopclues))],
        'record_desc_shopclues':[k for k in record_desc_shopclues],
        'record_price_shopclues':(record_price_shopclues),
        'record_image_shopclues':[i for i in record_image_shopclues],
        'record_amazon':[j for j in (record_amazon)],
        'record_amazon_title':[i for i in record_amazon_title],
        'extract_record_amazon_img':[i for i in record_amazon_img],
        'record_amazon_price':[i for i in record_amazon_price],
    }

    zipped=zip(record_shopclues, record_image_shopclues, record_price_shopclues
            , record_desc_shopclues)
    zipped2 = zip(record_amazon, record_amazon_img, record_amazon_price, 
        record_amazon_title)

    context_data = {'zipped':zipped, 'zipped2':zipped2}
    return render(request, 'karting/re1.html', context= context_data )
