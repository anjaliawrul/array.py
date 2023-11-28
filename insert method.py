from array import*
a=array('i',[101,102,103,104,105])
n=len(a)
i=0
while i<n:
    print(a[i])
    i=i+1
print("Array after insert")
m=a.insert(1,106)
o=a.insert(3,107)
n=len(a)
i=0
while(i<n):
    print(a[i])
    i=i+1
