from selenium import webdriver
import pandas as pd
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

names = []
state = []
price = []
rooms = []
area = []

for i in range(1,42):
    driver.get(f'https://www.pararius.com/apartments/amsterdam/page-{i}')
    time.sleep(9)
    home_holder = driver.find_elements_by_xpath("//li[contains(@class,'search-list__item search-list__item--listing')]")
    for home in home_holder:
        home_name = home.find_element_by_xpath(".//a[contains(@class,'listing-search-item__link listing-search-item__link--title')]").text
        names.append(home_name)
        print(home)
        home_price = home.find_element_by_xpath(".//div[contains(@class,'listing-search-item__price')]").text.replace('€','')
        price.append(home_price)
        location = home.find_element_by_xpath(".//div[contains(@class,'listing-search-item__location')]").text
        state.append(location)
        size = home.find_element_by_xpath(".//li[contains(@class,'illustrated-features__item illustrated-features__item--surface-area')]").text
        area.append(size)
        chambers = home.find_element_by_xpath(".//li[contains(@class,'illustrated-features__item illustrated-features__item--number-of-rooms')]").text
        rooms.append(chambers)
        
        
        
        
homes = pd.DataFrame(
    {
        "name":names,
        'state':state,
        'price in €':price,
        'rooms':rooms,
        'size':area,
    }
)
print(homes)
    
driver.close()
homes.to_csv('Armsterdamhomes.csv')