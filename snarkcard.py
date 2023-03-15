#!/usr/bin/env python3

import textwrap
from PIL import Image, ImageDraw, ImageFont
from string import ascii_letters

# https://www.alpharithms.com/fit-custom-font-wrapped-text-image-python-pillow-552321/

#480-x 234 Resolution

# Load custom font
font = ImageFont.truetype("Pillow/Tests/fonts/FreeMonoBold.ttf", 24)

textFile = open('quotes.txt', 'r')
lines = textFile.readlines()


for index, text in enumerate(lines):

    # create an image
    img = Image.open(fp='simple-background.jpg', mode='r')
    img = img.resize((800,600))

    # Create DrawText object
    draw = ImageDraw.Draw(im=img)

    avg_char_width = sum(font.getsize(char)[0]
                         for char in ascii_letters) / len(ascii_letters)

    # wrap the words across lines, preserving explicit new-lines
    paragraphs = text.split('\\n')
    text = "\n".join([textwrap.fill(text=p, width=int(img.size[0] * .7 / avg_char_width)) for p in paragraphs])

    # center test on the image
    draw.text(xy=(img.size[0]/2, img.size[1]/2), text=text, font=font, fill='#ffffff', anchor='mm')

    filename = "output/snark-{}.jpg".format(str(index).zfill(3))
    img.save(filename)
