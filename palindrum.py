#palindrum
n = str(input("text here : "))
j=-1
k=0
for i in n:
    if i != n[j]:
        k = 1
        break
    j = j - 1
if k == 1:
    print("no")
else:
    print("yes")
