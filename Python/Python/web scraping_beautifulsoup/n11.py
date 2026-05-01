import requests
from bs4 import BeautifulSoup

url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar"
urun_url="https://www.n11.com"

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"
}

html = requests.get(url, headers=headers).content

soup = BeautifulSoup(html, "html.parser")

liste = soup.find("div", {"class":"searchResults twoColumns"}).find_all("a",{"class":"product-item"},limit=20)

count = 1
images = []
for ahref in liste:
    link = urun_url + ahref.get("href")
    p_name = ahref.find("div",{"class":"product-text-area"}).find("div", {"class":"product-item-title two-lines"}).text
    slider_divs= ahref.find("div",{"class":"swiper-wrapper"}).find_all("div")
    for div in slider_divs:
       img= div.find("img")
       images.append(img.get("data-src"))
 
    # price = li.find("div", {"class":"priceContainer"}).find_all("span")[-1].ins.text.strip("TL")
    price_area= ahref.find("div",{"class":"product-text-area"}).find("div", {"class":"price-area"})
    if(price_area.find("div",{"class":"price"})) !=None:
        price=price_area.find("div",{"class":"price"}).text
    else:
        price=price_area.find("div",{"class":"price-currency"}).text

    print(f"{count}. ürün ismi {p_name} fiyat: {price}")
    count += 1
