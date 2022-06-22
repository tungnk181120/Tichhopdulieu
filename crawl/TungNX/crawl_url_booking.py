from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep
import csv
import re

# 40
url_Ha_Noi = "https://www.booking.com/searchresults.vi.html?aid=304142&label=gen173nr-1FCAEoggI46AdIM1gEaPQBiAEBmAEquAEXyAEM2AEB6AEB-AELiAIBqAIDuAK0gsKVBsACAdICJDQ3YzhiNDIzLTk1OWItNDVmMy1hOTc0LWRkNDhhNTQyZTY3N9gCBuACAQ&sid=ca5360fefe66e82e8f5833cf7345f576&sb=1&sb_lp=1&src=index&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Findex.vi.html%3Faid%3D304142%26label%3Dgen173nr-1FCAEoggI46AdIM1gEaPQBiAEBmAEquAEXyAEM2AEB6AEB-AELiAIBqAIDuAK0gsKVBsACAdICJDQ3YzhiNDIzLTk1OWItNDVmMy1hOTc0LWRkNDhhNTQyZTY3N9gCBuACAQ%26sid%3Dca5360fefe66e82e8f5833cf7345f576%26click_from_hp_logo%3D1%3Bsb_price_type%3Dtotal%3Bsrpvid%3D87687b2a59350761%26%26&ss=H%C3%A0+N%E1%BB%99i&is_ski_area=0&ssne=Ha%CC%80+N%C3%B4%CC%A3i&ssne_untouched=Ha%CC%80+N%C3%B4%CC%A3i&checkin_year=2022&checkin_month=6&checkin_monthday=27&checkout_year=2022&checkout_month=6&checkout_monthday=28&group_adults=1&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1&search_pageview_id=efa47b362fef024c&ss_raw=H%C3%A0+N%E1%BB%99i"

# 40
url_Ho_Chi_Minh = "https://www.booking.com/searchresults.vi.html?aid=304142&label=gen173nr-1FCAEoggI46AdIM1gEaPQBiAEBmAEquAEXyAEM2AEB6AEB-AELiAIBqAIDuAK0gsKVBsACAdICJDQ3YzhiNDIzLTk1OWItNDVmMy1hOTc0LWRkNDhhNTQyZTY3N9gCBuACAQ&sid=ca5360fefe66e82e8f5833cf7345f576&sb=1&sb_lp=1&src=index&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Findex.vi.html%3Faid%3D304142%26label%3Dgen173nr-1FCAEoggI46AdIM1gEaPQBiAEBmAEquAEXyAEM2AEB6AEB-AELiAIBqAIDuAK0gsKVBsACAdICJDQ3YzhiNDIzLTk1OWItNDVmMy1hOTc0LWRkNDhhNTQyZTY3N9gCBuACAQ%26sid%3Dca5360fefe66e82e8f5833cf7345f576%26click_from_hp_logo%3D1%3Bsb_price_type%3Dtotal%3Bsrpvid%3D87687b2a59350761%26%26&ss=TP.+H%E1%BB%93+Ch%C3%AD+Minh%2C+Khu+v%E1%BB%B1c+TP.+H%E1%BB%93+Ch%C3%AD+Minh%2C+Vi%E1%BB%87t+Nam&is_ski_area=0&ssne=Ha%CC%80+N%C3%B4%CC%A3i&ssne_untouched=Ha%CC%80+N%C3%B4%CC%A3i&checkin_year=2022&checkin_month=6&checkin_monthday=27&checkout_year=2022&checkout_month=6&checkout_monthday=28&group_adults=1&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1&ac_position=0&ac_langcode=vi&ac_click_type=b&dest_id=-3730078&dest_type=city&iata=SGN&place_id_lat=10.771475&place_id_lon=106.698296&search_pageview_id=efa47b362fef024c&search_selected=true&ss_raw=H%E1%BB%93+Ch%C3%AD+Minh"

