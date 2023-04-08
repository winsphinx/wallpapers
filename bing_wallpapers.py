import os
import re

import requests

URL = "https://www.bing.com/"
NAME = re.compile("Wallpaper\":\"/th\?id=(.*?_1920x1200.jpg)").search(requests.get(URL).text).group(1)
ADDRESS = URL + "th?id=" + NAME

with open(os.path.join(os.getcwd(), "wallpapers", NAME), "wb") as f:
    f.write(requests.get(ADDRESS).content)
