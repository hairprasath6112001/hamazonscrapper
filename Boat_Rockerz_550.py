#!/usr/bin/env python3
from scrapper import Scrapper
from discord import Discord

url = "https://www.amazon.in/dp/B0856HNLDK/ref=twister_B0859XSFF6?_encoding=UTF8&psc=1"
headers = 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'
dis_url = "https://discordapp.com/api/webhooks/779391429960531978/9iej5a0xP-GpvwsrbHIwHOXTT48oMWNVnbo5kDC5WcqDXjuigBKeb2qQq_RcfLP4m6Ur"

try:
    myscrapper = Scrapper("Boat Rockerz 550", url, headers, dis_url)
    myscrapper.get_price()
except:
    er_dis = Discord(dis_url)
    er_dis.msg("Program Stoppped")