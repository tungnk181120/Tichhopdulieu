from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import numpy as np
import pandas as pd
import re

options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument("start-maximized")
options.add_argument('disable-infobars')

data_f = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_mytour\\data_detail\\All_data_mytour.csv"
url_s = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_mytour\\data_detail\\Missing_url.csv"
url_f = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_mytour\\data_url\\Miss_star.txt"
save_dir = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_mytour\\data_detail\\Fill_url.csv"

raw_mytour = pd.read_csv(data_f)
#print(raw_mytour.head())

missing_stars_hotel_url = raw_mytour["Url"].loc[raw_mytour["Stars"]==0]
missing_stars_hotel_url = missing_stars_hotel_url.reset_index(drop=True)
# missing_stars_hotel_url.to_csv(url_s, index=False, encoding='utf8')

def get_stars(url):
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=options)
    driver.get(url)
    sleep(5)
    
    try:
        txt = driver.find_elements(By.CSS_SELECTOR, '#rooms_overview > div')[1]
        km = txt.find_elements(
            By.CSS_SELECTOR, 'div > div > div > div > div > svg')
        hotel_star = len(km)
    except:
        hotel_star = "NULL"
    
    return hotel_star

# for i in range(len(missing_stars_hotel_url)):
#     url = missing_stars_hotel_url[i]
#     with open(url_f, 'a') as fp:
#         fp.write(url)
#     fp.close()

def save2csv(file_dir, save_dir):
    result = []
    with open(file_dir) as f:
        for line in f:
            try:
                star = get_stars(line)
                result.append((line, star))
            except:
                pass
    
    df = pd.DataFrame(data=result, columns=["Url", "Stars"])
    df.to_csv(save_dir, index=False, encoding='utf8')
    print(df)
    print("\n------------------\n")
    print("So ban ghi la: " + str(len(result)))


save2csv(url_f, save_dir)