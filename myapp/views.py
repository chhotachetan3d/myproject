from django.shortcuts import render
from django.http import HttpResponse
from requests import Session
import requests
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver   # for webdriver
from selenium.webdriver.support.ui import WebDriverWait  # for implicit and explict waits
from selenium.webdriver.chrome.options import Options  # for suppressing the browser

# Create your views here.
def student_show(request):

   main_page = "https://beef.center.kobe-u.ac.jp/2020/"
   message_page = "https://beef.center.kobe-u.ac.jp/2020/message/index.php"     
   option = webdriver.ChromeOptions()
   option.add_argument('headless')
   driver = webdriver.Chrome('D:\chetan\python\chromedriver',options=option) 
   driver.get("https://beef.center.kobe-u.ac.jp/login/index.php")
   driver.find_element_by_id("j_username").send_keys('1862695b')
   driver.find_element_by_id("j_password").send_keys('k=MU9rXs')
   driver.find_element_by_name("_eventId_proceed").click()
   sleep(1)
   driver.get(message_page)
   #driver.find_element_by_id("nav-message-popover-container").click()
   #driver.find_element_by_class_name("see-all-link").click()
   base_url = driver.current_url
   #sleep(1)
   
   #with Session() as s:
   #    site = s.get(base_url)
   #    p = s.post(LOGIN_URL, data=payload)

   #    driver.close() 
   #with Session() as s:
   # site = s.get("https://beef.center.kobe-u.ac.jp/login/index.php")
   # bs_content = bs(site.content, "html.parser")
   # login_data = {"j_username":"1862695b","j_password":"k=MU9rXs"}
   # svr = s.post("https://idp.center.kobe-u.ac.jp/idp/profile/SAML2/Redirect/SSO?execution=e5s1",login_data)
   # home_page = s.get("https://beef.center.kobe-u.ac.jp/2020/")
    #print(home_page.content)
    #print(site.content) 

   #return HttpResponse(home_page.content)
   #with requests.Session() as s:
   #p = s.post(LOGIN_URL, data=payload)
    # print the html returned or something more intelligent to see if it's a successful login page.
    #print p.text

    # An authorised request.
    #r = s.get(DASHBOARD_URL)
    #print r.text
        # etc... 
     
   html = driver.page_source.encode('utf-8')
   soup = BeautifulSoup(html, 'html.parser')
   results = soup.find_all(class_='contacts-area') 
     
   return HttpResponse(results)
