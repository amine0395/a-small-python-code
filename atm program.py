# z=444
# '''my requirement is to create a atm options using functions
# withdraw
# deposit
# balance
# ministatement
# '''
# z=int(input("please enter your pin:"))
# a=int(input("press 1 to continue:"))
#
# b='''
#   1.withdraw
#   2.deposit
#   3.balance
#   4.ministatement'''
# if a==1:
#     print(b)
#     c = int(input('choose the option:'))
#     if c==1:
#         def withdraw():
#             n = int(input("enter the amount:"))
#             print('you have withdrawn rupees', n)
#
#
#         withdraw()
#     elif c==2:
#         def deposit():
#             n = int(input("enter the amount:"))
#             print("you have deposited", n)
#
#
#         deposit()
#     elif c==3:
#         def balance():
#             n = 10000
#             print("the available bal is:", n)
#
#
#         balance()
#
#     elif c==4:
#         def ministate():
#             n = '''
#               1-1-21  200
#               5-1-21  1000
#               22-1-21 300
#               the available bal is 8500'''
#             print(n)
#
#
#         ministate()
#     while c>4:
#         print("you have entered wrong option plz start from begining")
#         break
#     while c<=0:
#         print("you have entered wrong option plz start from begining")
#         break
#
#
# while a>1:
#     print('you have entered wrong option')
#     break
# #
#
print("plz insert your cardd")
p=int(input("please enter your pin:"))
pin=len(str(p))
if pin==4:

    a=int(input("press 1 to continue:"))

    b='''
       1.withdraw
       2.deposit
       3.balance
       4.ministatement'''
    if a == 1:
        print(b)
        c = int(input('choose the option:'))
        if c == 1:
            def withdraw():
                n = int(input("enter the amount:"))
                print('you have withdrawn rupees', n)


            withdraw()
        elif c == 2:
            def deposit():
                n = int(input("enter the amount:"))
                print("you have deposited", n)


            deposit()
        elif c == 3:
            def balance():
                n = 10000
                print("the available bal is:", n)


            balance()

        elif c == 4:
            def ministate():
                n = '''
                  1-1-21  200
                  5-1-21  1000
                  22-1-21 300
                  the available bal is 8500'''
                print(n)


            ministate()
        while c > 4:
            print("you have entered wrong option plz start from begining")
            break
        while c <= 0:
            print("you have entered wrong option plz start from begining")
            break

    while a > 1:
        print('you have entered wrong option')
        break



else:
    print("plz enter four digit pin")