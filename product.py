
products = []
while True:
	name = input("輸入商品名稱(若要停止輸入請按q)：")
	if name == "q":
		break
	price = input("輸入商品價格：") 
	p = [name, price] # 建立二維清單的進階寫法
	products.append(p)   
print(products)


