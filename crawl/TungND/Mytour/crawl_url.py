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


def scrollToEnd(driver):
    page = driver.find_element(by=By.TAG_NAME, value="html")
    page.send_keys(Keys.END)
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(5)


def writeToText(demo, file_dir):
    # Ghi vao file
    # print(len(demo))
    with open(file_dir, 'a', encoding='utf-8') as f:
        for l in range(len(demo)):
            f.write(demo[l]+"\n")
    f.close()


def filter_url(links):
    links = links[8:]
    prefixes = ('https://mytour.vn/khach-san/td155', 'https://mytour.vn/ve-may-bay/', 'http://online.gov.vn/',
                'https://mytour.vn/news/', 'https://hms.mytour.vn/', 'https://career.mytour.vn/', 'https://mytour.vn/help/30-lien-he.html', 'https://mytour.vn/khach-san/t')

    newlist = [x for x in links if not x.startswith(prefixes)]
    return newlist


options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument("start-maximized")
options.add_argument('disable-infobars')

file_dir_demo = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_mytour\\data_url\\demo_test.txt"
file_dir_sub = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_mytour\\data_url\\"
# file_dir_main = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_mytour\\data_url\\URL_links_all.txt"

# Link web
url_Hanoi = "https://mytour.vn/khach-san/tp11/khach-san-tai-ha-noi.html?checkIn=16-07-2022&checkOut=17-07-2022&adults=1&rooms=1&children=0&travellerType=0"

url_HoChiMinh = "https://mytour.vn/khach-san/tp33/khach-san-tai-ho-chi-minh.html?checkIn=16-07-2022&checkOut=17-07-2022&adults=1&rooms=1&children=0&travellerType=0"

url_DaLat = "https://mytour.vn/khach-san/td155/khach-san-tai-thanh-pho-da-lat.html?checkIn=16-07-2022&checkOut=17-07-2022&adults=1&rooms=1&children=0&travellerType=0"

url_Danang = "https://mytour.vn/khach-san/tp50/khach-san-tai-da-nang.html?checkIn=16-07-2022&checkOut=17-07-2022&adults=1&rooms=1&children=0&travellerType=0"

url_NhaTrang = "https://mytour.vn/khach-san/td414/khach-san-tai-thanh-pho-nha-trang.html?checkIn=16-07-2022&checkOut=17-07-2022&adults=1&rooms=1&children=0&travellerType=0"

url_PhuQuoc = "https://mytour.vn/khach-san/td446/khach-san-tai-phu-quoc.html?checkIn=16-07-2022&checkOut=17-07-2022&adults=1&rooms=1&children=0&travellerType=0"

url_VungTau = "https://mytour.vn/khach-san/td686/khach-san-tai-thanh-pho-vung-tau.html?checkIn=16-07-2022&checkOut=17-07-2022&adults=1&rooms=1&children=0&travellerType=0"

url_QuangNinh = "https://mytour.vn/khach-san/tp10/khach-san-tai-quang-ninh.html?checkIn=16-07-2022&checkOut=17-07-2022&adults=1&rooms=1&children=0&travellerType=0"

url_HaLong = "https://mytour.vn/khach-san/td235/khach-san-tai-thanh-pho-ha-long.html?checkIn=16-07-2022&checkOut=17-07-2022&adults=1&rooms=1&children=0&travellerType=0"

click_range = [9, 7, 4, 7, 4, 3, 2, 1, 1]

list_url = [
    url_Hanoi,
    url_HoChiMinh,
    url_DaLat,
    url_Danang,
    url_NhaTrang,
    url_PhuQuoc,
    url_VungTau,
    url_QuangNinh,
    url_HaLong
]

name_file = [
    "Hanoi",
    "HoChiMinh",
    "Dalat",
    "Danang",
    "Nhatrang",
    "Phuquoc",
    "Vungtau",
    "Quangninh",
    "Halong"
]
#===============================#
# url_demo = "https://mytour.vn/khach-san/td235/khach-san-tai-thanh-pho-ha-long.html?checkIn=16-07-2022&checkOut=17-07-2022&adults=1&rooms=1&children=0&travellerType=0&page=1"

# url_demo_1 = "https://mytour.vn/khach-san/td155/khach-san-tai-thanh-pho-da-lat.html?checkIn=16-07-2022&checkOut=17-07-2022&adults=1&rooms=1&children=0&travellerType=0"

# range_pages = 4


def crawlURLPerPage(url_link, range_pages, file_dir):
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=options)
    for r in range(0, range_pages):
        str_cnt_page = "&page="+str(r+1)
        # print(str_cnt_page)
        url_open = url_link + str_cnt_page

        driver.get(url_open)
        sleep(5)

        scrollToEnd(driver)

        # Get url in a page

        urls = driver.find_elements(
            By.CSS_SELECTOR, 'a.MuiTypography-root.MuiLink-root.MuiLink-underlineHover.MuiTypography-colorPrimary')
        links = [url.get_attribute('href') for url in urls]

        hotel_links = []
        for p in range(len(links)):
            hotel_links.append(links[p])

        hotel_links = filter_url(hotel_links)

        print(len(hotel_links))
        writeToText(hotel_links, file_dir)

    driver.close()


# crawlURLPerPage(url_demo_1, 1, file_dir_demo)

# Crawl urls
for i in range(3, len(list_url)):
    file_s = file_dir_sub + name_file[i] + "_url.txt"
    crawlURLPerPage(list_url[i], click_range[i], file_s)

    with open(file_s, 'r') as fp:
        x = len(fp.readlines())
        print('Tổng số link url tinh', name_file[i], ' : ', x)


# df = pd.DataFrame(data=hotel_links)
# save_dir = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_mytour\\data_url\\demo_test_1_again.csv"
# df.to_csv(save_dir, index=False, encoding='utf8')

# # for i in range(len(hotel_links)):
# #     print(hotel_links[i])
# #     print("\n")
# print(len(hotel_links))

# driver.close()
