#program to find the sum of digit as 3 in car number plate
a=[]#to enter the value in list
for x in list((range(0,10000))):
    s=0# to find sum
    t=0# to find sum
    num ='{0:04}'.format(x)#to make the digits as four digits
    while(x > 0):
        z = int(x % 10)
        s = int(s + z)
        x = int(x// 10)
    while (s > 0):
            z = s % 10
            t = int(t + z)
            s = s // 10
    last = "sum is {} ".format(s)
# checking if the sum is equal to 3
    if(t == 3):
            a.append(num)
print(a)
print("total")
print (len(a))

