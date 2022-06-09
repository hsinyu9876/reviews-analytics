import time
import progressbar

data = []
count = 0
bar = progressbar.ProgressBar(max_value=1000000)
with open('reviews.txt','r') as f:
    for line in f:
        data.append(line)
        count +=1
        bar.update(count)
        #if count % 1000000 == 0: # %是用來求餘數的
            #print(len(data))
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

good = [comment for comment in data if 'good' in comment]
#bad = ['bad' in comment for comment in data] 提到bad裝True、沒提到裝False到bad list
# good = []
# for comment in data:
#     if 'good' in comment:
#         good.append(comment)
print('一共有', len(good), '筆留言提到good') 
print(good[0])

#文字計數
start_time = time.time()
wc = {} #word_count
for d in data:
    words = d.split() #拿到每一筆留言用空格分出每一個英文單字
    for w in words:#巢狀迴圈 一層包一層包下去while / for 裡面還有 while / for 的情況
        if w in wc:
            wc[w] += 1
        else:
            wc[w] = 1
for w in wc:
    if wc[w] > 200000:
        print(w, wc[w])
end_time = time.time()
print('一共花', end_time - start_time, '秒')

print('字典一共有',len(wc),'個字')#字典有幾個單字

while True:
    w = input('你想查甚麼字:')
    if w == 'q':
        break
    if w in wc:
        print(w, '出現過的次數:', wc[w])
    else:
        print('這個單字沒出現過唷')

print('感謝使用本查詢功能')