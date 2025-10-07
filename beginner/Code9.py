import random
z= random.randint(1,100)
lp_in=0
lp_out=10
flag=True
while(flag == True):
    for i in range(lp_in,lp_out+1):
        if (i==z):
            print("You win! It was in range: ",lp_in,"to",lp_out,"and it was",z)
            flag=False
            break
        else:
            pass
    if flag==True:
        print("Wasn't in range",lp_in,"to",lp_out)    
        lp_in+=10
        lp_out+=10   
