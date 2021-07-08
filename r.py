data = []
with open('reviews.txt', 'r') as f: #r代表讀取模式
 for line in f:
 	data.append(line)
print(len(data))

print(data[0])
print('----------------------')
print(data[1])
