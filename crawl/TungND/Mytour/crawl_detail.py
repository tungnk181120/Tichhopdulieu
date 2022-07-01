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

# # List file
# Quangninh_f = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_traveloka\\data_url\\QuangNinh_url.txt"
# Quangninh_s = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_traveloka\\detail_data\\data_again\\Quangninh.csv"

# Dalat_f = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_traveloka\\data_url\\DaLat_url.txt"
# Dalat_s = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_traveloka\\detail_data\\data_again\\Dalat.csv"

# Danang_f = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_traveloka\\data_url\\Danang_list_1.txt"
# Danang_s = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_traveloka\\detail_data\\data_again\\Danang.csv"

# Hanoi_f = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_traveloka\\data_url\\Hanoi_list_1.txt"
# Hanoi_s = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_traveloka\\detail_data\\data_again\\Hanoi.csv"

# HoChiMinh_f = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_traveloka\\data_url\\HoChiMinh_list_1.txt"
# HoChiMinh_s = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_traveloka\\detail_data\\data_again\\HoChiMinh.csv"

# Nhatrang_f = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_traveloka\\data_url\\NhaTrang_url.txt"
# Nhatrang_s = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_traveloka\\detail_data\\data_again\\Nhatrang.csv"

# Phuquoc_f = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_traveloka\\data_url\\PhuQuoc_url.txt"
# Phuquoc_s = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_traveloka\\detail_data\\data_again\\Phuquoc.csv"

# Vungtau_f = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_traveloka\\data_url\\VungTau_url.txt"
# Vungtau_s = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_traveloka\\detail_data\\data_again\\Vungtau.csv"

# Halong_f = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_traveloka\\data_url\\HaLong_url.txt"
# Halong_s = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_traveloka\\detail_data\\data_again\\Halong.csv"

# file_dir_demo = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_mytour\\data_url\\demo.txt"
# file_dir_demo_small = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_mytour\\data_url\\demo_small.txt"
# file_s = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_mytour\\data_detail\\demo.csv"

Hanoi_f = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_mytour\\data_url\\Hanoi_url.txt"
Hanoi_s = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_mytour\\data_detail\\Hanoi.csv"

HCM_f = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_mytour\\data_url\\HoChiMinh_url.txt"
HCM_s = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_mytour\\data_detail\\HoChiMinh.csv"

Dalat_f = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_mytour\\data_url\\Dalat_url.txt"
Dalat_s = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_mytour\\data_detail\\Dalat.csv"

Danang_f = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_mytour\\data_url\\Danang_url.txt"
Danang_s = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_mytour\\data_detail\\Danang.csv"

Nhatrang_f = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_mytour\\data_url\\Nhatrang_url.txt"
Nhatrang_s = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_mytour\\data_detail\\Nhatrang.csv"

Phuquoc_f = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_mytour\\data_url\\Phuquoc_url.txt"
Phuquoc_s = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_mytour\\data_detail\\Phuquoc.csv"

Vungtau_f = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_mytour\\data_url\\Vungtau_url.txt"
Vungtau_s = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_mytour\\data_detail\\Vungtau.csv"

Quangninh_f = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_mytour\\data_url\\Quangninh_url.txt"
Quangninh_s = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_mytour\\data_detail\\Quangninh.csv"

Halong_f = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_mytour\\data_url\\Halong_url.txt"
Halong_s = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_mytour\\data_detail\\Halong.csv"


def scrollToEnd(driver):
    page = driver.find_element(by=By.TAG_NAME, value="html")
    page.send_keys(Keys.END)
    sleep(5)


def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1


def convertString(s):
    s = s.replace("(", "")
    s = s.replace(" ", "")
    s = s.replace("đánhgiá)", "")
    return int(s)


def handleSpecificString(list_ls):
    list_ls = [s for s in list_ls if "Xem tất cả" in s]
    result_ls = []
    for i in range(len(list_ls)):
        list_ls[i] = list_ls[i][list_ls[i].find("Xem tất cả\n")+11:]
        tmp = list_ls[i].split('\n')
        res = list(zip(tmp[::2], tmp[1::2]))
        result_ls = result_ls + res
    return result_ls

# driver = webdriver.Chrome(service=Service(
#     ChromeDriverManager().install()), options=options)


