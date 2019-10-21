# 延伸功能：透過技術了解狀態和印多少次
# print 很花時間，這次改善成每1000比讀一次


data = []
count = 0                 # 計數

with open('reviews.txt', 'r') as f:     # 此 f -> file
    for line in f:
        data.append(line.strip())     # strip() 取消前後空格
        count += 1                    # 計數， count = count + 1 
        if count % 1000 == 0:         # % -> 除完後的餘數,在這需要整除
            print(len(data))          # 每1000比印一次


print(len(data))             # 內容長度
print(data [0])              # 取第一筆資料
print('- - - - - - - ')      # 索引標籤，視覺區隔
print(data[1])               # 取第一筆資料

