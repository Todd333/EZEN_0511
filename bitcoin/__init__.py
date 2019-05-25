from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
from fbprophet import Prophet
from urllib.request import urlopen

if __name__ == '__main__':
    # driver = webdriver.Chrome('chromedriver')
    # url = 'https://bitcoincharts.com/charts/korbitKRW#rg730ztgSzm1g10zm2g25zv'
    # driver.get(url)
    # xpath = """//*[@id="content_chart"]/div/div[2]/a"""
    # variable = driver.find_element_by_xpath(xpath)
    # driver.execute_script("return arguments[0].scrollIntoView();", variable)
    # variable.click()
    # # 그 메뉴가 보일 때까지 스크롤해서 내려가서 클릭하라
    # html = driver.page_source
    # soup = BeautifulSoup(html, 'html.parser')
    # # print(soup.prettify())
    # table =soup.find("table", {"id": "chart_table"})  #필요데이터를 뽑아오는 장소
    # print(str(table))




    url = "https://bitcoincharts.com/charts/chart.json?m=korbitKRW&SubmitButton=Draw&r=730&i=&c=0&s=&e=&Prev=&Next=&t=S&b=&a1=&m1=10&a2=&m2=25&x=0&i1=&i2=&i3=&i4=&v=1&cv=0&ps=0&l=0&p=0&"
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    # print(soup.prettify())
    df = pd.read_json(soup.prettify())
    print(df)
