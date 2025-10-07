s= "abcafasedmnhasjdfhfajdfola"
uniqe=[]
for i in s:
    for j in uniqe:
        if i==j:
            break
    else:
        uniqe.append(i)
print(uniqe)
