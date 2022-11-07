from PIL import Image, ImageFilter
from loguru import logger
import os
import random


def create_rez(list_fon, list_rez):
    im_fon = Image.open(f'фон/{list_fon}')
    im_rez = Image.open(f'результаты/фэм/{list_rez}')
    im_rez_text = Image.open('маска/Rezult_text.png')
    im_filter = Image.open('маска/filtr.png').convert("RGBA")
    im_filter_small = Image.open('маска/filtr_small.png').convert("RGBA")
    im_logo = Image.open('маска/logo_fem.png').convert("RGBA")
    im_voda = Image.open('маска/zfemruolga.png').convert("RGBA")
    im_under = Image.open('маска/zfemruolga_under.png').convert("RGBA")


    width, height = (800, 525)
    # print(im_mask.size)
    width_rez, height_rez = im_rez.size
    # print(width_rez, height_rez)
    #im_fon = im_fon.filter(ImageFilter.BLUR)
    im_fon = im_fon.resize((width, height))
    if height_rez < 65:
        im_rez = im_rez.resize((width, 40))
        im_voda.resize((width_rez, height_rez))
        im_rez.paste(im_voda,(200,5), im_voda)
    elif 65 <= height_rez <= 100:
        im_rez = im_rez.resize((width, 60))
        im_voda.resize((width_rez, height_rez))
        im_rez.paste(im_voda, (200,15), im_voda)
    else:
        im_rez = im_rez.resize((width, 100))
        im_voda.resize((width_rez, height_rez))
        im_rez.paste(im_voda, (200,35), im_voda)

    # print(im_rez.size)
    im_fon.paste(im_filter, (0, 0), im_filter)
    im_fon.paste(im_filter_small, (0, 110), im_filter_small)
    im_fon.paste(im_rez, (0,height//2))
    # im_fon.paste(im_voda,(10,290), im_voda)
    im_fon.paste(im_rez_text, (100, 146))
    im_fon.paste(im_logo, (25,30), im_logo)
    im_fon.paste(im_under, (25,485), im_under)

    im_fon.save(f'rezults/{list_rez}+{list_fon}', quality = 95)
    return logger.info(f"Картинка {list_fon}+{list_rez} создана")


list_fon = os.listdir("фон/")
list_rez = os.listdir("результаты/фэм/")

for i in range(len(list_rez)):
    random.shuffle(list_fon)
    create_rez(random.choice(list_fon), list_rez[i])

