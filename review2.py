# 分析留言的程式碼

data = []
count = 0

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip()) # 顯示目前有幾筆資料，且每加10000筆再印一次就好
		count += 1
		if count % 10000 == 0:
			print(len(data)) # 這樣會比每加一筆就印出來的快很多

	print('檔案讀取完畢了，總共有', len(data), '筆資料!')
