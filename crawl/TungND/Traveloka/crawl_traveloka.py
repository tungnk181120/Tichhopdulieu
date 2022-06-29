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


# def writeToText(result):
#     # Ghi vao file
#     print(len(result))
#     with open(file_dir, 'a', encoding='utf-8') as f:
#         for l in range(len(result)):
#             f.write(result[l]+"\n")
#     f.close()

def scrollToEnd(driver):
    page = driver.find_element(by=By.TAG_NAME, value="html")
    page.send_keys(Keys.END)
    sleep(5)


options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument("start-maximized")
options.add_argument('disable-infobars')

file_dir = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_traveloka\\data_url\\url_booking.txt"

# Link web
url_Hanoi = "https://www.traveloka.com/vi-vn/hotel/search?spec=16-07-2022.17-07-2022.1.1.HOTEL_GEO.10009843.H%C3%A0%20N%E1%BB%99i.1"

url_HoChiMinh = "https://www.traveloka.com/vi-vn/hotel/search?spec=16-07-2022.17-07-2022.1.1.HOTEL_GEO.10009794.Th%C3%A0nh%20ph%E1%BB%91%20H%E1%BB%93%20Ch%C3%AD%20Minh.1"

url_DaLat = "https://www.traveloka.com/vi-vn/hotel/search?spec=16-07-2022.17-07-2022.1.1.HOTEL_GEO.10010169.%C4%90%C3%A0%20L%E1%BA%A1t.1"

url_Danang = "https://www.traveloka.com/vi-vn/hotel/search?spec=16-07-2022.17-07-2022.1.1.HOTEL_GEO.10010083.%C4%90%C3%A0%20N%E1%BA%B5ng.1"

url_NhaTrang = "https://www.traveloka.com/vi-vn/hotel/search?spec=16-07-2022.17-07-2022.1.1.HOTEL_GEO.10010498.Nha%20Trang.1"

url_PhuQuoc = "https://www.traveloka.com/vi-vn/hotel/search?spec=16-07-2022.17-07-2022.1.1.HOTEL_GEO.10011570.Ph%C3%BA%20Qu%E1%BB%91c.1"

url_VungTau = "https://www.traveloka.com/vi-vn/hotel/search?spec=16-07-2022.17-07-2022.1.1.HOTEL_GEO.10009889.B%C3%A0%20R%E1%BB%8Ba%20-%20V%C5%A9ng%20T%C3%A0u.1"

url_QuangNinh = "https://www.traveloka.com/vi-vn/hotel/search?spec=16-07-2022.17-07-2022.1.1.HOTEL_GEO.10009904.T%E1%BB%89nh%20Qu%E1%BA%A3ng%20Ninh.1"

url_HaLong = "https://www.traveloka.com/vi-vn/hotel/search?spec=16-07-2022.17-07-2022.1.1.HOTEL_GEO.30010278.Th%C3%A0nh%20ph%E1%BB%91%20H%E1%BA%A1%20Long.1"

click_range = [22, 31, 15, 17, 12, 8, 10, 6, 5]

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

driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=options)
driver.get(list_url[8])
sleep(5)

driver.find_element(By.CSS_SELECTOR, "div[class='_2Qki3 _11frB']").click()
result = []

for i in range(0, click_range[8]):
    urls = driver.find_elements(
        By.CSS_SELECTOR, "div[class='_2qd8A'] > div[class='ztzlF _2nyWi']")
    for url in urls:
        try:
            url.click()
            sleep(0.5)
            driver.switch_to.window(driver.window_handles[1])
            sleep(0.5)
            with open(file_dir, 'a', encoding='utf-8') as f:
                f.write(driver.current_url+"\n")
            # result.append(driver.current_url)
            driver.close()
            sleep(0.5)
            driver.switch_to.window(driver.window_handles[0])
            sleep(0.5)
        except:
            pass
    try:
        driver.find_element(By.CSS_SELECTOR, "div[id='next-button']").click()
        sleep(5)
    except:
        pass
    sleep(5)

# print(len(result))
# writeToText(result)


# print(len(result))


# def writeToText(result):
#     # Ghi vao file
#     print(len(result))
#     with open(file_dir, 'a', encoding='utf-8') as f:
#         for l in range(len(result)):
#             f.write(result[l]+"\n")
#     f.close()


# writeToText(result)
