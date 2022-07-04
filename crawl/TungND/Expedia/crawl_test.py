from itertools import count
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd

options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument("start-maximized")
options.add_argument('disable-infobars')

file_dir = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\url_booking.txt_old"

# Link web
# 1680
url_Hanoi = "https://www.expedia.com.vn/Hotel-Search?adults=1&d1=2022-06-27&d2=2022-06-28&destination=H%C3%A0%20N%E1%BB%99i%20%28v%C3%A0%20v%C3%B9ng%20ph%E1%BB%A5%20c%E1%BA%ADn%29%2C%20Vi%C3%AA%CC%A3t%20Nam&endDate=2022-06-28&latLong=21.035911%2C105.839431&regionId=1428&rooms=1&semdtl=&sort=RECOMMENDED&startDate=2022-06-27&theme=&useRewards=true&userIntent="

# 2498
url_HoChiMinh = "https://www.expedia.com.vn/Hotel-Search?adults=1&d1=2022-06-27&d2=2022-06-28&destination=Th%C3%A0nh%20ph%E1%BB%91%20H%E1%BB%93%20Ch%C3%AD%20Minh%20%28v%C3%A0%20v%C3%B9ng%20ph%E1%BB%A5%20c%E1%BA%ADn%29%2C%20Vi%C3%AA%CC%A3t%20Nam&endDate=2022-06-28&latLong=10.776308%2C106.702867&regionId=178262&rooms=1&semdtl=&sort=RECOMMENDED&startDate=2022-06-27&theme=&useRewards=true&userIntent="

# 641
url_DatLat = "https://www.expedia.com.vn/Hotel-Search?adults=1&d1=2022-06-27&d2=2022-06-28&destination=%C4%90%C3%A0%20L%E1%BA%A1t%2C%20L%C3%A2m%20%C4%90%E1%BB%93ng%20%28t%E1%BB%89nh%29%2C%20Vi%C3%AA%CC%A3t%20Nam&directFlights=false&endDate=2022-06-28&hotels-destination=%C4%90%C3%A0%20L%E1%BA%A1t&latLong=11.926084%2C108.468138&localDateFormat=dd%2FMM%2Fyyyy&partialStay=false&regionId=1030&semdtl=&sort=RECOMMENDED&startDate=2022-06-27&theme=&useRewards=true&userIntent="

# 2244
url_Danang = "https://www.expedia.com.vn/Hotel-Search?adults=1&d1=2022-06-27&d2=2022-06-28&destination=%C4%90%C3%A0%20N%E1%BA%B5ng%20%28v%C3%A0%20v%C3%B9ng%20ph%E1%BB%A5%20c%E1%BA%ADn%29%2C%20Vi%C3%AA%CC%A3t%20Nam&directFlights=false&endDate=2022-06-28&hotels-destination=%C4%90%C3%A0%20N%E1%BA%B5ng&latLong=16.06076%2C108.217039&localDateFormat=dd%2FMM%2Fyyyy&partialStay=false&regionId=974&semdtl=&sort=RECOMMENDED&startDate=2022-06-27&theme=&useRewards=true&userIntent="

# 870
url_NhaTrang = "https://www.expedia.com.vn/Hotel-Search?adults=1&d1=2022-06-27&d2=2022-06-28&destination=Nha%20Trang%2C%20Kh%C3%A1nh%20H%C3%B2a%20%28t%E1%BB%89nh%29%2C%20Vi%C3%AA%CC%A3t%20Nam&directFlights=false&endDate=2022-06-28&hotels-destination=Nha%20Trang&hotels-destination=%C4%90%C3%A0%20L%E1%BA%A1t&latLong=12.24959%2C109.190704&localDateFormat=dd%2FMM%2Fyyyy&partialStay=false&regionId=6054439&semdtl=&sort=RECOMMENDED&startDate=2022-06-27&theme=&useRewards=true&userIntent="

# 464
url_PhuQuoc = "https://www.expedia.com.vn/Hotel-Search?adults=1&d1=2022-06-27&d2=2022-06-28&destination=Ph%C3%BA%20Qu%E1%BB%91c%2C%20Ki%C3%AAn%20Giang%20%28t%E1%BB%89nh%29%2C%20Vi%C3%AA%CC%A3t%20Nam&directFlights=false&endDate=2022-06-28&hotels-destination=Ph%C3%BA%20Qu%E1%BB%91c&hotels-destination=%C4%90%C3%A0%20N%E1%BA%B5ng&latLong=10.158625%2C103.984016&localDateFormat=dd%2FMM%2Fyyyy&partialStay=false&regionId=6141655&semdtl=&sort=RECOMMENDED&startDate=2022-06-27&theme=&useRewards=true&userIntent="

