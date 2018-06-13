from urllib.request import urlopen,urlretrieve
from bs4 import BeautifulSoup
from pyexcel import *
from youtube_dl import YoutubeDL

url = "https://www.apple.com/itunes/charts/songs"

html_content = urlopen(url).read().decode("utf-8")

#beautifulsoup
soup = BeautifulSoup(html_content,"html.parser")
# print(soup.prettify())

sec = soup.find("section",attrs={"class": "section chart-grid"})
# print(div.prettify())
# ul = div.find("ul")

li_list = sec.find_all("li")
song_list = []
options = {
    'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
    'max_downloads': 1 # Tell downloader to download only the first entry (video)
    }
dl = YoutubeDL(options)
for li in li_list:
    song_dict = {}
    h3 = li.h3 #song
    song_dict["name"] = h3.string
    h4 = li.h4 #artist
    song_dict["artist"] = h4.string
    song_list.append(song_dict)
    dl.download([h3.string + "-" + h4.string])
# print(song_list)

# save_as(records = song_list, dest_file_name = 'itunes.xls')