# 27
url_Da_lat = "https://www.booking.com/searchresults.vi.html?aid=304142&label=gen173nr-1FCAEoggI46AdIM1gEaPQBiAEBmAEquAEXyAEM2AEB6AEB-AELiAIBqAIDuAK0gsKVBsACAdICJDQ3YzhiNDIzLTk1OWItNDVmMy1hOTc0LWRkNDhhNTQyZTY3N9gCBuACAQ&sid=ca5360fefe66e82e8f5833cf7345f576&sb=1&sb_lp=1&src=index&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Findex.vi.html%3Faid%3D304142%26label%3Dgen173nr-1FCAEoggI46AdIM1gEaPQBiAEBmAEquAEXyAEM2AEB6AEB-AELiAIBqAIDuAK0gsKVBsACAdICJDQ3YzhiNDIzLTk1OWItNDVmMy1hOTc0LWRkNDhhNTQyZTY3N9gCBuACAQ%26sid%3Dca5360fefe66e82e8f5833cf7345f576%26click_from_hp_logo%3D1%3Bsb_price_type%3Dtotal%3Bsrpvid%3D87687b2a59350761%26%26&ss=%C4%90%C3%A0+L%E1%BA%A1t%2C+L%C3%A2m+%C4%90%E1%BB%93ng%2C+Vi%E1%BB%87t+Nam&is_ski_area=0&ssne=Ha%CC%80+N%C3%B4%CC%A3i&ssne_untouched=Ha%CC%80+N%C3%B4%CC%A3i&checkin_year=2022&checkin_month=6&checkin_monthday=27&checkout_year=2022&checkout_month=6&checkout_monthday=28&group_adults=1&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1&ac_position=0&ac_langcode=vi&ac_click_type=b&dest_id=-3712045&dest_type=city&iata=DLI&place_id_lat=11.94266&place_id_lon=108.436905&search_pageview_id=efa47b362fef024c&search_selected=true&ss_raw=%C4%90%C3%A0+L%E1%BA%A1t"

# 31
url_Da_Nang = "https://www.booking.com/searchresults.vi.html?aid=304142&label=gen173nr-1FCAEoggI46AdIM1gEaPQBiAEBmAEquAEXyAEM2AEB6AEB-AELiAIBqAIDuAK0gsKVBsACAdICJDQ3YzhiNDIzLTk1OWItNDVmMy1hOTc0LWRkNDhhNTQyZTY3N9gCBuACAQ&sid=ca5360fefe66e82e8f5833cf7345f576&sb=1&sb_lp=1&src=index&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Findex.vi.html%3Faid%3D304142%26label%3Dgen173nr-1FCAEoggI46AdIM1gEaPQBiAEBmAEquAEXyAEM2AEB6AEB-AELiAIBqAIDuAK0gsKVBsACAdICJDQ3YzhiNDIzLTk1OWItNDVmMy1hOTc0LWRkNDhhNTQyZTY3N9gCBuACAQ%26sid%3Dca5360fefe66e82e8f5833cf7345f576%26click_from_hp_logo%3D1%3Bsb_price_type%3Dtotal%3Bsrpvid%3D87687b2a59350761%26%26&ss=%C4%90%C3%A0+N%E1%BA%B5ng%2C+Th%C3%A0nh+ph%E1%BB%91+%C4%90%C3%A0+N%E1%BA%B5ng%2C+Vi%E1%BB%87t+Nam&is_ski_area=0&ssne=Ha%CC%80+N%C3%B4%CC%A3i&ssne_untouched=Ha%CC%80+N%C3%B4%CC%A3i&checkin_year=2022&checkin_month=6&checkin_monthday=27&checkout_year=2022&checkout_month=6&checkout_monthday=28&group_adults=1&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1&ac_position=0&ac_langcode=vi&ac_click_type=b&dest_id=-3712125&dest_type=city&iata=DAD&place_id_lat=16.068365&place_id_lon=108.21919&search_pageview_id=efa47b362fef024c&search_selected=true&ss_raw=%C4%90%C3%A0+N%E1%BA%B5ng"

