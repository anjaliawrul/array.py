# define: this method is used to remove first occurrence of given element from the existing array. if it doesn't found the element,shows valueError

from array import*
a=array('i',[101,102,103,104,105])
n=len(a)
i=0
while i<n:
    print(a[i])
    i=i+1
print("Array after remove")
a.remove(105)
n=len(a)
i=0
while(i<n):
    print(a[i])
    i=i+1
