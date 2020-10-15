import os #operating system
#讀取檔案
products = []
if os.path.isfile("product.csv"): #檢查檔案在不在
	print("找到檔案了！")
	while True:
		name = input("輸入商品名稱(若要停止輸入請按q)：")
		if name == "q":
			break
		price = input("輸入商品價格：") 
		p = [name, price] # 建立二維清單的進階寫法
		products.append(p)   
	print(products)

else:
	print("找不到檔案!!!!")

#讓使用者輸入
while True:
		name = input("輸入商品名稱(若要停止輸入請按q)：")
		if name == "q":
			break
		price = input("輸入商品價格：") 
		p = [name, price] # 建立二維清單的進階寫法
		products.append(p)   
print(products)


# for p in products:
# 	print(p[0], "的價格為", p[1])

# with open("product.txt", 'w') as f:
# 	for p in products:
# 		f.write(p[0] + "," + p[1] + "\n")


with open("product.csv", 'w', encoding = "utf-8") as f:  #寫入中文時編碼，但若用excel開啟時還需從data在選編碼
	f.write("商品名稱" + "," + "商品價格" + "\n")
	for p in products:
		f.write(p[0] + "," + p[1] + "\n")

