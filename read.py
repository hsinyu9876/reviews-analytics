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