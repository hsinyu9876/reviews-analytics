data = []
count = 0
with open('reviews.txt','r') as f:
    for line in f:
        data.append(line)
        count +=1
        if count % 1000 == 0: # %是用來求餘數的
            print(len(data))
print(len(data))
print(data[0])
print('--------------') #方便區分留言
print(data[1])