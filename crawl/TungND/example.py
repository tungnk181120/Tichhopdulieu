# import both Requests and Beautifulsoup

import requests

from bs4 import BeautifulSoup


class ExpeHotelScraper:

    def __init__(self, url):

        self.url = url

        self.download_page()

    def download_page(self):

        # method for downloading the hotel page

        self.page = requests.get(self.url).text

    def scrape_data(self):

        # method for scraping out hotel name, address, and about

        soup = BeautifulSoup(self.page, "html.parser")

        hotel_name = soup.find("h1", {"class": "uitk-heading-3"}).text

        hotel_address = soup.find(
            "div", {"data-stid": "content-hotel-address"}).text

        hotel_about = soup.find("div", {"data-stid": "content-markup"}).text

        return {"name": hotel_name,

                "about": hotel_about,

                "address": hotel_address

                }


urls = ["https://www.expedia.com.vn/Hanoi-Khach-San-Hanoi-Royal-Palace-Hotel-2.h6747597.Thong-tin-khach-san?chkin=2022-07-22&chkout=2022-07-23&x_pwa=1&rfrr=HSR&pwa_ts=1655817753883&referrerUrl=aHR0cHM6Ly93d3cuZXhwZWRpYS5jb20udm4vSG90ZWwtU2VhcmNo&useRewards=true&rm1=a1&regionId=1428&destination=H%C3%A0+N%E1%BB%99i+%28v%C3%A0+v%C3%B9ng+ph%E1%BB%A5+c%E1%BA%ADn%29%2C+Vi%C3%AA%CC%A3t+Nam&destType=MARKET&neighborhoodId=3000664659&sort=RECOMMENDED&top_dp=687831&top_cur=VND&semdtl=&userIntent=&selectedRoomType=214344368&selectedRatePlan=248277564", ]

for url in urls:

    x = ExpeHotelScraper(url)

    print(x.scrape_data())
