'''
# Complete this ATM simulation
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = input("Choose option: ")
        
        # Complete the menu logic here
        # Your code here:
        
else:
    print("Invalid PIN")
'''

balandce=1000
pin="1234"
entered_pin = input("enter PIN: ")
if entered_pin == pin:
    print("PIN accepted!")
while 'Ture':
    print("\n1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit") 
    print("4. Exit")
    choice = input("Choose option: ")

    if choice == "1":
        print("balandce= ",balandce)

    elif choice == "2":
        whithdraw=int(input("what withdraw you want: "))
        if whithdraw > balandce :
            print("not have money")
        elif whithdraw == 0:
            print("you enter 0 for what?")
        else:
            balandce=balandce - whithdraw
    elif choice == "3":
        deposit=int(input("what deposit you want: "))
        if deposit <=0:
            print("don't do it man")
        else:
            balandce=deposit + balandce
    elif choice == "4":
        print("love you,thank you for use us ATM,Have a nice day ")
        break
    else:
        print("error")
            