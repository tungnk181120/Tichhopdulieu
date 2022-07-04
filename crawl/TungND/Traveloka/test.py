from cgitb import text
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

file_dir = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_traveloka\\data_url\\demo.txt"

save_dir = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_traveloka\\demo_list.csv"

url_demo = "https://www.traveloka.com/vi-vn/hotel/vietnam/paradise-elegance-cruise-1000000577244?spec=16-07-2022.17-07-2022.1.1.HOTEL.1000000577244.Du%20thuy%E1%BB%81n%20Paradise%20Elegance.1&prevSearchId=1736844481457578522&loginPromo=1&contexts=%7B%22inventoryRateKey%22%3A%22UBh6NEbrm3oRvPz965TEQYx6yJl1TnvT4YG%2Byjorw5RM0tKsNUio4Rxug1zOzHJilcvZa8YdqqIySdppe7dolTIewZlxfjiOGz6oXLTucMvN0%2BgQ3yZPvZcoHwUFNN%2BZpcr%2F%2FNa8o9ElfN8zOYhzzZeg0X586laFpeUViPi9rxCFtrSDsu208k0kdESQK1DTyHKWIZ1BQohM1LtP1iyp%2BvzU1DzhU0%2FYDjP46sAdpc7BKHpZT7ZDw0m5A93dWTzye%2BWHaI%2FRSlAE%2FUnrAjXp4A%3D%3D%22%7D"

url_demo_1 = "https://www.traveloka.com/vi-vn/hotel/vietnam/mong-cai-trade-union-hotel-3000020006436?spec=16-07-2022.17-07-2022.1.1.HOTEL.3000020006436.Kha%CC%81ch%20sa%CC%A3n%20C%C3%B4ng%20%C4%90oa%CC%80n%20Mo%CC%81ng%20Ca%CC%81i.1&prevSearchId=1736844515235363655&loginPromo=1&contexts=%7B%22inventoryRateKey%22%3A%22povEwB3ZzsU2C6pd%2B6MdU13LUNuufACdbU0usK5vg0dM0tKsNUio4Rxug1zOzHJilcvZa8YdqqIySdppe7dolTIewZlxfjiOGz6oXLTucMvN0%2BgQ3yZPvZcoHwUFNN%2BZpcr%2F%2FNa8o9ElfN8zOYhzzZeg0X586laFpeUViPi9rxAIkohi4u7xG7rsXyZPwrFnIvEWeildVo7nbHxIWcXPVNGysXwP9P%2F6jQTjnyKeTv%2ByqYmxSenRKFEfSHS0XO3ksOocFaHL1Wb9vQXntcm%2BDw%3D%3D%22%7D"

url_demo_2 = "https://www.traveloka.com/vi-vn/hotel/vietnam/tung-luxury-hotel-9000000755717?spec=16-07-2022.17-07-2022.1.1.HOTEL.9000000755717.Tung%20Luxury%20Hotel.1&prevSearchId=1736844288645430286&loginPromo=1&contexts=%7B%22inventoryRateKey%22%3A%22povEwB3ZzsU2C6pd%2B6MdU13LUNuufACdbU0usK5vg0dM0tKsNUio4Rxug1zOzHJilcvZa8YdqqIySdppe7dolTIewZlxfjiOGz6oXLTucMvN0%2BgQ3yZPvZcoHwUFNN%2BZpcr%2F%2FNa8o9ElfN8zOYhzzZeg0X586laFpeUViPi9rxAu5NABrHBm2aRMdJjU8x26IvEWeildVo7nbHxIWcXPVNGysXwP9P%2F6jQTjnyKeTv%2ByqYmxSenRKFEfSHS0XO3ksOocFaHL1Wb9vQXntcm%2BDw%3D%3D%22%7D"

url_demo_3 = "https://www.traveloka.com/vi-vn/hotel/vietnam/anh-dao-guest-house-3000010028777?spec=16-07-2022.17-07-2022.1.1.HOTEL.3000010028777.Anh%20Dao%20Guest%20House.1&prevSearchId=1736844288645430286&loginPromo=1&contexts=%7B%22inventoryRateKey%22%3A%22povEwB3ZzsU2C6pd%2B6MdU13LUNuufACdbU0usK5vg0dM0tKsNUio4Rxug1zOzHJilcvZa8YdqqIySdppe7dolTIewZlxfjiOGz6oXLTucMvN0%2BgQ3yZPvZcoHwUFNN%2BZpcr%2F%2FNa8o9ElfN8zOYhzzZeg0X586laFpeUViPi9rxAu31scXuv2Pg5SAiDNDfkhIvEWeildVo7nbHxIWcXPVNGysXwP9P%2F6jQTjnyKeTv%2ByqYmxSenRKFEfSHS0XO3ksOocFaHL1Wb9vQXntcm%2BDw%3D%3D%22%7D"

