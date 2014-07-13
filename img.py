from PIL import Image, ImageDraw, ImageFont

def createicon(s, c):
    img = Image.new('RGBA', (16, 16))
    ImageDraw.Draw(img).text((1, -3), s,
        font=ImageFont.truetype('consola.ttf', 25), fill=c)
    img.save('i16.png')

    img = Image.new('RGBA', (32, 32))
    ImageDraw.Draw(img).text((2, -5), s,
        font=ImageFont.truetype('consola.ttf', 50), fill=c)
    img.save('i32.png')

# s, c = 'F', (64, 96, 128)
# s, c = 'R', (212, 255, 0)
# createicon(s, c)

img = Image.new('RGBA', (300, 200))
ImageDraw.Draw(img).text((118, 92), '開発中！',
    font=ImageFont.truetype('meiryo.ttc', 16, encoding='utf-8'), fill=(0, 0, 0))
img.save('dev.png')