# 20
url_Nha_Trang = "https://www.booking.com/searchresults.vi.html?aid=304142&label=gen173nr-1FCAEoggI46AdIM1gEaPQBiAEBmAEquAEXyAEM2AEB6AEB-AELiAIBqAIDuAK0gsKVBsACAdICJDQ3YzhiNDIzLTk1OWItNDVmMy1hOTc0LWRkNDhhNTQyZTY3N9gCBuACAQ&sid=ca5360fefe66e82e8f5833cf7345f576&sb=1&sb_lp=1&src=index&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Findex.vi.html%3Faid%3D304142%26label%3Dgen173nr-1FCAEoggI46AdIM1gEaPQBiAEBmAEquAEXyAEM2AEB6AEB-AELiAIBqAIDuAK0gsKVBsACAdICJDQ3YzhiNDIzLTk1OWItNDVmMy1hOTc0LWRkNDhhNTQyZTY3N9gCBuACAQ%26sid%3Dca5360fefe66e82e8f5833cf7345f576%26click_from_hp_logo%3D1%3Bsb_price_type%3Dtotal%3Bsrpvid%3D87687b2a59350761%26%26&ss=Nha+Trang%2C+Kh%C3%A1nh+H%C3%B2a%2C+Vi%E1%BB%87t+Nam&is_ski_area=0&ssne=Ha%CC%80+N%C3%B4%CC%A3i&ssne_untouched=Ha%CC%80+N%C3%B4%CC%A3i&checkin_year=2022&checkin_month=6&checkin_monthday=27&checkout_year=2022&checkout_month=6&checkout_monthday=28&group_adults=1&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1&ac_position=0&ac_langcode=vi&ac_click_type=b&dest_id=-3723998&dest_type=city&iata=NHA&place_id_lat=12.238502&place_id_lon=109.195175&search_pageview_id=efa47b362fef024c&search_selected=true&ss_raw=Nha+Trang"

# 11
url_Phu_Quoc = "https://www.booking.com/searchresults.vi.html?aid=304142&label=gen173nr-1FCAEoggI46AdIM1gEaPQBiAEBmAEquAEXyAEM2AEB6AEB-AELiAIBqAIDuAK0gsKVBsACAdICJDQ3YzhiNDIzLTk1OWItNDVmMy1hOTc0LWRkNDhhNTQyZTY3N9gCBuACAQ&sid=ca5360fefe66e82e8f5833cf7345f576&sb=1&sb_lp=1&src=index&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Findex.vi.html%3Faid%3D304142%26label%3Dgen173nr-1FCAEoggI46AdIM1gEaPQBiAEBmAEquAEXyAEM2AEB6AEB-AELiAIBqAIDuAK0gsKVBsACAdICJDQ3YzhiNDIzLTk1OWItNDVmMy1hOTc0LWRkNDhhNTQyZTY3N9gCBuACAQ%26sid%3Dca5360fefe66e82e8f5833cf7345f576%26click_from_hp_logo%3D1%3Bsb_price_type%3Dtotal%3Bsrpvid%3D87687b2a59350761%26%26&ss=Ph%C3%BA+Qu%E1%BB%91c%2C+Ki%C3%AAn+Giang%2C+Vi%E1%BB%87t+Nam&is_ski_area=0&ssne=Ha%CC%80+N%C3%B4%CC%A3i&ssne_untouched=Ha%CC%80+N%C3%B4%CC%A3i&checkin_year=2022&checkin_month=6&checkin_monthday=27&checkout_year=2022&checkout_month=6&checkout_monthday=28&group_adults=1&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1&ac_position=0&ac_langcode=vi&ac_click_type=b&dest_id=-3726177&dest_type=city&iata=PQC&place_id_lat=10.216248&place_id_lon=103.95939&search_pageview_id=efa47b362fef024c&search_selected=true&ss_raw=Ph%C3%BA+Qu%E1%BB%91c"

