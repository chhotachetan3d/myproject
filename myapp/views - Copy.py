from django.shortcuts import render
from django.http import HttpResponse
from requests import Session
import requests
from bs4 import BeautifulSoup

# Create your views here.
def student_show(request):
   #x = []
   #for i in range(10):
   #    x.append(i)
   #var1 = "<h1>DataFlair Django Tutorials</h1>The Digits are {0}".format(x)   
   var2 = "<h2>This first Code</h2>" 
     
   payload = {
    'j_username': '1862695b',
    'j_password': 'k=MU9rXs',
    'SAMLResponse': 'hZJdT4MwFIb%2FCuk9FLowlmaQ4HbhkqnLmF54Y0o5uCprsaf48e9lY%2BpMzLxtT5%2F3vE86RbFrWp53bqvX8NIBOu9912jkh4uUdFZzI1Ah12IHyJ3kRX615CwIeWuNM9I0xMsRwTpl9Mxo7HZgC7CvSsLtepmSrXMtckpLgDqQoB3Y4NmU4HeBkMFTS4utKkvTgNsGiIbu%2BYyubooN8eb9QkqLPfoHpKr2T05%2FTvudatXAEbKGSlmQjhbFDfEW85Q8RLWUbBJHTNQVsLAuk7BmkySuyiROqnjcjyF2sNDohHYpYSGL%2FJD5bLyJRnwU8zi%2BJ97qWP1C6Urpx%2FOeymEI%2BeVms%2FKHYndg8VCqHyDZdG%2BbH4Ltif%2FzWPElnWT%2FKsZvxT62U3oSN2S3%2FLrnL%2BYr0yj54eVNY95mFoSDlESEZsOT3x8l%2BwQ%3D',
    'RelayState': 'ss%3Amem%3A2d5060f40803d1eb2d3e5b4ea7c2318b95298943c9e4d8d3dbb0d37812aebf11',
    
}

   #LOGIN_URL     = "https://idp.center.kobe-u.ac.jp/idp/profile/SAML2/Redirect/SSO?execution=e11s1"
   LOGIN_URL     = "https://beef.center.kobe-u.ac.jp/Shibboleth.sso/SAML2/POST"
   #LOGIN_URL     = "https://beef.center.kobe-u.ac.jp/2020/auth/shibboleth/index.php"
   DASHBOARD_URL = "https://beef.center.kobe-u.ac.jp/2020/"

   with Session() as s:
       site = s.get("https://beef.center.kobe-u.ac.jp/2020/auth/shibboleth/index.php")
       p = s.post(LOGIN_URL, data=payload)

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
   
       return HttpResponse(p.content)
