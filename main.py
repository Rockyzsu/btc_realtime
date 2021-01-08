# -*- coding: UTF-8 -*-
"""
@author:xda
@file:main.py
@time:2021/01/08
"""
from http_method.monitor import BTCPrice
def main():
    btc = BTCPrice()
    btc.data()

if __name__ == '__main__':
    main()
