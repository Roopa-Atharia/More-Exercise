a=[1, 5, 10, 12, 16, 20]
b=[1, 2, 10, 13, 16]
i=0
d=a+b
c=[]
while i<len(d):
    if d[i] not in c:
        c.append(d[i])
    i+=1
print(c)

