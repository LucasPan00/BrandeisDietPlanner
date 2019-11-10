import requests
from lxml import etree

html = requests.get("https://menus.sodexomyway.com/BiteMenu/Menu?menuId=1119&locationId=62313001&whereami=http://brandeis.sodexomyway.com/dining-near-me/sherman-dining").text
# print (html)
etree_html = etree.HTML(html)
f = open("Sherman.txt","w+")

f.writelines('\t\t//////Breakfast//////')
f.writelines('\n\t\t')
content = etree_html.xpath('/html/body/div/div/div[2]/div[2]/div[2]/div[1]/div[9]/div/div[1]/div[2]/ul/li')
for div in content:
    food = div.xpath('./div[1]/a/text()')
    f.writelines(food)
    f.writelines(' : ')
    cal = div.xpath('./div[2]/a/text()')
    f.writelines(cal[0])

f.writelines('//////Lunch//////')
f.writelines('\n\t\t')
content = etree_html.xpath('/html/body/div/div/div[2]/div[2]/div[2]/div[1]/div[9]/div/div[2]/div[2]/ul/li')
for div in content:
    food = div.xpath('./div[1]/a/text()')
    f.writelines(food)
    f.writelines(' : ')
    cal = div.xpath('./div[2]/a/text()')
    f.writelines(cal[0])

f.writelines('//////Dinner//////')
f.writelines('\n\t\t')
content = etree_html.xpath('/html/body/div/div/div[2]/div[2]/div[2]/div[1]/div[9]/div/div[3]/div[2]/ul/li')
for div in content:
    food = div.xpath('./div[1]/a/text()')
    f.writelines(food)
    f.writelines(' : ')
    cal = div.xpath('./div[2]/a/text()')
    f.writelines(cal[0])