url_demo_4 = "https://www.traveloka.com/vi-vn/hotel/vietnam/indochina-sails-cruise-1000000302743?spec=16-07-2022.17-07-2022.1.1.HOTEL.1000000302743.Du%20thuy%E1%BB%81n%20Indochina%20Sails.1&prevSearchId=1736844515235363655&loginPromo=1&contexts=%7B%22inventoryRateKey%22%3A%22povEwB3ZzsU2C6pd%2B6MdU13LUNuufACdbU0usK5vg0dM0tKsNUio4Rxug1zOzHJilcvZa8YdqqIySdppe7dolTIewZlxfjiOGz6oXLTucMvN0%2BgQ3yZPvZcoHwUFNN%2BZpcr%2F%2FNa8o9ElfN8zOYhzzZeg0X586laFpeUViPi9rxDdR3vsTGivIBc0tRq3GF81IvEWeildVo7nbHxIWcXPVNGysXwP9P%2F6jQTjnyKeTv%2ByqYmxSenRKFEfSHS0XO3ksOocFaHL1Wb9vQXntcm%2BDw%3D%3D%22%7D"

url_demo_5 = "https://www.traveloka.com/vi-vn/hotel/vietnam/ann-hotel-3000010035223?spec=16-07-2022.17-07-2022.1.1.HOTEL.3000010035223.Kha%CC%81ch%20sa%CC%A3n%20Ann.1&prevSearchId=1736844515235363655&loginPromo=1&contexts=%7B%22inventoryRateKey%22%3A%22povEwB3ZzsU2C6pd%2B6MdU13LUNuufACdbU0usK5vg0dM0tKsNUio4Rxug1zOzHJilcvZa8YdqqIySdppe7dolTIewZlxfjiOGz6oXLTucMvN0%2BgQ3yZPvZcoHwUFNN%2BZpcr%2F%2FNa8o9ElfN8zOYhzzZeg0X586laFpeUViPi9rxB%2FG2V6f0%2FO5XMb8kRwkR04mhLDdV0WLeT%2FFKfQ0QL8LH02Dvlx%2F8PjYogEE5yzx6g6yOKyKeIDf7jO3GM45O1ok5sYzsZdVhL8yLD1ILOp6Q%3D%3D%22%7D"

url_demo_6 = "https://www.traveloka.com/vi-vn/hotel/vietnam/indochina-sails-cruise-1000000302743?spec=16-07-2022.17-07-2022.1.1.HOTEL.1000000302743.Du%20thuy%E1%BB%81n%20Indochina%20Sails.1&prevSearchId=1736844515235363655&loginPromo=1&contexts=%7B%22inventoryRateKey%22%3A%22povEwB3ZzsU2C6pd%2B6MdU13LUNuufACdbU0usK5vg0dM0tKsNUio4Rxug1zOzHJilcvZa8YdqqIySdppe7dolTIewZlxfjiOGz6oXLTucMvN0%2BgQ3yZPvZcoHwUFNN%2BZpcr%2F%2FNa8o9ElfN8zOYhzzZeg0X586laFpeUViPi9rxDdR3vsTGivIBc0tRq3GF81IvEWeildVo7nbHxIWcXPVNGysXwP9P%2F6jQTjnyKeTv%2ByqYmxSenRKFEfSHS0XO3ksOocFaHL1Wb9vQXntcm%2BDw%3D%3D%22%7D"


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


driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=options)