# 399
url_VungTau = "https://www.expedia.com.vn/Hotel-Search?adults=1&d1=2022-06-27&d2=2022-06-28&destination=Vu%CC%83ng%20Ta%CC%80u%2C%20B%C3%A0%20R%E1%BB%8Ba-V%C5%A9ng%20T%C3%A0u%20%28t%E1%BB%89nh%29%2C%20Vi%C3%AA%CC%A3t%20Nam&directFlights=false&endDate=2022-06-28&hotels-destination=Vu%CC%83ng%20Ta%CC%80u&hotels-destination=Nha%20Trang%2C%C4%90%C3%A0%20L%E1%BA%A1t&latLong=10.34589%2C107.076462&localDateFormat=dd%2FMM%2Fyyyy&partialStay=false&regionId=6054414&semdtl=&sort=RECOMMENDED&startDate=2022-06-27&theme=&useRewards=true&userIntent="

# 600
url_QuangNinh = "https://www.expedia.com.vn/Hotel-Search?adults=1&d1=2022-06-27&d2=2022-06-28&destination=Qu%E1%BA%A3ng%20Ninh%20%28t%E1%BB%89nh%29%2C%20Vi%C3%AA%CC%A3t%20Nam&directFlights=false&endDate=2022-06-28&hotels-destination=Qu%E1%BA%A3ng%20Ninh%20%28t%E1%BB%89nh%29&hotels-destination=Ph%C3%BA%20Qu%E1%BB%91c%2C%C4%90%C3%A0%20N%E1%BA%B5ng&latLong=21.11074365957125%2C107.48096764494251&localDateFormat=dd%2FMM%2Fyyyy&partialStay=false&regionId=6257682&semdtl=&sort=RECOMMENDED&startDate=2022-06-27&theme=&useRewards=true&userIntent="

list_url = [
    url_Hanoi,
    url_HoChiMinh,
    url_DatLat,
    url_Danang,
    url_NhaTrang,
    url_PhuQuoc,
    url_VungTau,
    url_QuangNinh
]

click_range = [35, 50, 15, 45, 20, 10, 10, 15]

# Thoi gian cho
delay = 30  # seconds

# Scroll ve cuoi trang de load du lieu


def scrollToEnd(driver):
    page = driver.find_element(by=By.TAG_NAME, value="html")
    page.send_keys(Keys.END)
    time.sleep(5)

# Crawl link khach san


def crawlLinks(driver):
    scrollToEnd(driver)
    urls = driver.find_elements(by=By.CLASS_NAME, value="uitk-card-link")
    links = [url.get_attribute('href') for url in urls]
    hotel_links = []
    for p in range(len(links)):
        hotel_links.append(links[p])

    return hotel_links


def writeToText(demo):
    # Ghi vao file
    print(len(demo))
    with open(file_dir, 'a', encoding='utf-8') as f:
        for l in range(len(demo)):
            f.write(demo[l]+"\n")
    f.close()


# for i in range(0, 8):
print("Bat dau crawl!\n")
# Test dem so lan click
count_click = 1

driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=options)
driver.get(list_url[0])

# Xu ly nut "Hien thi them"
while count_click < 5:
    try:
        scrollToEnd(driver)
        WebDriverWait(driver, delay).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 'button[data-stid="show-more-results"]'))).click()
        print("Button clicked #", count_click)
        count_click += 1
        time.sleep(5)

    except:
        count_click += 1
        pass

# Crawl
time.sleep(5)
demo = crawlLinks(driver)
print("Done part 1-----------\n")
print(len(demo))
writeToText(demo)
print("Hoan thanh crawl!")
time.sleep(5)

# File link chinh
save_dir = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\url_booking.txt"
# Tinh chinh lai du lieu link url
with open(file_dir, 'r') as f1, open(save_dir, 'w') as f2:
    for x in f1:
        if 'Hotel-Search' not in x:
            f2.write(x.strip()+'\n')
