# 延伸功能 3：清單篩選

data = []
count = 0                

with open('reviews.txt', 'r') as f:
    for line in f:                  
        data.append(line)           
        count += 1                  
        if count % 1000 == 0:       
            print(len(data))       
print('檔案讀取完了，總共有', len(data), '筆資料', '/ Total data:', len(data))

sum_len = 0             
for d in data :         
    sum_len += len(d)   
print('留言平均長度為', sum_len/len(data)) 


# 如何篩選資料：找出小於100的字串

new = []                     # 建立新清單
for d in data:               # d 為一個留言(字串)
    if len(d) < 100:         # 如果字串長度 < 100
        new.append(d)        # 就裝入新的(new)清單
print('一共有', len(new), '筆留言長度小於100', 'Total', len(new), 'of comments are less than 100')
print(new[0])                # 挑出篩選後的第一筆資料
print(new[1])



# 篩選出有Good的字串：

good = []
for d in data:              # d 為一個留言(字串)
    if 'good' in d:         # 如果 d 裡有出現 good 的字串  #是非題
        good.append(d)      # 裝入 'good' 的清單
print('一共有', len(good), '比留言提到good', '/Total', len(good), 'of comments mentioned about good')

print(good[0])













