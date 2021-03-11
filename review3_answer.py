# 分析留言的程式碼
# 計算留言的平均長度

data = []
sum_len = 0

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		sum_len = sum_len + len(line) 

print('檔案讀取完畢了，總共有', len(data), '筆資料!')
print('留言平均長度為', sum_len / len(data),'字')

