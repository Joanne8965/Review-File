
data = []

with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line.strip())   #strip() 取消前後空格

print(len(data))          # 內容長度
print(data [0])           # 取第一筆資料
print('- - - - - - - ')   # 索引標籤，視覺區隔
print(data[1])            # 取第二筆資料


