# import these libraries
import urllib.request
from bs4 import BeautifulSoup
setipage='https://setiathome.berkeley.edu/nebula/multiplets.php?s6=0&type=0&bary=1&nonbary=0&adj=0&offset=0'
#ask website and return the html t the variable 'weatherhtml'
setihtml=urllib.request.urlopen(setipage)

#parse the html with BS and put it in 'soup'
soup=BeautifulSoup(setihtml,'html.parser')

table=soup.find('td', attrs={'':''})
score=table.find_next_sibling()
singletype=score.find_next_sibling()
baryunbary=singletype.find_next_sibling()
pixel=baryunbary.find_next_sibling()
numofsigs=pixel.find_next_sibling()
print(table)
print('==============================')
print(score.text)
print('--------------------')
print(singletype.text)
print('---------------------')
print(baryunbary.text)
print('---------------------')
print(pixel.text)
print('---------------------')
print(numofsigs.text)
