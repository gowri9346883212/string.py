#ATM withdraw
print("please insert your card")
accountnumber=1234123412341234
print(int(input("please enter your accountnumber:")))
password=1234
pin=int(input("please enter your pin number:"))
balance=50000
if pin==password:
    print("""1==balance enquiry   2==withdrawl
             3==deposit           4==exit""")
    try:
        option=int(input("enter your choice:"))
    except:
        print("please enter valid option")
    if option==1:
        print("your accont balance{50000}")
    if option==2:
        withdrawlamount=int(input("enter the withdrawl amount:"))
        balance=balance-withdrawlamount
        print(f'{withdrawlamount} is debited to your account')
        print(f'{balance} is your current balance ')
    if option==3:
        depositamount=int(input("enter the deposited amount:"))
        balance=balance+depositamount
        print(f'{depositamount} is credited to your account')
        print(f'{balance} is your current balance')
        if option==4:
            print("exit")
        else:
            print("wrong pin")