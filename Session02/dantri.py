from urllib.request import urlopen,urlretrieve
from bs4 import BeautifulSoup

url = "http://dantri.com.vn"

#1. Download web page
# #1.1 Create a connection
conn = urlopen(url)
# #1.2 Read
data = conn.read()

# #1.3 Decode
html_content = data.decode("utf-8")
# print(html_content)

#save html_content to file
  
# urlretrieve(url, "test.html")

# title_name = title_box.text
# print(title_name)


# f = open("dantri.html", "w")
# f.write(html_content)
# f.close()

#2. Extract ROI (Region of interest)
#beautifulsoup
soup = BeautifulSoup(html_content,"html.parser")
# print(soup.prettify())
ul = soup.find('ul',attrs={'class': 'ul1'})

li_list = ul.find_all("li")
for li in li_list:
    # print(li.prettify())
    # print()
    # h4 = li.find("h4")
    # a = h4.find("a")
    a = li.h4.a
    # print(a.prettify())
    print(a.string)
    print(url + a['href'])

#3. Extract info