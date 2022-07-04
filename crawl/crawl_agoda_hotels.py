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


file_dir = "D:/LEARNING/20212/Tich hop du lieu/Crawl/url_hotels_agoda_hanoi.txt"
driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=options)

def scrollToEnd(driver):
    page = driver.find_element(by=By.TAG_NAME, value="html")
    page.send_keys(Keys.END)
    # time.sleep(5)

def craw_from_url(url):
    driver.get(url)
    time.sleep(10)
    # scrollToEnd(driver)
    city= "Hà Nội"
    hotel_name = driver.find_element(By.CSS_SELECTOR, 'h1[data-selenium="hotel-header-name"]').text
    address = driver.find_element(By.CSS_SELECTOR, 'span[data-selenium="hotel-address-map"]').text
    hotel_url = url
    n_reviews = driver.find_elements(By.CSS_SELECTOR, 'p[class="Typographystyled__TypographyStyled-sc-j18mtu-0 Hkrzy kite-js-Typography "]')
    n_review = n_reviews[0].text
    # prices = driver.find_elements(By.CSS_SELECTOR, 'strong[data-ppapi="room-price"]')
    # price = prices[0].text
    price = driver.find_element(By.CSS_SELECTOR, 'div[data-element-name="cheapest-room-price-property-nav-bar"]').get_attribute('data-cheapest-room-price')
    location_ratings = driver.find_elements(By.CSS_SELECTOR, 'p[class="Typographystyled__TypographyStyled-sc-j18mtu-0 Hkrzy kite-js-Typography "]')
    location_rating = location_ratings[2].text
    ratings = driver.find_elements(By.CSS_SELECTOR, 'h3[class="Typographystyled__TypographyStyled-sc-j18mtu-0 hTkvyT kite-js-Typography "]')
    rating = ratings[0].text
    # fata
    fatalicities_elements = driver.find_elements(By.CSS_SELECTOR, 'p[class="Typographystyled__TypographyStyled-sc-j18mtu-0 keaLUr kite-js-Typography "]')
    fatalicites = []
    for i in range(0, len(fatalicities_elements)):
        fatalicites.append(fatalicities_elements[i].text)
    checkin = driver.find_element(By.CSS_SELECTOR, 'div[data-selenium="checkInText"]').text
    checkout = driver.find_element(By.CSS_SELECTOR, 'div[data-selenium="checkOutText"]').text
    images_elements = driver.find_elements(By.CSS_SELECTOR, 'img[class="SquareImage"]')
    image = images_elements[0].get_attribute("src")

    return (
        city,
        hotel_name,
        hotel_url,
        image,
        address,
        n_review,
        price,
        rating,
        location_rating,
        fatalicites,
        checkin,
        checkout
    )

# print(craw_from_url("https://www.agoda.com/vi-vn/swiss-belresort-tuyen-lam-dalat/hotel/dalat-vn.html?finalPriceView=1&isShowMobileAppPrice=false&cid=-1&numberOfBedrooms=&familyMode=false&adults=1&children=0&rooms=1&maxRooms=0&checkIn=2022-07-5&isCalendarCallout=false&childAges=&numberOfGuest=0&missingChildAges=false&travellerType=-1&showReviewSubmissionEntry=false&currencyCode=USD&isFreeOccSearch=false&flexibleDateSearchCriteria=[object%20Object]&isCityHaveAsq=false&tspTypes=15,5&los=1&searchrequestid=2e790d44-ebf8-435a-9dae-52b22ce5cdfe"))
records = []
with open(file_dir) as f:
    for line in f:
        try:
            print(line)
            content = craw_from_url(line)
            print(content)
            records.append(content)
        except:
            pass

df = pd.DataFrame(data=records, columns=['City', 'Hotel name', 'Url', 'Image', 'Address', 'Number reviews', 'Price',
                  'Rating', 'Location Rating', 'Facilities', 'Checkin', 'Checkout'])
df.to_csv('crawl_agoda_hotels_hanoi.csv', index=False, encoding='utf8')

driver.quit()