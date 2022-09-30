#!/usr/bin/python
import requests
import bs4
import tqdm
a = requests.get("https://pypi.tuna.tsinghua.edu.cn/simple").text
b = bs4.BeautifulSoup(a, "lxml")
s = b.find_all("a")
with open("pypi.txt", "w") as f:
   for i in tqdm.tqdm(range(len(s)), total=len(s), desc="进度"):
       f.write(str(s[i].text )+ "\n")
