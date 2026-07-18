a = [1,2,3,4,5,6,7,7,6,5,434,534,2,2,1,3,45,7,8]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)