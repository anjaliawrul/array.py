from array import*
a=array('i',[101,102,103,104,105])
n=len(a)
i=0
while i<n:
    print(a[i])
    i=i+1
print("Array after append")
m=a.append(106)
o=a.append(107)
n=len(a)
i=0
while(i<n):
    print(a[i])
    i=i+1