# url_demo = "https://mytour.vn/khach-san/44177-khach-san-the-twin.html?checkIn=16-07-2022&checkOut=17-07-2022&adults=1&rooms=1&children=0&priceKey=%2Bkhj4MYg%2F5obnE8D0l7Xy3l1D%2Bl9Yo1E51WaG9wYNLKup5rFYUpFqtiCW5nRvEw2w7OTCjhzeM0%3D"
# url_demo_1 = "https://mytour.vn/khach-san/50423-citadines-marina-ha-long.html?checkIn=16-07-2022&checkOut=17-07-2022&adults=1&rooms=1&children=0&priceKey=%2Bkhj4MYg%2F5orKAvp5TXfLZ6ExPOu7k7IVqfA98hLf1bYvEKvKnt9VjjsUj6y2al9ysbNPa8Qhvk%3D"
# url_demo_2 = "https://mytour.vn/khach-san/2536-khach-san-ruby-star-reddoorz.html?checkIn=16-07-2022&checkOut=17-07-2022&adults=1&rooms=1&children=0&priceKey=%2Bkhj4MYg%2F5oYFM8dC2YAKRw4b%2Fe5dTbFH6Jo5%2FN3ojftv62Mu1GcW7HAsIKB7si2"
# url_demo_3 = "https://mytour.vn/khach-san/902-khach-san-minh-dang.html?checkIn=16-07-2022&checkOut=17-07-2022&adults=1&rooms=1&children=0&priceKey=%2Bkhj4MYg%2F5qoImovAGJqqdgBWaRz1GCk6WDLGZx%2F89MVsmJqnuSe2QesjK1R3IXNbbceAzTKfKg%3D"
# url_demo_4 = "https://mytour.vn/khach-san/49675-khach-san-hyatt-regency-west-hanoi.html?checkIn=16-07-2022&checkOut=17-07-2022&adults=1&rooms=1&children=0&priceKey=%2FF6T3StyQjnEsg42LAT%2BlVv75arbiSgdXSnVqeNi7m57rjY0EqpA0xqYHfeVLSM10QqOyl%2FKS2k%3D"


