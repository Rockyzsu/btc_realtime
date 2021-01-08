# -*- coding: UTF-8 -*-
"""
@author:xda
@file:monitor.py
@time:2021/01/08
"""
import requests
import json
import os

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

    def data(self):
        data = self.get()
        if data:
            print(self.price(data))

    def price(self,row):
        return row['status']['summery']['curr']

    def read_config(self, file):
        with open(file, 'r') as f:
            return json.load(f)
