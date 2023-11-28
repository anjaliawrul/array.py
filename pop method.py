from array import*
a=array('i',[101,102,103,104,105])
n=len(a)
i=0
r=a.pop(1)
while i<n:
    print(a[1])
    i=i+1
print("removed",r)