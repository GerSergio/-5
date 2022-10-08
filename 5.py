print("Введите DELTA(целое число)")
a=[0,2,5,4,7,1,8,9,2,4]
d=int(input())
cou=0
for i in range(len(a)):
    if((a[i]-a[0])==d):
        cou+=1
print("Количество элиментов в заданном массиве,отличающихся на DELTA : ",cou)




