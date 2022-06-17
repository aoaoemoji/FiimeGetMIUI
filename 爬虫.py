# -*- coding: utf-8 -*-
# @Author: aoao
# @Date:   2022-06-10 09:09:34
# @Last Modified by:   aoao
# @Last Modified time: 2022-06-15 17:49:23

import urllib.request
import urllib.parse
import json
import urllib.error
from lxml import etree
import os


path = os.getcwd()
apath = path + "\\865\\"
vabpath = path + "\\VAB\\"
if os.path.exists(apath) != True:
    os.mkdir(apath)
    with open(apath + "TZJB",'w') as pp:
        print(1)
if os.path.exists(vabpath) != True:
    os.mkdir(vabpath)

# 接口地址
url = "https://miui.511i.cn/?index=rom_list"
headers = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Mobile Safari/537.36'
}
# vab机型数据
d = ['ALIOTH','ELISH','HAYDN','PSYCHE','RENOIR','STAR','THYME','VENUS']
for a in d:
    data = {
        'dh':a,
         # lx参数: 0稳定版,1开发版内测,1b开发版公测
        'lx':'1'
    }
    data = urllib.parse.urlencode(data).encode("utf-8")
    try:
        request = urllib.request.Request(url=url,data=data,headers=headers)
        reponse = urllib.request.urlopen(request)
        contant = etree.HTML(reponse.read().decode("utf-8"))
        list_td = contant.xpath("//td//a[@href]/@href")
        # print(list_td[0]) 获取最新的一个内测版本地址
        with open(vabpath + a + ".txt",'w',encoding='utf-8') as fp:
            fp.write(str(list_td[0]))
        
    except urllib.error.HTTPError:
        print('error:HTTPError')
    except urllib.error.URLError:
        print('error:URLError')

# 865机型数据
h = ['APOLLO','CAS','CMI','LMI','PICASSO','UMI','VANGOGH']
for b in h:
    data = {
        'dh':b,
         # lx参数: 0稳定版,1开发版内测,1b开发版公测
        'lx':'1'
    }
    data = urllib.parse.urlencode(data).encode("utf-8")
    try:
        request = urllib.request.Request(url=url,data=data,headers=headers)
        reponse = urllib.request.urlopen(request)
        contant = etree.HTML(reponse.read().decode("utf-8"))
        list_td = contant.xpath("//td//a[@href]/@href")
        # print(list_td[0]) 获取最新的一个内测版本地址
        with open(apath + b + ".txt",'w',encoding='utf-8') as fp:
            fp.write(str(list_td[0]))
        
    except urllib.error.HTTPError:
        print('error:HTTPError')
    except urllib.error.URLError:
        print('error:URLError')














