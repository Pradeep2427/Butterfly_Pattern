def getting_num():
    num = int(input("Enter a odd number  "))
    if num % 2 == 0:
        return getting_num()
    return num 

num = getting_num()

row = []
lis = []
for i in range (num*2):
    lis.append(' ')

val = 1 
for m in range (num): 
    lis[m] = val
    lis[num*2-1 - m] = val
    val = val + 1
    listToStr = ' '.join([str(elem) for elem in lis])
    print(listToStr)
    row.append(listToStr) 

row.reverse()
for n in range(1,num):
    print(row[n])
        

    
