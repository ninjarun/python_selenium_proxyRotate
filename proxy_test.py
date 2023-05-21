import json
import random
import time
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Browser:
    browser, service = None, None
    proxies=[]

    # Initialise the webdriver with the path to chromedriver.exe
    def __init__(self, driver: str, proxies: list):
        try:
            self.service = Service(driver)
            self.proxies = proxies
            self.rotate_proxy()
            print('Browser successfully initialized')
        except Exception as e:
            print(f'Error initializing browser: {str(e)}')

    def rotate_proxy(self):
        proxy = random.choice(self.proxies)
        print('proxy select:',proxy)
        proxy_host, proxy_port = proxy

        # Configure proxy settings
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument(f'--proxy-server={proxy_host}:{proxy_port}')

        self.browser = webdriver.Chrome(service=self.service, options=chrome_options)

    def open_page(self, url: str):
        self.browser.get(url)

    def close_browser(self):
        self.browser.close()

    def add_input(self, by: By, value: str, text: str):
        field = self.browser.find_element(by=by, value=value)
        field.send_keys(text)
        time.sleep(1)

    def click_button(self, by: By, value: str):
        button = self.browser.find_element(by=by, value=value)
        button.click()
        time.sleep(1)

    def login(self, username: str, password: str):
        self.add_input(by=By.ID, value='Username', text=username)
        self.add_input(by=By.ID, value='Password', text=password)
        self.click_button(by=By.CSS_SELECTOR, value='.btnregister.submit')




def Main():
    proxies = [
        ('158.160.56.149', 8080),
        # ('190.61.88.147', 8080)
    ]

    browser = Browser('/home/test/pythoncourse/CHROME_DRIVER/chromedriver',proxies)
    browser.open_page('https://www.whatismyip.com')
    time.sleep(3)



if __name__ == '__main__':
    Main()
    