"""
可选机型代号:
"UMI":小米10
"ANGELICAIN":POCO C3
"BERYLLIUM":POCO F1
"SHIVA":POCO M2
"GRAM":POCO M2 Pro
"CITRUS":POCO M3
"EVERGREEN":POCO M4 Pro 5G
"PHOENIXIN":POCO X2 印度版
"SURYA":POCO X3 NFC
"VAYU":POCO X3 Pro
"MONET":小米10 Lite
"CMI":小米10 Pro
"CAS":小米10 至尊纪念版
"VANGOGH":小米10 青春版
"THYME":小米10S
"VENUS":小米11
"COURBET":小米11 Lite
"STAR":小米11 Pro / Ultra
"RENOIR":小米11 青春版
"AGATE":小米11T
"VILI":小米11T Pro
"LISA":小米11青春活力版
"CUPID":小米12
"ZEUS":小米12 Pro
"PSYCHE":小米12X
"MIONE":小米1S
"TAURUS":小米2A
"ARIES":小米2S
"CANCRO":小米3 / 小米4
"PISCES":小米3 移动版
"LIBRA":小米4C
"FERRARI":小米4i
"AQUA":小米4S
"GEMINI":小米5
"MERI":小米5C
"CAPRICORN":小米5S
"NATRIUM":小米5S Plus
"TIFFANY":小米5X
"SAGIT":小米6
"WAYNE":小米6X
"DIPPER":小米8
"PLATINA":小米8 Lite
"EQUULEUS":小米8 Pro 屏幕指纹版
"SIRIUS":小米8 SE
"URSA":小米8 透明探索版
"CEPHEUS":小米9
"CRUX":小米9 Pro 5G
"GRUS":小米9 SE
"TISSOT":小米A1
"JASMINE":小米A2
"DAISY":小米A2 Lite
"LAUREL":小米A3
"PYXIS":小米CC9 / 小米9 Lite
"TUCANA":小米CC9 Pro / 小米Note 10
"VELA":小米CC9 美图定制版
"LAURUS":小米CC9e
"MONA":小米CIVI
"ZIJIN":小米CIVI 1S
"OXYGEN":小米Max 2
"NITROGEN":小米Max 3
"HYDROGEN":小米Max 标准版
"HELIUM":小米Max 高配版
"LITHIUM":小米MIX
"CHIRON":小米MIX 2
"POLARIS":小米MIX 2S
"PERSEUS":小米MIX 3
"ANDROMEDA":小米MIX 3 5G
"CETUS":小米MIX Fold
"ODIN":小米MIX4
"SCORPIO":小米Note 2
"JASON":小米Note 3
"VIRGO":小米Note 双网通 / 全网通
"LEO":小米Note 顶配版
"TOCO":小米Note10 Lite
"LOTUS":小米Play
"MOCHA":小米平板1
"LATTE":小米平板2
"CAPPU":小米平板3
"CLOVER":小米平板4/Plus
"NABU":小米平板5
"ENUMA":小米平板5 Pro (5G)
"ELISH":小米平板5 Pro (WiFi)
"SELENE":红米10
"DANDELION":红米10A
"FOG":红米10C
"MERLIN":红米10X 4G / 红米Note 9
"ATOM":红米10X 5G
"BOMB":红米10X Pro
"LTE26007":红米2A 标准版
"IDO":红米3 / Pro
"LAND":红米3S
"PRADA":红米4 标准版
"MARKW":红米4 高配版
"ROLEX":红米4A
"SANTONI":红米4X
"ROSY":红米5
"VINCE":红米5 Plus
"RIVA":红米5A
"CEREUS":红米6
"SAKURA":红米6 Pro
"CACTUS":红米6A
"ONCLITE":红米7
"PINE":红米7A
"OLIVE":红米8
"OLIVELITE":红米8A
"OLIVEWOOD":红米8A Pro / 红米8A Dual
"LANCELOT":红米9
"CATTAIL":红米9 (India)
"DANDELION":红米9A / 9AT
"ANGELICA":红米9C
"ANGELICAN":红米9C NFC
"TIARE":红米Go
"DAVINCI":红米K20 / 小米9T
"DAVINCIIN":红米K20 / 小米9T 印度版
"RAPHAEL":红米K20 Pro / 小米9T Pro
"RAPHAELIN":红米K20 Pro 印度版
"RAPHAELS":红米K20 Pro 尊享版
"PHOENIX":红米K30 4G / POCO X2
"PICASSO":红米K30 5G
"LMI":红米K30 Pro / 变焦版 / POCO F2 Pro
"CEZANNE":红米K30 至尊纪念版
"PICASSO48M":红米K30i 5G
"APOLLO":红米K30S 至尊纪念版 / 小米10T / 10T Pro
"ALIOTH":红米K40 / POCO F3
"HAYDN":红米K40 Pro / Pro+ / 小米11i / 小米11X Pro
"ARES":红米K40 游戏增强版 / POCO F3 GT
"MUNCH":红米K40S
"RUBENS":红米K50
"MATISSE":红米K50 Pro
"INGRES":红米K50 电竞版
"LCSH92":红米Note
"MOJITO":红米Note 10
"CAMELLIA":红米Note 10 (China) / POCO M3 Pro
"CAMELLIAN":红米Note 10 5G
"CHOPIN":红米Note 10 Pro
"CHOPIN":红米Note 10 Pro (China) / POCO X3 GT
"ROSEMARY":红米Note 10S
"HERMES":红米Note 2
"KENZO":红米Note 3 全网通版
"HENNESSY":红米Note 3 双网通版
"KATE":红米Note 3 台湾特别版
"NIKEL":红米Note 4 联发科版
"DIOR":红米Note 4G单卡版
"GUCCI":红米Note 4G双卡版
"MIDO":红米Note 4X 高通版
 "WHYRED":红米Note 5 / Pro
"UGGLITE":红米Note 5A 标准版
"UGG":红米Note 5A 高配版
"TULIP":红米Note 6 Pro
"LAVENDER":红米Note 7
"VIOLET":红米Note 7 Pro
"GINKGO":红米Note 8
"BILOBA":红米Note 8 (21年款)
"BEGONIA":红米Note 8 Pro
"BEGONIAIN":红米Note 8 Pro 印度版
"WILLOW":红米Note 8T
"LIME":红米Note 9 4G / 红米9T
"CANNON":红米Note 9 5G
"GAUGUIN":红米Note 9 Pro 5G / 小米10T Lite
"EXCALIBUR":红米Note 9 Pro Max
"CURTANA":红米Note 9S / Pro (India)
"CANNONG":红米Note 9T 5G
"SPES":红米Note11
"SELENES":红米Note11 4G
"EVERGO":红米Note11 5G
"SPESN":红米Note11 NFC
"VIVA":红米Note11 Pro
"PISSARRO":红米Note11 Pro / Pro+
"LIGHT":红米Note11E
"VEUX":红米Note11E Pro / 红米Note11 Pro 5G
"FLEUR":红米Note11S / POCO M4 Pro 4G
"JOYEUSE":红米Note9 Pro
"OMEGA":红米Pro
"YSL":红米S2 / 红米Y2
"ONC":红米Y3
"HM2013023":红米手机
"ARMANI":红米手机1S
"HM2014011":红米手机1S 移动3G版
"HM2014501":红米手机1S 移动4G版
"WT88047":红米手机2
"WT86047":红米手机2 增强版
"""