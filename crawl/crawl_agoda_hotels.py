import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import json
from selenium.webdriver.chrome.options import Options
import csv
from selenium.webdriver.chrome.service import Service

# Read hotel links json file
filepath = 'D:/LEARNING/20212/Tich hop du lieu/Crawl/hotel_links.json'
hotel_links_json = open(filepath)
hotel_links_data = json.load(hotel_links_json)
hotel_links = []
for hotel_link in hotel_links_data['hotel_links']:
    hotel_links.append(hotel_link)
# Crawl hotel content
options = Options()
options.add_argument('--headless')
number_of_hotel = len(hotel_links)
hotel_links = []
content = []
for i in range(0, number_of_hotel):
    print(i)
    try:
        url = hotel_links[i]
        driver = webdriver.Chrome(executable_path='D:/LEARNING/20212/Tich hop du lieu/Crawl/chromedriver', options=options)
        driver.get(url)
        time.sleep(3)
        city= "Hồ Chí Minh"
        hotel_name = driver.find_element(By.CSS_SELECTOR, 'h1[data-selenium="hotel-header-name"]').text
        address = driver.find_element(By.CSS_SELECTOR, 'span[data-selenium="hotel-address-map"]').text
        hotel_url = url
        rating = driver.find_element(By.CSS_SELECTOR, '.Typographystyled__TypographyStyled-sc-j18mtu-0 hTkvyT kite-js-Typography ').text
        price = driver.find_element(By.CSS_SELECTOR, 'strong[data-ppapi="room-price"]').text
        location_rating = driver.find_element(By.CSS_SELECTOR, 'p[class="Typographystyled__TypographyStyled-sc-j18mtu-0 Hkrzy kite-js-Typography "]').text
        n_reviews = driver.find_element(By.CSS_SELECTOR, 'p[class="Typographystyled__TypographyStyled-sc-j18mtu-0 Hkrzy kite-js-Typography "]').text
        fatalicities_elements = driver.find_elements(By.CSS_SELECTOR, 'p[class="Typographystyled__TypographyStyled-sc-j18mtu-0 keaLUr kite-js-Typography "]')
        fatalicites = []
        for fatalicity in fatalicities_elements:
            fatalicites.append(fatalicity)
        checkin = driver.find_element(By.CSS_SELECTOR, 'div[data-selenium="checkInText"]').text
        checkout = driver.find_element(By.CSS_SELECTOR, 'div[data-selenium="checkOutText"]').text
        images_elements = driver.find_elements(By.CSS_SELECTOR, 'img[class="SquareImage"]')
        images = []
        for image in images_elements:
            images.append(image.get_attribute("src"))
        driver.quit()
        # save
        hotel = {}
        hotel["city"] = city
        hotel["hotel name"] = hotel_name
        hotel["url"] = hotel_url
        hotel["price"] = price
        hotel["rating"] = rating
        hotel["location rating"] = location_rating
        hotel["n_reviews"] = n_reviews
        hotel["check in"] = checkin
        hotel["check out"] = checkout
        hotel["facilities"] = fatalicites
        hotel["images"] = images
        content.append(hotel)
    except:
        print('error:', i)
    
    time.sleep(5)
filepath = 'D:/LEARNING/20212/Tich hop du lieu/Crawl/hotel_contents.json'
hotel_contents = json.dumps(content)
with open(filepath, "w") as result:
    result.write(hotel_contents)
