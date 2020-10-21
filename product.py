import os # operating system

# 確認檔案是否存在
products = []
if os.path.isfile("product.csv"):
	print("找到檔案了!!!")
	with open("product.csv", 'r', encoding = "utf-8") as f:
		for line in f:
			if "商品名稱,商品價格" in line:
				continue
			name, price = line.strip().split(",")
			# s = line.strip().split(",")
			# name = s[0]
			# price = s[1]
			products.append([name,price])
		print(products)
else:
	print("找不到檔案~~")


# 使用者輸入
while True:
	name = input("輸入商品名稱(若要停止輸入請按q)：")
	if name == "q":
		break
	price = input("輸入商品價格：") 
	p = [name, price] # 建立二維清單的進階寫法
	products.append(p)   
print(products)


# 印出所有購買紀錄
for p in products:
	print(p[0], "的價格是", p[1])

# 寫入檔案
with open("product.csv", 'w', encoding = "utf-8") as f:  #寫入中文時編碼，但若用excel開啟時還需從data在選編碼
	f.write("商品名稱" + "," + "商品價格" + "\n")
	for p in products:
		f.write(p[0] + "," + p[1] + "\n")
