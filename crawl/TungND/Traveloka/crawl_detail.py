from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import csv
import re
import pandas as pd

options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument("start-maximized")
options.add_argument('disable-infobars')

file_dir = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_traveloka\\QuangNinh_list.txt"

save_dir = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_traveloka\\QuangNinh_save.csv"

# url_demo = "https://www.traveloka.com/vi-vn/hotel/vietnam/the-imperial-hotel-1000000324420?spec=16-07-2022.17-07-2022.1.1.HOTEL.1000000324420.The%20Imperial%20Hotel.1&prevSearchId=1736532113590611070&loginPromo=1&contexts=%7B%22inventoryRateKey%22%3A%22povEwB3ZzsU2C6pd%2B6MdUwKh3BcjHsHvQbV0EUcyDRFM0tKsNUio4Rxug1zOzHJilcvZa8YdqqIySdppe7dolTIewZlxfjiOGz6oXLTucMvN0%2BgQ3yZPvZcoHwUFNN%2BZpcr%2F%2FNa8o9ElfN8zOYhzzZeg0X586laFpeUViPi9rxC1qbrARRWTiiHXJle6iNv0IvEWeildVo7nbHxIWcXPVNGysXwP9P%2F6jQTjnyKeTv%2ByqYmxSenRKFEfSHS0XO3ksOocFaHL1Wb9vQXntcm%2BDw%3D%3D%22%7D"

# url_demo_1 = "https://www.traveloka.com/vi-vn/hotel/vietnam/kim-ngan-hotel-9000000793148?spec=16-07-2022.17-07-2022.1.1.HOTEL.9000000793148.Kim%20Ngan%20Hotel.1&prevSearchId=1736533476983728826&loginPromo=1&contexts=%7B%22inventoryRateKey%22%3A%22povEwB3ZzsU2C6pd%2B6MdU13LUNuufACdbU0usK5vg0dM0tKsNUio4Rxug1zOzHJilcvZa8YdqqIySdppe7dolTIewZlxfjiOGz6oXLTucMvN0%2BgQ3yZPvZcoHwUFNN%2BZpcr%2F%2FNa8o9ElfN8zOYhzzZeg0X586laFpeUViPi9rxDZ62WTwGC%2FZpx4qXTU45PMmhLDdV0WLeT%2FFKfQ0QL8LH02Dvlx%2F8PjYogEE5yzx6g6yOKyKeIDf7jO3GM45O1ok5sYzsZdVhL8yLD1ILOp6Q%3D%3D%22%7D"

# url_demo_2 = "https://www.traveloka.com/vi-vn/hotel/vietnam/lenid-hotel-nha-trang-3000020001694?spec=16-07-2022.17-07-2022.1.1.HOTEL.3000020001694.Lenid%20Hotel%20Nha%20Trang.1&prevSearchId=1736535664842790868&loginPromo=1&contexts=%7B%22inventoryRateKey%22%3A%22povEwB3ZzsU2C6pd%2B6MdU13LUNuufACdbU0usK5vg0dM0tKsNUio4Rxug1zOzHJilcvZa8YdqqIySdppe7dolTIewZlxfjiOGz6oXLTucMvN0%2BgQ3yZPvZcoHwUFNN%2BZpcr%2F%2FNa8o9ElfN8zOYhzzZeg0X586laFpeUViPi9rxA9PbipD9rvRO5PVWTWBx5TIvEWeildVo7nbHxIWcXPVNGysXwP9P%2F6jQTjnyKeTv%2ByqYmxSenRKFEfSHS0XO3ksOocFaHL1Wb9vQXntcm%2BDw%3D%3D%22%7D"


def scrollToEnd(driver):
    page = driver.find_element(by=By.TAG_NAME, value="html")
    page.send_keys(Keys.END)
    sleep(5)

# Function to convert


def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1


# driver = webdriver.Chrome(service=Service(
#     ChromeDriverManager().install()), options=options)


