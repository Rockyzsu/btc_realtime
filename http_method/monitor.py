# -*- coding: UTF-8 -*-
"""
@author:xda
@file:monitor.py
@time:2021/01/08
"""
import datetime

import requests
import json
import os
import time

# update btc price every 10s
INTERVAL = 10

class BTCPrice():

    def __init__(self):
        file = 'config.json'
        # print(os.getcwd())
        path = os.path.join(self.path, file)
        self.config = self.read_config(path)

    @property
    def path(self):
        return os.path.dirname(os.path.abspath(__file__))

    def get(self):
        resp = requests.get(
            url=self.config['url'],
            headers=self.config['headers'])
        if resp.status_code == 200:
            return resp.json()
        else:
            return []

    @property
    def data(self):
        data = self.get()
        if data:
            return self.price(data)
        else:
            return None

    def display(self):
        while True:
            print(f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} : ',self.data)
            time.sleep(INTERVAL)

    def price(self,row):
        return row['status']['summery']['curr']

    def read_config(self, file):
        with open(file, 'r') as f:
            return json.load(f)


if __name__=='__main__':
    btc = BTCPrice()
    btc.display()