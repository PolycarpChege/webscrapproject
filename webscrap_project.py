from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq
my_url = "https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card"  
uclient = ureq(my_url)
page_html=uclient.read()
uclient.close()
page_soup= soup(page_html,"html.parser")
containers = page_soup.findAll("div",{"class": "item-container"})

container = containers[0]
title = container.findAll('div',{'class':'item-info'})

filename = "products.csv"
f = open(filename,"w")

headers ="brand,product_name,shipping \n"

f.write(headers)

for container in containers:
	brand = container.find("div", "item-info").div.a.img["title"]
	full_title=container.findAll('a',{'class':'item-title'})
	product_name= full_title[0].text
	shipping_container = container.findAll('li',{'class':'price-ship'})
	shipping= shipping_container[0].text.strip()

	print("brand:" + brand)
	print("product_name:" + product_name)
	print("shipping:" + shipping)

	f.write(brand + "," + product_name.replace(",", "|")+ "," + shipping +"\n")
f.close()
	





