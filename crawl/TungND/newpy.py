# # # https://proxycrawl.com/how-to-scrape-expedia
# # import json
# # import requests
# # from lxml import html
# # from collections import OrderedDict
# # import argparse


# # def parse(source, destination, date):
# #     for i in range(5):
# #         try:
# #             url = "https://www.expedia.com/Flights-Search?trip=oneway&leg1=from:{0},to:{1},departure:{2}TANYT&passengers=adults:1,children:0,seniors:0,infantinlap:Y&options=cabinclass%3Aeconomy&mode=search&origref=www.expedia.com".format(
# #                 source, destination, date)
# #             headers = {
# #                 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
# #             response = requests.get(url, headers=headers, verify=False)
# #             parser = html.fromstring(response.text)
# #             json_data_xpath = parser.xpath(
# #                 "//script[@id='cachedResultsJson']//text()")
# #             raw_json = json.loads(
# #                 json_data_xpath[0] if json_data_xpath else '')
# #             flight_data = json.loads(raw_json["content"])

# #             flight_info = OrderedDict()
# #             lists = []

# #             for i in flight_data['legs'].keys():
# #                 total_distance = flight_data['legs'][i].get(
# #                     "formattedDistance", '')
# #                 exact_price = flight_data['legs'][i].get(
# #                     'price', {}).get('totalPriceAsDecimal', '')

# #                 departure_location_airport = flight_data['legs'][i].get(
# #                     'departureLocation', {}).get('airportLongName', '')
# #                 departure_location_city = flight_data['legs'][i].get(
# #                     'departureLocation', {}).get('airportCity', '')
# #                 departure_location_airport_code = flight_data['legs'][i].get(
# #                     'departureLocation', {}).get('airportCode', '')

# #                 arrival_location_airport = flight_data['legs'][i].get(
# #                     'arrivalLocation', {}).get('airportLongName', '')
# #                 arrival_location_airport_code = flight_data['legs'][i].get(
# #                     'arrivalLocation', {}).get('airportCode', '')
# #                 arrival_location_city = flight_data['legs'][i].get(
# #                     'arrivalLocation', {}).get('airportCity', '')
# #                 airline_name = flight_data['legs'][i].get(
# #                     'carrierSummary', {}).get('airlineName', '')

# #                 no_of_stops = flight_data['legs'][i].get("stops", "")
# #                 flight_duration = flight_data['legs'][i].get('duration', {})
# #                 flight_hour = flight_duration.get('hours', '')
# #                 flight_minutes = flight_duration.get('minutes', '')
# #                 flight_days = flight_duration.get('numOfDays', '')

# #                 if no_of_stops == 0:
# #                     stop = "Nonstop"
# #                 else:
# #                     stop = str(no_of_stops)+' Stop'

# #                 total_flight_duration = "{0} days {1} hours {2} minutes".format(
# #                     flight_days, flight_hour, flight_minutes)
# #                 departure = departure_location_airport+", "+departure_location_city
# #                 arrival = arrival_location_airport+", "+arrival_location_city
# #                 carrier = flight_data['legs'][i].get(
# #                     'timeline', [])[0].get('carrier', {})
# #                 plane = carrier.get('plane', '')
# #                 plane_code = carrier.get('planeCode', '')
# #                 formatted_price = "{0:.2f}".format(exact_price)

# #                 if not airline_name:
# #                     airline_name = carrier.get('operatedBy', '')

# #                 timings = []
# #                 for timeline in flight_data['legs'][i].get('timeline', {}):
# #                     if 'departureAirport' in timeline.keys():
# #                         departure_airport = timeline['departureAirport'].get(
# #                             'longName', '')
# #                         departure_time = timeline['departureTime'].get(
# #                             'time', '')
# #                         arrival_airport = timeline.get(
# #                             'arrivalAirport', {}).get('longName', '')
# #                         arrival_time = timeline.get(
# #                             'arrivalTime', {}).get('time', '')
# #                         flight_timing = {
# #                             'departure_airport': departure_airport,
# #                             'departure_time': departure_time,
# #                             'arrival_airport': arrival_airport,
# #                             'arrival_time': arrival_time
# #                         }
# #                         timings.append(flight_timing)

# #                 flight_info = {'stops': stop,
# #                                'ticket price': formatted_price,
# #                                'departure': departure,
# #                                'arrival': arrival,
# #                                'flight duration': total_flight_duration,
# #                                'airline': airline_name,
# #                                'plane': plane,
# #                                'timings': timings,
# #                                'plane code': plane_code
# #                                }
# #                 lists.append(flight_info)
# #             sortedlist = sorted(
# #                 lists, key=lambda k: k['ticket price'], reverse=False)
# #             return sortedlist

# #         except ValueError:
# #             print("Rerying...")

# #         return {"error": "failed to process the page", }


# # if __name__ == "__main__":
# #     argparser = argparse.ArgumentParser()
# #     argparser.add_argument('source', help='Source airport code')
# #     argparser.add_argument('destination', help='Destination airport code')
# #     argparser.add_argument('date', help='MM/DD/YYYY')

# #     args = argparser.parse_args()
# #     source = args.source
# #     destination = args.destination
# #     date = args.date
# #     print("Fetching flight details")
# #     scraped_data = parse(source, destination, date)
# #     print("Writing data to output file")
# #     with open('%s-%s-flight-results.json' % (source, destination), 'w') as fp:
# #         json.dump(scraped_data, fp, indent=4)


# # #!/usr/bin/env python
# # from re import findall,sub
# # from lxml import html
# # from time import sleep
# # from selenium import webdriver
# # from pprint import pprint
# # from importlib import reload
# # from xvfbwrapper import Xvfb