def crawl_from_url(url):
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=options)
    driver.get(url)
    sleep(5)

    # Ten thanh pho
    hotel_city = "Quảng Ninh"
    # print(hotel_city)
    # print("\n============================\n")
    # Ten khach san
    hotel_name = driver.find_element(By.TAG_NAME, 'h1').text
    # print(hotel_name)
    # print("\n============================\n")
    # Url
    # print(url)
    # print("\n============================\n")
    # Dia chi
    try:
        hotel_address = driver.find_element(
            By.CSS_SELECTOR, 'div[class="css-901oao r-1ud240a r-1sixt3s r-1b43r93 r-majxgm r-rjixqe r-13hce6t r-fdjqy7"]').text
    except:
        hotel_address = driver.find_element(
            By.CSS_SELECTOR, 'div[class="css-901oao r-1sixt3s r-1b43r93 r-majxgm r-rjixqe r-13hce6t r-fdjqy7"]').text
    # print(hotel_address)
    # print("\n============================\n")
    # So sao khach san
    stars = driver.find_elements(By.CSS_SELECTOR, '#__next > div:nth-child(5) > div.css-1dbjc4n.r-1jgb5lz.r-1r5su4o.r-uwe93p.r-pezta > div > div:nth-child(3) > div > div:nth-child(1) > div > div.css-1dbjc4n.r-1habvwh.r-18u37iz.r-1wtj0ep > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-5oul0u > div:nth-child(2) > div > div > img')
    hotel_star = len(stars)
    # print(hotel_star)
    # print("\n============================\n")
    # Gia phong nho nhat
    scrollToEnd(driver)
    try:
        hotel_min_price = driver.find_element(
            By.CSS_SELECTOR, 'div[class="css-901oao r-173mn98 r-1sixt3s r-b88u0q r-135wba7 r-fdjqy7"]').text
    except:
        hotel_min_price = driver.find_element(
            By.CSS_SELECTOR, 'div[class="css-901oao r-173mn98 r-1sixt3s r-1i10wst r-b88u0q r-135wba7 r-fdjqy7"]').text
    # print(hotel_min_price)
    # print("\n============================\n")
    # Rating
    scrollToEnd(driver)
    try:
        hotel_rating = driver.find_element(By.CSS_SELECTOR, '#__next > div:nth-child(5) > div.css-1dbjc4n.r-14lw9ot > div > div > div:nth-child(1) > div > div > div:nth-child(1) > div.css-1dbjc4n.r-1awozwy.r-6koalj.r-18u37iz > div.css-1dbjc4n.r-ymttw5.r-rjfia > div > div.css-1dbjc4n.r-14lw9ot.r-143h623.r-sdzlij.r-7d3vna.r-oebo59.r-1ifxtd0.r-1udh08x.r-tuq35u.r-1xy5wl5 > div > div').text
    except:
        hotel_rating = 0
    # print(hotel_rating)
    # print("\n============================\n")
    # Nums of reviews
    if hotel_rating == 0:
        hotel_num_of_reviews = 0
    else:
        number_of_reviews = driver.find_element(
            By.CSS_SELECTOR, '#__next > div:nth-child(5) > div.css-1dbjc4n.r-1jgb5lz.r-1r5su4o.r-uwe93p.r-pezta > div > div:nth-child(3) > div > div:nth-child(1) > div > div:nth-child(9) > div.css-1dbjc4n.r-1oszu61.r-eqz5dr > div.css-901oao.r-1sixt3s.r-ubezar.r-majxgm.r-135wba7.r-fdjqy7').text
        hotel_num_of_reviews = listToString(
            re.findall(r"\d+", number_of_reviews))
    # print(hotel_num_of_reviews)
    # print("\n============================\n")
    if hotel_num_of_reviews == 0:
        hotel_reviews_list = []
    else:
        hotel_reviews_list = []
        rv = driver.find_elements(
            By.CSS_SELECTOR, 'div[itemprop="reviewBody"]')
        for r in rv:
            hotel_reviews_list.append(r.text)
    # print(hotel_reviews_list)
    # print("\n============================\n")
    # Facilities
    hotel_facilities = []
    demo = driver.find_elements(
        By.CSS_SELECTOR, 'div[class="css-1dbjc4n r-18u37iz r-1wtj0ep r-ymttw5"]')
    for f in demo:
        hotel_facilities.append(f.text)
    # hotel_facilities = hotel_facilities[0].split("\n")
    # print(hotel_facilities)
    # print("\n============================\n")
    # Ảnh
    hotel_list_image = []
    list_image = driver.find_elements(
        by=By.CSS_SELECTOR, value="div[class='css-1dbjc4n r-u8s1d'] > img")
    for image in list_image:
        try:
            hotel_list_image.append(image.get_attribute('src'))
        except:
            pass
    # print(hotel_list_image)
    # print("\n============================\n")
    # Description
    des = driver.find_elements(
        By.CSS_SELECTOR, '#__next > div:nth-child(5) > div.css-1dbjc4n.r-14lw9ot > div > div > div.css-1dbjc4n.r-1oszu61.r-eqz5dr > div:nth-child(3) > div.css-1dbjc4n.r-12hfotv > div.css-1dbjc4n.r-1udh08x > div > div')
    hotel_description = []
    for d in des:
        hotel_description.append(d.text)
    # hotel_description = hotel_description[0].split("\n")
    # print(hotel_description)
    # print(len(hotel_description))
    # print("\n============================\n")
    # Near places
    pls = driver.find_elements(
        By.CSS_SELECTOR, 'div.css-901oao.r-1sixt3s.r-1b43r93.r-b88u0q.r-rjixqe.r-15zivkp.r-fdjqy7')
    dis = driver.find_elements(
        By.CSS_SELECTOR, 'div.css-901oao.r-1sixt3s.r-1b43r93.r-majxgm.r-rjixqe.r-fdjqy7.r-3s2u2q')
    hotel_near_places = []
    for i in range(len(pls)):
        hotel_near_places.append((pls[i].text, dis[i].text))
    # print(hotel_near_places)
    # print("\n============================\n")
    driver.close()

    return (
        hotel_city,
        hotel_name,
        hotel_list_image,
        url,
        hotel_address,
        hotel_star,
        hotel_min_price,
        hotel_rating,
        hotel_num_of_reviews,
        hotel_reviews_list,
        hotel_facilities,
        hotel_description,
        hotel_near_places
    )

# m = crawl_from_url(url_demo)
# print(m)


records = []
# checkLine = []
with open(file_dir) as f:
    for line in f:
        # checkLine.append(line)
        # m = crawl_from_url(line)
        # records.append(m)
        try:
            records.append(crawl_from_url(line))
        except:
            pass

df = pd.DataFrame(data=records, columns=['City', 'Hotel name', 'Image', 'Url', 'Address', 'Stars', 'Min Price',
                  'Rating', 'Number of reviews', 'Reviews', 'Facilities', 'Description', 'Nearby places'])
df.to_csv(save_dir, index=False, encoding='utf8')
# print(records)
# print("\n")
# print(len(records))
# print(len(checkLine))
