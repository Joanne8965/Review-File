# 延伸功能 2：總共有多少筆資料

data = []
count = 0                 # 計數

with open('reviews.txt', 'r') as f:
    for line in f:                  # 用 for loop
        data.append(line)           
        count += 1                  # 計數， count = count + 1 
        if count % 1000 == 0:       # % -> 除完後的餘數,在這需要整除
            print(len(data))        # 每1000比印一次
print('檔案讀取完了，總共有', len(data), '筆資料', '/ Total data:', len(data))


# 算出留言平均長度：

sum_len = 0             # 加總每筆留言的長度
for d in data :         # 用 for loop, 可用在字元，一個個字去算！d -> 留言
    sum_len += len(d)   # sum_len = sum_len + len(d)，每筆留言加上當下留言總數，再存回總數

print('留言平均長度為', sum_len/len(data))  # 總長/data長度 

# 補充：可透過 print(sum_len) 印出字元數量 
