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

# List file
Quangninh_f = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_traveloka\\data_url\\QuangNinh_url.txt"
Quangninh_s = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_traveloka\\detail_data\\data_again\\Quangninh.csv"

Dalat_f = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_traveloka\\data_url\\DaLat_url.txt"
Dalat_s = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_traveloka\\detail_data\\data_again\\Dalat.csv"

Danang_f = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_traveloka\\data_url\\Danang_list_1.txt"
Danang_s = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_traveloka\\detail_data\\data_again\\Danang.csv"

Hanoi_f = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_traveloka\\data_url\\Hanoi_list_1.txt"
Hanoi_s = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_traveloka\\detail_data\\data_again\\Hanoi.csv"

HoChiMinh_f = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_traveloka\\data_url\\HoChiMinh_list_1.txt"
HoChiMinh_s = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_traveloka\\detail_data\\data_again\\HoChiMinh.csv"

Nhatrang_f = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_traveloka\\data_url\\NhaTrang_url.txt"
Nhatrang_s = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_traveloka\\detail_data\\data_again\\Nhatrang.csv"

Phuquoc_f = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_traveloka\\data_url\\PhuQuoc_url.txt"
Phuquoc_s = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_traveloka\\detail_data\\data_again\\Phuquoc.csv"

Vungtau_f = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_traveloka\\data_url\\VungTau_url.txt"
Vungtau_s = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_traveloka\\detail_data\\data_again\\Vungtau.csv"

Halong_f = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_traveloka\\data_url\\HaLong_url.txt"
Halong_s = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_traveloka\\detail_data\\data_again\\Halong.csv"


def scrollToEnd(driver):
    page = driver.find_element(by=By.TAG_NAME, value="html")
    page.send_keys(Keys.END)
    sleep(5)


def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1


# driver = webdriver.Chrome(service=Service(
#     ChromeDriverManager().install()), options=options)


def crawl_from_url(url, ten_tinh):
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=options)
    driver.get(url)
    sleep(5)

    # Ten thanh pho
    hotel_city = ten_tinh

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


def save2csv(file_dir, save_dir, ten_tinh):
    records = []
    with open(file_dir) as f:
        for line in f:
            try:
                records.append(crawl_from_url(line, ten_tinh))
            except:
                pass

    df = pd.DataFrame(data=records, columns=['City', 'Hotel name', 'Image', 'Url', 'Address', 'Stars', 'Min Price',
                                             'Rating', 'Number of reviews', 'Reviews', 'Facilities', 'Description', 'Nearby places'])
    df.to_csv(save_dir, index=False, encoding='utf8')
    print("So ban ghi la: " + str(len(records)))


# print(Dalat_f, '\n', Dalat_s)
# print(Danang_f, '\n', Danang_s)
# print(Hanoi_f, '\n', Hanoi_s)
# print(HoChiMinh_f, '\n', HoChiMinh_s)
# print(Nhatrang_f, '\n', Nhatrang_s)
# print(Phuquoc_f, '\n', Phuquoc_s)
# print(Quangninh_f, '\n', Quangninh_s)
# print(Vungtau_f, '\n', Vungtau_s)

# print("Bat dau crawl: \n")
# print("\n==================\n")
# print("Da Lat:")
# save2csv(Dalat_f, Dalat_s, "Đà Lạt")
# print("Het Da Lat!!!\n==============\n")
# sleep(5)

# print("Da Nang:")
# save2csv(Danang_f, Danang_s, "Đà Nẵng")
# print("Het Da Nang!!!\n==============\n")
# sleep(5)

# print("Ho Chi Minh:")
# save2csv(HoChiMinh_f, HoChiMinh_s, "Hồ Chí Minh")
# print("Het Ho Chi Minh!!!\n==============\n")
# sleep(5)

# print("Vung Tau:")
# save2csv(Vungtau_f, Vungtau_s, "Vũng Tàu")
# print("Het Vung Tau!!!\n==============\n")
# sleep(5)

# print("Quang Ninh:")
# save2csv(Quangninh_f, Quangninh_s, "Quảng Ninh")
# print("Het Quang Ninh!!!\n==============\n")
# sleep(5)

# print("Nha Trang:")
# save2csv(Nhatrang_f, Nhatrang_s, "Nha Trang")
# print("Het Nha Trang!!!\n==============\n")
# sleep(5)

# print("Ha Noi:")
# save2csv(Hanoi_f, Hanoi_s, "Hà Nội")
# print("Het Ha Noi!!!\n==============\n")
# sleep(5)

# print("Phu Quoc:")
# save2csv(Phuquoc_f, Phuquoc_s, "Phú Quốc")
# print("\n----------------------\n")

print("Ha Long:")
save2csv(Halong_f, Halong_s, "Hạ Long")
