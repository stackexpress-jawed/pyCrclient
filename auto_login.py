#!/usr/bin/env python

import requests
import configs
import time
from urllib.parse import urljoin
import re


MODE_LOGIN=191
MODE_LOGOUT=193
MODE_LIVE=192

HEADERS =  {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:73.0) Gecko/20100101 Firefox/73.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Connection': 'keep-alive'
    }

def keep_live():
    LIVE_URL = urljoin(configs.BASE_URL, 'live')
    data = dict()
    data.update(
            mode=MODE_LIVE,
            username=configs.USERNAME,
            a=int(time.time()),
            producttype=0,
        )
    while True:
        print("wait...")
        time.sleep(150)
        print("[ %s ] : Keep user - %s active" %(time.strftime("%H:%M:%S"), data['username']))
        data.update(a=int(time.time()))
        response = requests.get(LIVE_URL, params=data, headers=HEADERS)
        print(response)

def login():
    LOGIN_URL = urljoin(configs.BASE_URL, 'login.xml')
    data = dict()
    data.update(
        mode=MODE_LOGIN,
        username=configs.USERNAME,
        password=configs.PASSWORD,
        a=int(time.time()),
        producttype=0,
    )

    response = requests.post(LOGIN_URL, data=data, headers=HEADERS)

    if re.search("You have successfully logged in", response.text):
        # keep user active
        print(response.text)
        keep_live()
    else:
        print("Unable to login !!")
        print(response.text)

def logout():
    LOGOUT_URL = urljoin(configs.BASE_URL, 'logout.xml')
    data = dict()
    data.update(
        mode=MODE_LOGOUT,
        username=configs.USERNAME,
        password=configs.PASSWORD,
        a=int(time.time()),
        producttype=0,
    )

    response = requests.post(LOGOUT_URL, data=data, headers=HEADERS)
    print(response.text)

if __name__ == "__main__":
    # logout if user is already logged in
    logout()
    # login the user
    login()
    
