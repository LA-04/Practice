from PIL import Image, ImageFilter
from loguru import logger
import os
import random


def create_rez_fem(list_fon, list_rez_fem):
    im_fon = Image.open(f'фон/{list_fon}')
    im_rez_fem = Image.open(f'результаты/фэм/{list_rez_fem}')
    im_rez_text = Image.open('маска/fem/Rezult_text.png')
    im_filter = Image.open('маска/fem/filtr.png').convert("RGBA")
    im_filter_small = Image.open('маска/fem/filtr_small.png').convert("RGBA")
    im_logo = Image.open('маска/fem/logo_fem.png').convert("RGBA")
    im_voda = Image.open('маска/fem/zfemruolga.png').convert("RGBA")
    im_under = Image.open('маска/fem/zfemruolga_under.png').convert("RGBA")


    width, height = (800, 525)
    # print(im_mask.size)
    width_rez, height_rez = im_rez_fem.size
    # print(width_rez, height_rez)
    #im_fon = im_fon.filter(ImageFilter.BLUR)
    im_fon = im_fon.resize((width, height))
    if height_rez < 70:
        im_rez_fem = im_rez_fem.resize((width, 40))
        im_voda.resize((width_rez, height_rez))
        im_rez_fem.paste(im_voda, (200, 5), im_voda)
    elif 70 <= height_rez <= 100:
        im_rez_fem = im_rez_fem.resize((width, 60))
        im_voda.resize((width_rez, height_rez))
        im_rez_fem.paste(im_voda, (200, 15), im_voda)
    elif 100 < height_rez <= 120:
        im_rez_fem = im_rez_fem.resize((width, 80))
        im_voda.resize((width_rez, height_rez))
        im_rez_fem.paste(im_voda, (200, 15), im_voda)
    else:
        im_rez_fem = im_rez_fem.resize((width, 100))
        im_voda.resize((width_rez, height_rez))
        im_rez_fem.paste(im_voda, (200, 35), im_voda)

    # print(im_rez_fem.size)
    im_fon.paste(im_filter, (0, 0), im_filter)
    im_fon.paste(im_filter_small, (0, 110), im_filter_small)
    im_fon.paste(im_rez_fem, (0, height // 2))
    # im_fon.paste(im_voda,(10,290), im_voda)
    im_fon.paste(im_rez_text, (100, 146))
    im_fon.paste(im_logo, (25,30), im_logo)
    im_fon.paste(im_under, (25,485), im_under)

    im_fon.save(f'rezults/fem/{list_rez_fem}+{list_fon}', quality = 95)
    return logger.info(f"Картинка {list_fon}+{list_rez_fem} создана")


def create_rez_vitte(list_fon, list_rez_vitte):
    im_fon = Image.open(f'фон/{list_fon}')
    im_rez = Image.open(f'результаты/витте/{list_rez_vitte}')
    im_stock = Image.open('маска/vitte/stock.png')
    im_header = Image.open('маска/vitte/header.png').convert("RGBA")
    im_filter = Image.open('маска/vitte/filtr.png').convert("RGBA")
    im_voda = Image.open('маска/vitte/vittetests.png').convert("RGBA")
    im_under = Image.open('маска/vitte/vittetests_under.png').convert("RGBA")

    width, height = (800, 525)

    width_rez, height_rez = im_rez.size

    # im_fon = im_fon.resize((800, 400))
    im_fon = im_fon.crop((0,100, 800, 500))

    # if height_rez < 65:
    #     im_rez = im_rez.resize((width, 40))
    #     im_voda.resize((width_rez, height_rez))
    #     im_rez.paste(im_voda,(200,5), im_voda)
    # elif 65 <= height_rez <= 100:
    #     im_rez = im_rez.resize((width, 60))
    #     im_voda.resize((width_rez, height_rez))
    #     im_rez.paste(im_voda, (200,15), im_voda)
    # else:
    #     im_rez = im_rez.resize((width, 100))
    #     im_voda.resize((width_rez, height_rez))
    #     im_rez.paste(im_voda, (200,35), im_voda)

    im_rez = im_rez.resize((700, 150))
    im_voda.resize((width_rez, height_rez))
    im_rez.paste(im_voda, (200, 35), im_voda)

    im_stock.paste(im_fon, (0, 100), im_fon)
    im_stock.paste(im_filter, (0, 100), im_filter)
    im_stock.paste(im_rez, (50,(height - 150 )//2))
    im_stock.paste(im_header, (0, 0), im_header)
    im_stock.paste(im_under, (25,505), im_under)

    im_stock.save(f'rezults/vitte/{list_rez_vitte}+{list_fon}', quality = 95)
    return logger.info(f"Картинка {list_fon}+{list_rez_vitte} создана")

list_fon = os.listdir("фон/")
list_rez_fem = os.listdir("результаты/фэм/")
list_rez_vitte = os.listdir("результаты/витте/")

# for i in range(len(list_rez_fem)):
#     random.shuffle(list_fon)
#     create_rez_fem(random.choice(list_fon), list_rez_fem[i])

for i in range(len(list_rez_vitte)):
    random.shuffle(list_fon)
    create_rez_vitte(random.choice(list_fon), list_rez_vitte[i])
    # create_rez_vitte(random.choice(list_fon), list_rez_vitte[1])