# 25
url_Vung_Tau = "https://www.booking.com/searchresults.vi.html?aid=304142&label=gen173nr-1FCAEoggI46AdIM1gEaPQBiAEBmAEquAEXyAEM2AEB6AEB-AELiAIBqAIDuAK0gsKVBsACAdICJDQ3YzhiNDIzLTk1OWItNDVmMy1hOTc0LWRkNDhhNTQyZTY3N9gCBuACAQ&sid=ca5360fefe66e82e8f5833cf7345f576&sb=1&sb_lp=1&src=index&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Findex.vi.html%3Faid%3D304142%26label%3Dgen173nr-1FCAEoggI46AdIM1gEaPQBiAEBmAEquAEXyAEM2AEB6AEB-AELiAIBqAIDuAK0gsKVBsACAdICJDQ3YzhiNDIzLTk1OWItNDVmMy1hOTc0LWRkNDhhNTQyZTY3N9gCBuACAQ%26sid%3Dca5360fefe66e82e8f5833cf7345f576%26click_from_hp_logo%3D1%3Bsb_price_type%3Dtotal%3Bsrpvid%3D87687b2a59350761%26%26&ss=V%C5%A9ng+T%C3%A0u%2C+B%C3%A0+R%E1%BB%8Ba+-+V%C5%A9ng+T%C3%A0u%2C+Vi%E1%BB%87t+Nam&is_ski_area=0&ssne=Ha%CC%80+N%C3%B4%CC%A3i&ssne_untouched=Ha%CC%80+N%C3%B4%CC%A3i&checkin_year=2022&checkin_month=6&checkin_monthday=27&checkout_year=2022&checkout_month=6&checkout_monthday=28&group_adults=1&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1&ac_position=0&ac_langcode=vi&ac_click_type=b&dest_id=-3733750&dest_type=city&place_id_lat=10.347682&place_id_lon=107.08443&search_pageview_id=efa47b362fef024c&search_selected=true&ss_raw=V%C5%A9ng+T%C3%A0u"

# 2
url_Quang_Ninh = "https://www.booking.com/searchresults.vi.html?aid=304142&label=gen173nr-1FCAEoggI46AdIM1gEaPQBiAEBmAEquAEXyAEM2AEB6AEB-AELiAIBqAIDuAK0gsKVBsACAdICJDQ3YzhiNDIzLTk1OWItNDVmMy1hOTc0LWRkNDhhNTQyZTY3N9gCBuACAQ&sid=ca5360fefe66e82e8f5833cf7345f576&sb=1&sb_lp=1&src=index&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Findex.vi.html%3Faid%3D304142%26label%3Dgen173nr-1FCAEoggI46AdIM1gEaPQBiAEBmAEquAEXyAEM2AEB6AEB-AELiAIBqAIDuAK0gsKVBsACAdICJDQ3YzhiNDIzLTk1OWItNDVmMy1hOTc0LWRkNDhhNTQyZTY3N9gCBuACAQ%26sid%3Dca5360fefe66e82e8f5833cf7345f576%26click_from_hp_logo%3D1%3Bsb_price_type%3Dtotal%3Bsrpvid%3D87687b2a59350761%26%26&ss=H%E1%BA%A1+Long%2C+Qu%E1%BA%A3ng+Ninh%2C+Vi%E1%BB%87t+Nam&is_ski_area=0&ssne=Ha%CC%80+N%C3%B4%CC%A3i&ssne_untouched=Ha%CC%80+N%C3%B4%CC%A3i&checkin_year=2022&checkin_month=6&checkin_monthday=27&checkout_year=2022&checkout_month=6&checkout_monthday=28&group_adults=1&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1&ac_position=0&ac_langcode=vi&ac_click_type=b&dest_id=-3715715&dest_type=city&place_id_lat=20.9511&place_id_lon=107.08&search_pageview_id=efa47b362fef024c&search_selected=true&ss_raw=Qu%E1%BA%A3ng+Ninh"

list_url = [
    url_Ha_Noi,
    url_Ho_Chi_Minh,
    url_Da_lat,
    url_Da_Nang,
    url_Nha_Trang,
    url_Phu_Quoc,
    url_Vung_Tau,
    url_Quang_Ninh
]

list_range = [40, 40, 30, 32, 21, 13, 25, 14]


for i in range(0, 8):
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get(list_url[i])
    for i in range(0, list_range[i]):
        t1 = driver.find_elements_by_css_selector(
            "a[data-testid='title-link']")
        with open("url_booking_com.txt", 'a', encoding='utf-8') as f:
            for tag in t1:
                f.write(tag.get_attribute('href') + "\n")
        driver.find_element_by_css_selector(
            "button[aria-label='Trang sau']").click()
        sleep(5)
