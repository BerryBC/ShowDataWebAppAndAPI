'''
@Descripttion: 爬虫包
@Author: BerryBC
@Date: 2020-02-18 19:00:21
@LastEditors: BerryBC
@LastEditTime: 2020-02-18 21:59:17
'''

import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def funSpyDataWithTag(strInURL, strInTag):
    try:
        options = Options()

        prefs = {'profile.default_content_setting_values': {'notifications': 2}}
        options.add_experimental_option('prefs', prefs)
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        options.add_argument('--hide-scrollbars')
        options.add_argument('blink-settings=imagesEnabled=false')
        options.add_argument('--headless')
        options.add_argument('--incognito')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--disable-software-rasterizer')
        options.add_argument('--disable-extensions')
        options.add_argument(
            '--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36"')
        options.add_argument('--window-size=1280x1024')
        options.add_argument('--start-maximized')
        options.add_argument('--disable-infobars')

        browserChorme = webdriver.Chrome(
            '/usr/bin/chromedriver', chrome_options=options)
        browserChorme.set_page_load_timeout(10)
        browserChorme.set_script_timeout(10)
        browserChorme.implicitly_wait(20)
        browserChorme.get(strInURL)
        strhtml = browserChorme.page_source
        browserChorme.close()
        browserChorme.quit()
        soup = BeautifulSoup(strhtml, 'lxml')
        arrWebP = soup.select(strInTag)
        strPContent = ''
        for eleP in arrWebP:
            strPContent += eleP.get_text().strip()+'\n'
        return None,strPContent
    except Exception as e:
        return str(e), str(' Error of MongoDB at "funDeleteOldPage" ' + time.strftime('%Y-%m-%d %H:%M:%S'))
