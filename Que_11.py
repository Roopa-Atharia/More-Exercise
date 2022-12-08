a="NavGurukul is an alternative to higher education reducing the barriers of current formal education system"
b=[]
c=''
for d in a:
    if d== ' ':
        b.append(c)
        c=''
    else:
        c+=d
if c:
    b.append(c)
print(b)
