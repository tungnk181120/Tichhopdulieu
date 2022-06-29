from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep
import csv
import re

import pandas as pd

driver = webdriver.Chrome("chromedriver.exe")


def craw_from_url(url):
    driver.get(url)

    # click xem them
    try:
        t1 = driver.find_element_by_css_selector(
            "a[class='b-button b-button_secondary b-button_small']").click()

        # driver.find_element_by_css_selector('button[data-stid="show-more-results"]').click()
    except:
        pass

    city = driver.find_element_by_css_selector(
        "input[data-component='search/destination/input-placeholder']")
    # print("Tên thành phố: ", city.get_attribute('value'))

    # print("\n============================\n")
    hotel_name = driver.find_element_by_css_selector(
        "h2[id='hp_hotel_name']")
    # print("Tên khách sạn: ", hotel_name.text)

    # url: đã có
    # print("\n============================\n")
    address = driver.find_element_by_css_selector(
        "span[data-node_tt_id='location_score_tooltip']")
    # print("Địa chỉ: ", address.text)

    # print("\n============================\n")
    num_stars = driver.find_elements_by_css_selector(
        "span[class='b6dc9a9e69 adc357e4f1 fe621d6382']")
    # print("Số sao khách sạn: ", len(num_stars))

    # print("\n============================\n")
    # price : tìm các thẻ chứa giá, lấy giá nhỏ nhất
    price = driver.find_elements_by_css_selector(
        "div[class='bui-price-display__value prco-text-nowrap-helper prco-inline-block-maker-helper prco-f-font-heading '] span")
    # print(price[0].text)

    # print("\n============================\n")

    # rating
    rating = driver.find_elements_by_css_selector(
        "div[class='b5cd09854e d10a6220b4']")
    if len(rating) != 0:
        # print("Người dùng đánh giá: ", rating[0].text)
        rating = rating[0].text
    else:
        rating = 0
        # print("Người dùng đánh giá: ", rating)
    # print("\n============================\n")

    try:
        num_reviews = driver.find_element_by_css_selector(
            "div[class='d8eab2cf7f c90c0a70d3 db63693c62']")
        # print("số đánh giá: ", num_reviews.text)
        num_reviews = num_reviews.text
    except:
        num_reviews = 0
        # print("số đánh giá: ", num_reviews)
    # print("\n============================\n")
    # reviews : click and crawl
    # print("Reivew:")
    res_review = []
    if num_reviews != 0:
        reviews = driver.find_elements_by_css_selector(
            "div[data-testid='featuredreview-text'] div div")
        for rev in reviews:
            try:
                # print(rev.text)
                res_review.append(rev.text)
            except:
                pass

    # print("Description:")
    description = driver.find_elements_by_css_selector(
        "div[id='property_description_content'] p")
    res_description = ''
    for des in description:
        # print(des.text)
        res_description += des.text + '\n'
    # print("\n============================\n")
    # nearby_places
    # print("nearby_places:")
    res_nearby_places = []
    nearby_places = driver.find_elements_by_css_selector(
        "ul[class='bui-list bui-list--divided bui-list--text'] li div div[class='bui-list__description']")
    num_km = driver.find_elements_by_css_selector(
        "div[class='bui-list__item-action hp_location_block__section_list_distance']")
    for i in range(len(nearby_places)):
        # print("Địa điểm tham quan xung quanh: ",
        #   nearby_places[i].text, "   ", num_km[i].text)
        res_nearby_places.append((nearby_places[i].text, num_km[i].text))
    # print("\n============================\n")
    # CSVC
    # print("CSVC:")
    res_CSVC = []
    csvc = driver.find_elements_by_css_selector(
        "div[class='hp_desc_important_facilities clearfix hp_desc_important_facilities--bui '] div")
    for i in range(int(len(csvc)/2)):
        # print(csvc[i].text)
        res_CSVC.append(csvc[i].text)
    # print("END============================")

    res_list_image = []
    list_image = driver.find_elements_by_css_selector(
        "div.clearfix.bh-photo-grid.fix-score-hover-opacity > div[aria-hidden='true'] > a")
    for image in list_image:
        try:
            res_list_image.append(image.get_attribute('data-thumb-url'))
        except:
            pass
    return (
        city.get_attribute('value'),
        hotel_name.text,
        url,
        address.text,
        len(num_stars),
        price[0].text,
        rating,
        num_reviews,
        res_review,
        res_CSVC,
        res_description,
        res_nearby_places,
        res_list_image
    )


# records_1 = []
# with open('url_booking_new_1.txt') as f:
#     for line in f:
#         try:
#             records_1.append(craw_from_url(line))
#             # print(craw_from_url(line))
#         except:
#             pass

# df = pd.DataFrame(data=records_1, columns=['City', 'Hotel name', 'Url', 'Address', 'Stars', 'Price',
#                   'Rating', 'Number of reviews', 'Reviews', 'Facilities', 'Description', 'Nearby places', 'Image'])
# df.to_csv('data_booking_com_1.csv', index=False, encoding='utf8')


# records_2 = []
# with open('url_booking_new_2.txt') as f:
#     for line in f:
#         try:
#             records_2.append(craw_from_url(line))
#             # print(craw_from_url(line))
#         except:
#             pass

# df = pd.DataFrame(data=records_2, columns=['City', 'Hotel name', 'Url', 'Address', 'Stars', 'Price',
#                   'Rating', 'Number of reviews', 'Reviews', 'Facilities', 'Description', 'Nearby places', 'Image'])
# df.to_csv('data_booking_com_2.csv', index=False, encoding='utf8')


records_3 = []
with open('url_booking_new_3.txt') as f:
    for line in f:
        try:
            records_3.append(craw_from_url(line))
            # print(craw_from_url(line))
        except:
            pass

df = pd.DataFrame(data=records_3, columns=['City', 'Hotel name', 'Url', 'Address', 'Stars', 'Price',
                  'Rating', 'Number of reviews', 'Reviews', 'Facilities', 'Description', 'Nearby places', 'Image'])
df.to_csv('data_booking_com_3.csv', index=False, encoding='utf8')
