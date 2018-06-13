from urllib.request import urlopen,urlretrieve
from bs4 import BeautifulSoup
from pyexcel import *

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
html_content = urlopen(url).read().decode("utf-8")

#beautifulsoup
soup = BeautifulSoup(html_content,"html.parser")

tab = soup.find("table",attrs={"id": "tblGridData"})
td_list = tab.find_all("td",attrs={"class": "h_t"})
td = []
for t in td_list:
    td.append(t.string.replace("\r\n","").strip())
# print(td)

tab2 = soup.find("table",attrs={"id": "tableContent"})
td2_list = tab2.find_all("td",attrs={"class": "b_r_c"})
data_list = []
for i in range (0,len(td2_list),6):
    data={}
    data['Content'] = td2_list[i].string.strip()
    data[td[0]] = td2_list[i+1].string
    data[td[1]] = td2_list[i+2].string
    data[td[2]] = td2_list[i+3].string
    data[td[3]] = td2_list[i+4].string
    data_list.append(data)
    
save_as(records=data_list, dest_file_name="vnm.xls")