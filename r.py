data = []
count = 0
with open('reviews.txt', 'r') as f: #r代表讀取模式
 for line in f:
 	data.append(line)
 	count += 1
 	if count % 1000 == 0:
 		print(len(data))
print('file read, there are', len(data),'comments in total')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('the average length of the comment is', sum_len/len(data))