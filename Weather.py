def runWeather():
    

    # import these libraries
    import urllib.request
    from bs4 import BeautifulSoup
    from weatherturt import turtlefun

    from PIL import Image
    from PIL import ImageDraw
    from PIL import ImageFont

    import ILI9341 as tft
    import Adafruit_GPIO as GPIO
    import Adafruit_GPIO.SPI as SPI
    from TFTTextFxn import drawtext

    PITFT_2_8=18
    PITFT_2_2=25

    CURRENT_PITFT=PITFT_2_8

    #pi config
    DC=CURRENT_PITFT
    RST=23
    SPI_PORT=0
    SPI_DEVICE=0


    #choose the url to pull data from
    weatherpage='https://weather.com/weather/today/l/65409:4:US'
    setipage='https://setiathome.berkeley.edu/nebula/multiplets.php?s6=0&type=0&bary=1&nonbary=0&adj=0&offset=0'
    
    #ask website and return the html t the variable 'weatherhtml'
    weatherhtml=urllib.request.urlopen(weatherpage)
    setihtml=urllib.request.urlopen(setipage)

    #parse the html with BS and put it in 'soup'
    soup=BeautifulSoup(weatherhtml,'html.parser')
    soup2=BeautifulSoup(setihtml,'html.parser')

    #=========================================Temperature=========================================
    #Take out <div> of temp and get its value
    tempbox=soup.find('div', attrs={'class':'today_nowcard-temp'})

    #Bad parsing, but it works.
    tempstr=str(tempbox)
    temp1=tempstr[47]
    temp2=tempstr[48]
    temp=int(temp1+temp2)
    #=======================================Feels Like==============================================
    #Get the data I need from the html, put into 'feelsbox'
    feelsbox=soup.find('span', attrs={'classname':'deg-feels'})
    feelsstr=str(feelsbox)
    feels1=feelsstr[46]
    feels2=feelsstr[47]
    feels=int(feels1+feels2)
    #=======================================Chance of Preciipitation================
    precipbox=soup.find('span',attrs={'class':'precip-val'})
    precipstr=str(precipbox)
    precip1=precipstr[54]
    precip2=precipstr[55]
    if precip2=='<':
        precip=0
    else:
        precip=int(precip1+precip2)
    
    #========================================Humidity==================================
    humid=soup.find('tr').find_next_sibling().findChild('td').text

    #=================================seti============at night==================
    table=soup2.find('td', attrs={'':''})
    score=(table.find_next_sibling())
    singletype=(score.find_next_sibling())
    baryunbary=(singletype.find_next_sibling())
    pixel=(baryunbary.find_next_sibling())
    numofsigs=(pixel.find_next_sibling())
    #turtle function

    print('yeet')
    turtlefun(temp, feels, precip, humid, score.text, singletype.text, pixel.text)
    tempbyte=bytes(temp)
    """
    #create class
    disp=tft.ILI9341(DC, rst=RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=64000000))

    #Initialize
    disp.begin()

    #clear and set to black, also make 'draw' an object???
    disp.clear()
    draw=disp.draw()

    #choose font. Must be TTF font Example: font=ImageFont.truetype('Minecraftia.ttf', 16)
    font=ImageFont.load_default()

    #run the 'write' function to put all the data pulled from the website
    drawtext(disp.buffer, tempstr, (150,120), 90, font, fill=(255,255,255))
    drawtext(disp.buffer, feelsstr, (170,120), 90, font, fill=(255,255,255))
    drawtext(disp.buffer, precipstr, (190,120), 90, font, fill=(255,255,255))
    drawtext(disp.buffer, humidstr, (210, 120), 90, font, fill=(255,255,255))
    disp.display()
    """
