#!/usr/bin/env python3
import time
import requests
from bs4 import BeautifulSoup
from discord import Discord

class Scrapper:
    def __init__(self, Pname, url, headers, discord_url):
        self.url = url
        self.headers = {"User-Agent": headers}
        self.Pname = Pname
        self.desc = "Price Checking..."
        self.webhook_url = discord_url

    def send_report(self, PPrice):
        mydiscord = Discord(self.webhook_url)
        mydiscord.send_msg(self.Pname, self.desc, "Price", "₹" + str(PPrice))

    def check_price(self, price):
        self.send_report(price)

    def get_price(self):
        modified_price = ''
        page = requests.get(self.url, headers=self.headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        price = soup.find(id='priceblock_ourprice').get_text()
        for i in range(len(price)):
            if price[i] == '₹' or price[i] == ' ' or price[i] == ',' or price[i] == '.':
                modified_price = modified_price
            else:
                modified_price = modified_price + price[i]
        self.check_price(modified_price[0:5])