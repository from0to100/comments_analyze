# 分析留言的程式碼
# 計算留言的平均長度

data = []


with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(len(line.strip())) # 將每篇留言長度存到data清單 # len的資料是int 
		
x = 0
for num in data:
	x = num + x  # 將加總值存到x變數

print('檔案讀取完畢了，總共有', len(data), '筆資料!')
print('留言平均長度為', x / len(data),'字')

