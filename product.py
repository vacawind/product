import os # operating system

# 確認檔案是否存在
def read_file(filename):
	products = []
	with open(filename, 'r', encoding = "utf-8") as f:
		for line in f:
			if "商品名稱,商品價格" in line:
				continue
			name, price = line.strip().split(",")
			# s = line.strip().split(",")
			# name = s[0]
			# price = s[1]
			products.append([name,price])
		print(products)
	return products


# 使用者輸入
def user_input(products):
	while True:
		name = input("輸入商品名稱(若要停止輸入請按q)：")
		if name == "q":
			break
		price = input("輸入商品價格：") 
		p = [name, price] # 建立二維清單的進階寫法
		products.append(p)   
	print(products)
	return products


# 印出所有購買紀錄
def print_products(products):
	for p in products:
		print(p[0], "的價格是", p[1])


# 寫入檔案
def write_file(filename, products):
	with open("product.csv", 'w', encoding = "utf-8") as f:  #寫入中文時編碼，但若用excel開啟時還需從data在選編碼
		f.write("商品名稱" + "," + "商品價格" + "\n")
		for p in products:
			f.write(p[0] + "," + p[1] + "\n")


# 主程式
def main(filename):
	if os.path.isfile(filename):
		print("找到檔案了!!!")
		products = read_file(filename)
	else:
		print("找不到檔案~~")

	products = user_input(products)

	print_products(products)

	write_file(filename, products)
	


filename = "product.csv"
# 主程式進入點
main(filename)
