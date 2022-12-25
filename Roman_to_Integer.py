d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
ds=['I','V','X','L','C','D','M']
s=input()
s="".join(reversed(s))
sum=0
k = 'I'
for i in s:
    p=ds.index(i)
    p2=ds.index(k)
    if p>=p2:
        sum=d[i]+ sum
    else: sum=sum-d[i]
    k=i
print(sum)