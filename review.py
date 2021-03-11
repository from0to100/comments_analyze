# 分析留言的程式碼

data = []

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())

print(len(data)) # 印出資料有幾筆
print(data[1]) #印出所有的資料，Ctrl+C keyboard interrupt