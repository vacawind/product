
products = []
while True:
	name = input("輸入商品名稱(若要停止輸入請按q)：")
	if name == "q":
		break
	products.append(name)
print(products)


