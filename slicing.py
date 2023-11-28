from array import*
a=array('i',[101,102,103,104,105,106,107])
print("original Array")
n=len(a)
for i in range(n):
    print(i,"=",a[i])

print("************")
m=a[0:4]
for i in m:
    print(i)
