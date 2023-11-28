from array import*
a=array('i',[101,102,103,104,105])
arr=array('i',[107,108,109])
n=len(a)
i=0
while(i<n):
    print(a[i])
    i=i+1

print("Array After Extend")
a.extend(arr)
n=len(a)
i=0
while(i<n):
    print(a[i])
    i=i+1
