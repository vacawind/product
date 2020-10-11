
products = []
while True:
	name = input("輸入商品名稱(若要停止輸入請按q)：")
	if name == "q":
		break
	price = input("輸入商品價格：")
	p = []         #建立二維清單
	p.append(name)
	p.append(price)
	products.append(p)
print(products)


