from selenium import webdriver
import colorama
from colorama import Fore, Back, Style
import os,time,re,re

colorama.init()

keyword = input("Keyword : ")

DRIVER_PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get(f'https://www.google.com/search?q={keyword}+pastebin')

time.sleep(5)

#Get googles contents
driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[9]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div[1]/a/h3').click()
time.sleep(5)
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/a[1]').click()
time.sleep(5)
get_content = driver.find_element_by_xpath('/html/body/pre')
print(Fore.GREEN + f"""
Heres your paste content:
----------------------------
{get_content.text}
----------------------------
""")