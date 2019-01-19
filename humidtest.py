import urllib.request
from bs4 import BeautifulSoup
from weatherturt import turtlefun

#choose the url to pull data from
weatherpage='https://weather.com/weather/today/l/65619:4:US'

#ask website and return the html t the variable 'weatherhtml'
weatherhtml=urllib.request.urlopen(weatherpage)

#parse the html with BS and put it in 'soup'
soup=BeautifulSoup(weatherhtml,'html.parser')

humidbox=soup.find('tr')
humid1=humidbox.find_next_sibling()
humid2=humid1.findChild('td').text
print(humidbox)
print(humid1)
print('----')
print(humid2)
