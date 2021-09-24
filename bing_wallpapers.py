#!/usr/bin/env python
# -- coding: utf-8 --

import os
import re

import requests

url = "https://www.bing.com/"

name = re.compile("url\(/th\?id=(.*?\.jpg)").search(requests.get(url).text).group(1)

address = url + "th?id=" + name

with open(os.path.join(os.getcwd(), "wallpapers", name), "wb") as f:
    f.write(requests.get(address).content)
