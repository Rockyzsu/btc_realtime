# -*- coding: UTF-8 -*-
"""
@author:xda
@file:main.py
@time:2021/01/08
"""
from http_method.monitor import BTCPrice
def main():
    btc = BTCPrice()
    btc.display()

if __name__ == '__main__':
    main()
