where= input("Go left or right? ")
x=0
while where == "right" and x<2:
    where= input("Go left or right? ")
    x+=1
    if x==2:
        print("(-_-)")
print("You got out!")
