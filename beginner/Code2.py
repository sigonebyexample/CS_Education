Secret_num=10
User_num=int(input("Enter a number that you think is the secret number : "))
if User_num==Secret_num:
    print("You are right!")
elif User_num<Secret_num:
    print("Your guess is too low!")
else:
    print("Your guess is too high!")
