data = []
count = 0
with open('reviews.txt','r') as f:
    for line in f:
        data.append(line)
        count +=1
        if count % 100000 == 0: # %是用來求餘數的
            print(len(data))
print('檔案讀取完了，總共有', len(data), '筆資料')

sum_len = 0
for comment in data:
    sum_len += len(comment) # =sum_len+len(comment) 算出總長度
print('留言的平均長度為', sum_len/len(data)) 

new = []
for comment in data:
    if len(comment) < 100:
        new.append(comment)
print('一共有', len(new), '筆留言長度小於100')
print(new[0])

# good = []
# for comment in data:
#     if 'good' in comment:
#         good.append(comment)
good = [comment for comment in data if 'good' in comment]
print('一共有', len(good), '筆留言提到good') 
print(good[0])


#bad = ['bad' in comment for comment in data] 提到bad裝True、沒提到裝False到bad list