# # def parse(url):
# #     searchKey = "Hanoi" # Change this to your city
# #     checkInDate = '22/07/2022' #Format %d/%m/%Y
# #     checkOutDate = '23/07/2022' #Format %d/%m/%Y
# #     response = webdriver.Firefox()
# #     response.get(url)
# #     searchKeyElement = response.find_elements_by_xpath('//input[contains(@id,"destination")]')
# #     checkInElement = response.find_elements_by_xpath('//input[contains(@class,"check-in")]')
# #     checkOutElement = response.find_elements_by_xpath('//input[contains(@class,"check-out")]')
# #     submitButton = response.find_elements_by_xpath('//button[@type="submit"]')
# #     if searchKeyElement and checkInElement and checkOutElement:
# #         searchKeyElement[0].send_keys(searchKey)
# #         checkInElement[0].clear()
# #         checkInElement[0].send_keys(checkInDate)
# #         checkOutElement[0].clear()
# #         checkOutElement[0].send_keys(checkOutDate)
# #         randomClick = response.find_elements_by_xpath('//h1')
# #         if randomClick:
# #             randomClick[0].click()
# #         submitButton[0].click()
# #         sleep(15)
# #         dropDownButton = response.find_elements_by_xpath('//fieldset[contains(@id,"dropdown")]')
# #         if dropDownButton:
# #             dropDownButton[0].click()
# #             priceLowtoHigh = response.find_elements_by_xpath('//li[contains(text(),"low to high")]')
# #             if priceLowtoHigh:
# #                 priceLowtoHigh[0].click()
# #                 sleep(10)

# #     parser = html.fromstring(response.page_source,response.current_url)
# #     hotels = parser.xpath('//div[@class="hotel-wrap"]')
# #     for hotel in hotels[:5]: #Replace 5 with 1 to just get the cheapest hotel
# #         hotelName = hotel.xpath('.//h3/a')
# #         hotelName = hotelName[0].text_content() if hotelName else None
# #         price = hotel.xpath('.//div[@class="price"]/a//ins')
# #         price = price[0].text_content().replace(",","").strip() if price else None
# #         if price==None:
# #             price = hotel.xpath('.//div[@class="price"]/a')
# #             price = price[0].text_content().replace(",","").strip() if price else None
# #         price = findall('([\d\.]+)',price) if price else None
# #         price = price[0] if price else None
# #         rating = hotel.xpath('.//div[@class="star-rating"]/span/@data-star-rating')
# #         rating = rating[0] if rating else None
# #         address = hotel.xpath('.//span[contains(@class,"locality")]')
# #         address = "".join([x.text_content() for x in address]) if address else None
# #         locality = hotel.xpath('.//span[contains(@class,"locality")]')
# #         locality = locality[0].text_content().replace(",","").strip() if locality else None
# #         region = hotel.xpath('.//span[contains(@class,"locality")]')
# #         region = region[0].text_content().replace(",","").strip() if region else None
# #         postalCode = hotel.xpath('.//span[contains(@class,"postal-code")]')
# #         postalCode = postalCode[0].text_content().replace(",","").strip() if postalCode else None
# #         countryName = hotel.xpath('.//span[contains(@class,"country-name")]')
# #         countryName = countryName[0].text_content().replace(",","").strip() if countryName else None

# #         item = {
# #                     "hotelName":hotelName,
# #                     "price":price,
# #                     "rating":rating,
# #                     "address":address,
# #                     "locality":locality,
# #                     "region":region,
# #                     "postalCode":postalCode,
# #                     "countryName":countryName,
# #         }
# #         pprint(item)
# # if __name__ == '__main__':
# #     vdisplay = Xvfb()
# #     vdisplay.start()
# #     parse('http://www.hotels.com')
# #     vdisplay.stop()


# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import json
# from selenium.webdriver.chrome.options import Options
# import csv
# from selenium.webdriver.chrome.service import Service
# chrome_options = Options()
# chrome_options.add_argument("--incognito")
# driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='E:/STUDY/UNIVERSITY/Sem_20212/Tich_hop_du_lieu/BTL/crawl_data/Crawl/chromedriver')
# driver.get('https://www.agoda.com/vi-vn/search?city=13170')
# hotel_links = []
# time.sleep(5)
# elements = driver.find_elements(By.CLASS_NAME, 'PropertyCard__Link')
# for element in elements:
#     url = element.get_attribute("href")
#     hotel_links.append(url)

# filepath = 'D:/LEARNING/20212/Tich hop du lieu/Crawl/hotel_links.json'

# hotel_links_dict = {'hotel_links': []}
# for i in range(0, len(hotel_links)):
#     hotel_links_dict['hotel_links'].append(hotel_links[i])
# hotel_links_json = json.dumps(hotel_links_dict)
# with open(filepath, "w") as outfile:
#     outfile.write(hotel_links_json)
#     # file = open(filepath, 'w', encoding='utf-8', newline='')
#     # file_CSV = csv.writer(file)
#     # file_CSV.writerow(hotel_links_dict)
# # file = open(filepath, 'w', encoding='utf-8', newline='')
# # file_CSV = csv.writer(file)
# # for hotel_link in hotel_links:
# #     file_CSV.writerow(hotel_link)
# # file_CSV.writerows(hotel_links)
# # file.close()
# print(hotel_links)
# driver.quit()

save_dir = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\url_booking.txt"
with open(save_dir, 'r') as f:
    lines = f.readlines()

set(lines)

if len(lines) == len(set(lines)):
      print ('all lines are unique')
else:
      print ('not all lines are unique')