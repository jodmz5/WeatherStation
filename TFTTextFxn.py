def drawtext(image, text, position, angle, font, fill=(255,255,255)):
    draw=ImageDraw.Draw(image)
    width, height=draw.textsize(text, font=font)
    textimage=Image.new('RGBA', (width, height), (0,0,0,0))
    textdraw=ImageDraw.Draw(textimage)
    textdraw.text((0,0),text,font=font,fill=fill)
    rotated = textimage.rotate(angle, expand=1)
    image.paste(rotated, position, rotated)