def crawl_from_url(url):
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=options)
    driver.get(url)
    sleep(5)

    # Ten thanh pho
    hotel_city = "Quảng Ninh"

    # Ten khach san
    hotel_name = driver.find_element(By.TAG_NAME, 'h1').text

    # Url

    # Dia chi
    try:
        hotel_address = driver.find_element(
            By.CSS_SELECTOR, 'div[class="css-901oao r-1ud240a r-1sixt3s r-1b43r93 r-majxgm r-rjixqe r-13hce6t r-fdjqy7"]').text
    except:
        hotel_address = driver.find_element(
            By.CSS_SELECTOR, 'div[class="css-901oao r-1sixt3s r-1b43r93 r-majxgm r-rjixqe r-13hce6t r-fdjqy7"]').text

    # So sao khach san
    stars = driver.find_elements(By.CSS_SELECTOR, '#__next > div:nth-child(5) > div.css-1dbjc4n.r-1jgb5lz.r-1r5su4o.r-uwe93p > div > div:nth-child(3) > div > div:nth-child(1) > div > div.css-1dbjc4n.r-1habvwh.r-18u37iz.r-1wtj0ep > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-5oul0u > div:nth-child(2) > div > div > img')
    hotel_star = len(stars)

    # Gia phong nho nhat
    scrollToEnd(driver)
    try:
        hotel_min_price = driver.find_element(
            By.CSS_SELECTOR, 'div[class="css-901oao r-173mn98 r-1sixt3s r-b88u0q r-135wba7 r-fdjqy7"]').text
    except:
        hotel_min_price = driver.find_element(
            By.CSS_SELECTOR, 'div[class="css-901oao r-173mn98 r-1sixt3s r-1i10wst r-b88u0q r-135wba7 r-fdjqy7"]').text

    # Rating
    scrollToEnd(driver)
    try:
        hotel_rating = driver.find_element(By.CSS_SELECTOR, '#__next > div:nth-child(5) > div.css-1dbjc4n.r-14lw9ot > div > div > div:nth-child(1) > div > div > div:nth-child(1) > div.css-1dbjc4n.r-1awozwy.r-6koalj.r-18u37iz > div.css-1dbjc4n.r-ymttw5.r-rjfia > div > div.css-1dbjc4n.r-14lw9ot.r-143h623.r-sdzlij.r-7d3vna.r-oebo59.r-1ifxtd0.r-1udh08x.r-tuq35u.r-1xy5wl5 > div > div').text
    except:
        hotel_rating = 0

    # Nums of reviews
    try:
        txt = driver.find_element(By.CSS_SELECTOR, '#__next > div:nth-child(5) > div.css-1dbjc4n.r-1jgb5lz.r-1r5su4o.r-uwe93p > div > div:nth-child(3) > div > div:nth-child(1) > div > div:nth-child(9) > div.css-1dbjc4n.r-1oszu61.r-eqz5dr > div.css-901oao.r-1sixt3s.r-ubezar.r-majxgm.r-135wba7.r-fdjqy7').text
    except:
        txt = driver.find_element(By.CSS_SELECTOR, '#__next > div:nth-child(5) > div.css-1dbjc4n.r-1jgb5lz.r-1r5su4o.r-uwe93p > div > div:nth-child(3) > div > div:nth-child(1) > div > div:nth-child(7) > div.css-1dbjc4n.r-1oszu61.r-eqz5dr > div.css-901oao.r-1sixt3s.r-ubezar.r-majxgm.r-135wba7.r-fdjqy7').text
    if txt == "No reviews yet":
        hotel_num_of_reviews = 0
    else:
        tmp = re.findall(r'\d+', txt)
        tmp = list(map(int, tmp))
        hotel_num_of_reviews = tmp[0]

    if hotel_num_of_reviews == 0:
        hotel_reviews_list = []
    else:
        hotel_reviews_list = []
        rv = driver.find_elements(
            By.CSS_SELECTOR, 'div[itemprop="reviewBody"]')
        for r in rv:
            hotel_reviews_list.append(r.text)

    # Facilities
    hotel_facilities = []
    try:
        demo = driver.find_elements(
            By.CSS_SELECTOR, 'div[class="css-1dbjc4n r-18u37iz r-ymttw5"]')
    except:
        demo = driver.find_elements(
            By.CSS_SELECTOR, 'div[class="css-1dbjc4n r-18u37iz r-1wtj0ep r-ymttw5"]')
    for f in demo:
        hotel_facilities.append(f.text)
    hotel_facilities = hotel_facilities[0].split("\n")

    # Ảnh
    hotel_list_image = []
    list_image = driver.find_elements(
        by=By.CSS_SELECTOR, value="div[class='css-1dbjc4n r-u8s1d'] > img")
    for image in list_image:
        try:
            hotel_list_image.append(image.get_attribute('src'))
        except:
            pass

    # Description
    des = driver.find_elements(
        By.CSS_SELECTOR, 'div.css-1dbjc4n.r-12hfotv')
    res = []
    for d in des:
        res.append(d.text)

    m = res[0]
    hotel_description = m.replace('\nXem thêm', '')

    # Near places
    pls = driver.find_elements(
        By.CSS_SELECTOR, 'div.css-901oao.r-1sixt3s.r-1b43r93.r-b88u0q.r-rjixqe.r-15zivkp.r-fdjqy7')
    dis = driver.find_elements(
        By.CSS_SELECTOR, 'div.css-901oao.r-1sixt3s.r-1b43r93.r-majxgm.r-rjixqe.r-fdjqy7.r-3s2u2q')
    hotel_near_places = []
    for i in range(len(pls)):
        hotel_near_places.append((pls[i].text, dis[i].text))

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


records = []
with open(file_dir) as f:
    for line in f:
        try:
            records.append(crawl_from_url(line))
        except:
            pass

df = pd.DataFrame(data=records, columns=['City', 'Hotel name', 'Image', 'Url', 'Address', 'Stars', 'Min Price',
                  'Rating', 'Number of reviews', 'Reviews', 'Facilities', 'Description', 'Nearby places'])
# df = pd.DataFrame(data=records, columns=['Description'])
print(df)
df.to_csv(save_dir, index=False, encoding='utf8')


# driver = webdriver.Chrome(service=Service(
#     ChromeDriverManager().install()), options=options)
# driver.get(url_demo_1)
# sleep(5)


# driver.close()

# print(hotel_description)
# print(type(hotel_description))
