""" this webscraper will use regular 
    expressions to find the title
"""

import re
from urllib.request import urlopen

url = 'http://olympus.realpython.org/profiles/dionysus'
page = urlopen(url)
html = page.read().decode("utf-8")

pattern = '<title.*?>.*?</title.*?>'
match_results = re.search(pattern,html,re.IGNORECASE)
title = match_results.group()
print(title)

#remove html tags
title = re.sub("<.*?>","",title)
print(title)