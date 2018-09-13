def swap(aaa,b,c):
    temp=a[b]
    a[b]=a[c]
    a[c]=temp
a=[100,4,6,5,10,9,6]
#tttttttttttttttttttttttt
for x in range(0,len(a)-1):
    last=len(a)-1-x
    for i in range((last-1)/2,-1,-1):
        k=i
        while(2*k+1<=last):
            da=2*k+1
            if(da<last):
                if(a[da]<a[da+1]):
                    da+=1
            if(a[k]<a[da]):
                swap(a,k,da)
                k=da
            else:
                break
    swap(a,0,len(a)-1-x)
print (a)