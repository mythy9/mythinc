ac=170851
pin=7410
cr_ac=2500000
sv_ac=300000
card=int(input("insert the card"))
p=int(input("enter pin:"))
if  card==ac and p==pin:
    print("1.savings acc, 2. current acc")
    choose_ac=int(input("choose the acc:"))
    if choose_ac==1:
        print("savings account!")
        print("1. balance 2. withdraw 3. deposit")
        choose_op=int(input("choose the option:"))
        if choose_op==1:
            print("total balance:",sv_ac)
        elif choose_op==2:
            wd=int(input("enter amt to withdraw"))
            if wd>=500 and wd<=45000:
                print("collect cash:", wd)
                print("available balance:",sv_ac-wd)
            else:
                print("limited withdraw reached")
        elif choose_op==3:
            dp=int(input("enter the depodit amt:"))
            if dp>100 and dp<=45000:
                print("amount deposited:",dp)
                print("available balance:",sv_ac+dp)
            else:
                print("limited deposit has reached")
        else:
            print("wrong choice")
    elif choose_ac==2:
        print("current account!")
        print("1. balance 2. withdraw 3. deposit")
        choose_op=int(input("enter option"))
        if choose_op==1:
            print("total balance:",cr_ac)
        elif choose_op==2:
            wd=int(input("enter amount to draw"))
            if wd>=500 and wd<=45000:
                print("collect cash:",wd)
                print("available balance:",cr_ac-wd)
            else:
                print("limited withdraw reached")
        elif choose_op==3:
            dp=int(input("enter amt to deposit"))
            if dp>=200 and dp<20000:
                print("amt deposited:", dp)
                print("available balance:", cr_ac+dp)
            else:
                print("limited deposit reached")
        else:
            print("wrong choice")
    else:
        print("wrong option")
else:
    print("wrong pin or card not detected")
