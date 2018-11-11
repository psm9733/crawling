import os
import sys
import time
from bs4 import BeautifulSoup
from selenium import webdriver

class Collection_Tool():
    def __init__(self):
        print ('__Collection_Tool Create__')
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.implicitly_wait(1000)

    def SetUrl(self, url):
        self.url=url
        self.driver.get(url)
        time.sleep(3)

    def getSource(self):
        self.source = self.driver.page_source
        self.soup = BeautifulSoup(self.source, 'html.parser')
        return self.source

    def getList(self):
        list_source = self.soup.find_all('li', {'class' : 'trip_result_item'})
        self.number = len(list_source)
        for index in range(self.number):
            list_item = list_source[index]
            # print(list_item)
            # print("항공사: ", list_item.find('span').string)
            print("항공사: ", list_item.find('span', {'class' : 'h_tit_result ng-binding'}).string)
            print("출발지: ", list_item.findAll('dd', {'class' : 'txt_code ng-binding'})[0].string)
            print("출발시간: ", list_item.findAll('dd', {'class' : 'txt_time ng-binding'})[0].string)
            print("도착지: ", list_item.findAll('dd', {'class' : 'txt_code ng-binding'})[1].string)
            print("도착시간: ", list_item.findAll('dd', {'class' : 'txt_time ng-binding'})[1].string)
            print("소요시간: ", list_item.findAll('dd', {'class' : 'txt_time ng-binding'})[2].string)
            print("왕복/편도: ", list_item.find('div', {'class' : 'txt_total'}).string)
            print("어린이/성인: ", list_item.find('span', {'class' : 'txt_pay ng-binding'}).string)
            print("가격: ", list_item.find('span', {'class' : 'txt_pay ng-binding'}).string)
            print("------------------------")

    def Finish(self):
        print ('__Collection_Tool Quit__')
        self.driver.quit()

if __name__ == "__main__":
    url = 'https://store.naver.com/flights/results/domestic?trip=OW&fareType=YC&scity1=GMP&ecity1=CJU&adult=1&child=0&infant=0&sdate1=2018.11.14.'
    tool = Collection_Tool()
    tool.SetUrl(url)
    tool.getSource()
    tool.getList()
    tool.Finish()
