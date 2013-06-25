import urllib.request
from bs4 import BeautifulSoup


webpage = urllib.request.urlopen("http://www.cwb.gov.tw/V7/forecast/f_index.htm?_=1370160314196") #讀取氣象局網站原始碼
soup = BeautifulSoup(webpage.read().decode("utf8"))	#利用 BeautifulSoup 函式庫解析

webtext = soup.get_text().strip().split()	#獲取原始碼中的所有純文字內容放入 list 中

weather = []
for image in soup.find_all('img'):			#尋找 img 標籤的式子，取得 alt 的值，丟入 list 中
	weather.append(image.get('alt',''))


#print(webtext) #所有純文字
#print(webtext[12],webtext[34],webtext[53],webtext[63],webtext[73])	#五大地區分類
count = 13
CountWeather = 0
print(webtext[12])
while count < len(webtext):
	print(webtext[count],webtext[count+1],webtext[count+2],weather[CountWeather])
	count+=3
	CountWeather+=1
	if CountWeather == 13:
		CountWeather+=24
	if count == 34 or count == 53 or count == 63 or count ==73:
		print(webtext[count])
		count+=1

