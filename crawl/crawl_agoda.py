import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import json
from selenium.webdriver.chrome.options import Options
import csv
from selenium.webdriver.chrome.service import Service
chrome_options = Options()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='D:/LEARNING/20212/Tich hop du lieu/Crawl/chromedriver')
driver.get('https://www.agoda.com/vi-vn/search?city=13170')
hotel_links = []
time.sleep(20)
# Thêm timesleep -> load nhiều hơn. Chưa cần xử lý cuộn trang.
elements = driver.find_elements(By.CLASS_NAME, 'PropertyCard__Link')
for element in elements:
    url = element.get_attribute("href")
    hotel_links.append(url)

filepath = 'D:/LEARNING/20212/Tich hop du lieu/Crawl/hotel_links.json'

hotel_links_dict = {'hotel_links': []}
for i in range(0, len(hotel_links)):
    hotel_links_dict['hotel_links'].append(hotel_links[i])
hotel_links_json = json.dumps(hotel_links_dict)
with open(filepath, "w") as outfile:
    outfile.write(hotel_links_json)
    # file = open(filepath, 'w', encoding='utf-8', newline='')
    # file_CSV = csv.writer(file)
    # file_CSV.writerow(hotel_links_dict)
# file = open(filepath, 'w', encoding='utf-8', newline='')
# file_CSV = csv.writer(file)
# for hotel_link in hotel_links:
#     file_CSV.writerow(hotel_link)
# file_CSV.writerows(hotel_links)
# file.close()
print(hotel_links)
driver.quit()