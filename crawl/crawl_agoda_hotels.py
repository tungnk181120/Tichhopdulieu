import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import json
from selenium.webdriver.chrome.options import Options
import csv
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# Read hotel links json file
filepath = 'D:/LEARNING/20212/Tich hop du lieu/Crawl/hotel_links.json'
hotel_links_json = open(filepath)
hotel_links_data = json.load(hotel_links_json)
hotel_links = []
for hotel_link in hotel_links_data['hotel_links']:
    hotel_links.append(hotel_link)
# Crawl hotel content
options = Options()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument("start-maximized")
options.add_argument('disable-infobars')
number_of_hotel = len(hotel_links)
content = []
for i in range(0, number_of_hotel):
    # print(i)
    # print(hotel_links[i])
    # try:
    url = hotel_links[i]
    driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=options)
    driver.get(url)
    print(i)
    time.sleep(5)
    city= "Hồ Chí Minh"
    hotel_name = driver.find_element(By.CSS_SELECTOR, 'h1[data-selenium="hotel-header-name"]').text
    address = driver.find_element(By.CSS_SELECTOR, 'span[data-selenium="hotel-address-map"]').text
    hotel_url = url
    n_reviews = driver.find_elements(By.CSS_SELECTOR, 'p[class="Typographystyled__TypographyStyled-sc-j18mtu-0 Hkrzy kite-js-Typography "]')
    n_review = n_reviews[0].text
    prices = driver.find_elements(By.CSS_SELECTOR, 'strong[data-ppapi="room-price"]')
    price = prices[0].text
    location_ratings = driver.find_elements(By.CSS_SELECTOR, 'p[class="Typographystyled__TypographyStyled-sc-j18mtu-0 Hkrzy kite-js-Typography "]')
    location_rating = location_ratings[2].text
    ratings = driver.find_elements(By.CSS_SELECTOR, 'h3[class="Typographystyled__TypographyStyled-sc-j18mtu-0 hTkvyT kite-js-Typography "]')
    rating = ratings[0].text
    #fata
    fatalicities_elements = driver.find_elements(By.CSS_SELECTOR, 'p[class="Typographystyled__TypographyStyled-sc-j18mtu-0 keaLUr kite-js-Typography "]')
    fatalicites = []
    for i in range(0, len(fatalicities_elements)):
        fatalicites.append(fatalicities_elements[i].text)
    checkin = driver.find_element(By.CSS_SELECTOR, 'div[data-selenium="checkInText"]').text
    checkout = driver.find_element(By.CSS_SELECTOR, 'div[data-selenium="checkOutText"]').text
    images_elements = driver.find_elements(By.CSS_SELECTOR, 'img[class="SquareImage"]')
    image = images_elements[0].get_attribute("src")
    # for image in images_elements:
    #     images.append(image.get_attribute("src"))
    driver.quit()
    # save
    hotel = {}
    hotel["city"] = city
    hotel["hotel name"] = hotel_name
    hotel["url"] = hotel_url
    hotel['address'] = address
    hotel["price"] = price
    hotel["rating"] = rating
    hotel["location rating"] = location_rating
    hotel["n_reviews"] = n_review
    hotel["check in"] = checkin
    hotel["check out"] = checkout
    hotel["facilities"] = fatalicites
    # hotel["image"] = image
    content.append(hotel)
    print(content)
    # except:
    #     print('error:', i)
    
    time.sleep(5)

filepath = 'D:/LEARNING/20212/Tich hop du lieu/Crawl/hotel_contents.json'
hotel_contents = json.dumps(content)
with open(filepath, "w") as result:
    result.write(hotel_contents)