def crawl_from_url(url, ten_tinh):
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=options)
    driver.get(url)
    sleep(5)

    # Ten thanh pho
    hotel_city = ten_tinh

    # Ten khach san
    try:
        hotel_name = driver.find_element(
            By.CSS_SELECTOR, 'input#input-search-hotel').get_attribute('value')
    except:
        hotel_name = "NULL"
    # Url

    # # Dia chi
    try:
        addrs = driver.find_elements(
            By.CSS_SELECTOR, 'div.MuiBox-root.jss136 > span.MuiBox-root')
        hotel_address = addrs[1].text
    except:
        hotel_address = "NULL"

    # So sao khach san
    try:
        stars = driver.find_elements(
            By.CSS_SELECTOR, 'div.MuiBox-root.jss186 > svg')
        hotel_star = len(stars)
    except:
        hotel_star = "NULL"

    # Gia phong nho nhat
    try:
        hotel_min_price = driver.find_element(
            By.CSS_SELECTOR, 'div.MuiBox-root.jss139 > span.MuiBox-root.jss143').text
    except:
        hotel_min_price = "NULL"

    # Rating
    try:
        hotel_rating = driver.find_element(
            By.CSS_SELECTOR, 'span.MuiBox-root.jss133').text
    except:
        hotel_rating = "NULL"

    # Nums of reviews
    try:
        txt = driver.find_element(
            By.CSS_SELECTOR, 'div.MuiBox-root.jss132 > span.MuiBox-root.jss134').text
        hotel_num_of_reviews = convertString(txt)
    except:
        hotel_num_of_reviews = 0

    # Review list
    if hotel_num_of_reviews == 0:
        hotel_reviews_list = []
    else:
        try:
            txt = driver.find_elements(
                By.CSS_SELECTOR, 'div.MuiBox-root.jss2 > div#evaluate > div > div > div.MuiGrid-root.MuiGrid-container > div.MuiGrid-root.MuiGrid-item.MuiGrid-grid-sm-9.MuiGrid-grid-md-9.MuiGrid-grid-lg-9 > div ')
            hotel_reviews_list = []

            for i in range(len(txt)):
                if (i % 2 == 0):
                    k = txt[i].text
                    k = k.replace(
                        "\nĐánh giá này có hữu ích với bạn không?", "")
                    hotel_reviews_list.append(k)
        except:
            hotel_reviews_list = ["NULL"]

    # FIX_1
    # Facilities
    try:
        all_fac = driver.find_elements(
            By.CSS_SELECTOR, '#top_places > div')[1]
        facs = all_fac.find_elements(By.CSS_SELECTOR, 'div > div > div > span')
        hotel_facilities = [facs[i].text for i in range(len(facs))]
        del hotel_facilities[0]
        if len(hotel_facilities) == 8:
            del hotel_facilities[len(hotel_facilities)-1]
    except:
        hotel_facilities = ["NULL"]

    # Ảnh
    try:
        imgs = driver.find_elements(
            By.CSS_SELECTOR, '#rooms_overview > div.MuiBox-root.jss144 > div')
        hotel_list_image = []
        for i in range(len(imgs)):
            try:
                img = imgs[i].find_element(By.CSS_SELECTOR, 'div > div > img')
                hotel_list_image.append(img.get_attribute('src'))
            except:
                pass
    except:
        hotel_list_image = ["NULL"]

    # Description
    try:
        all_des = driver.find_elements(
            By.CSS_SELECTOR, '#hotel_description > div > div')[1]
        des = all_des.find_elements(By.CSS_SELECTOR, 'div > div > p')
        hotel_description = []
        for i in range(len(des)):
            hotel_description.append(des[i].text)
        del hotel_description[0]
        hotel_description = list(filter(None, hotel_description))
    except:
        hotel_description = ["NULL"]

    # Near places
    try:
        all_places = driver.find_elements(
            By.CSS_SELECTOR, '#id-hotel-detail > div')[1]
        plcs = all_places.find_elements(
            By.CSS_SELECTOR, 'div > div.MuiBox-root.jss2 > div > div')
        ls = []
        hotel_near_places = []
        for i in range(len(plcs)):
            ls.append(plcs[i].text)
        hotel_near_places = handleSpecificString(ls)
    except:
        hotel_near_places = ["NULL"]

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

    df = pd.DataFrame(data=records, columns=['City',
                                             'Hotel name',
                                             'Image',
                                             'Url', 'Address', 'Stars',
                                             'Min Price', 'Rating',
                                             'Number of reviews',
                                             'Reviews',
                                             'Facilities',
                                             'Description',
                                             'Nearby places'
                                             ])

    df.to_csv(save_dir, index=False, encoding='utf8')
    print(df)
    print("\n------------------\n")
    print("So ban ghi cua " + ten_tinh + " la: " + str(len(records)))


save2csv(Hanoi_f, Hanoi_s, "Hà Nội")
sleep(4)
save2csv(HCM_f, HCM_s, "Hồ Chí Minh")
sleep(4)
save2csv(Dalat_f, Dalat_s, "Đà Lạt")
sleep(4)
save2csv(Danang_f, Danang_s, "Đà Nẵng")
sleep(4)
save2csv(Nhatrang_f, Nhatrang_s, "Nha Trang")
sleep(4)
save2csv(Phuquoc_f, Phuquoc_s, "Phú Quốc")
sleep(4)
save2csv(Vungtau_f, Vungtau_s, "Vũng Tàu")
sleep(4)
save2csv(Quangninh_f, Quangninh_s, "Hạ Long")
sleep(4)
save2csv(Halong_f, Halong_s, "Hạ Long")

# driver = webdriver.Chrome(service=Service(
#     ChromeDriverManager().install()), options=options)
# driver.get(url_demo)
# sleep(5)
# try:
#     all_fac = driver.find_elements(
#         By.CSS_SELECTOR, '#top_places > div')[1]
#     facs = all_fac.find_elements(By.CSS_SELECTOR, 'div > div > div > span')
#     hotel_facilities = [facs[i].text for i in range(len(facs))]
#     del hotel_facilities[0]
#     if len(hotel_facilities) == 8:
#         del hotel_facilities[len(hotel_facilities)-1]
# except:
#     hotel_facilities = ["NULL"]

# print(hotel_facilities)
# driver.close()
