import random

def test_random():
    random_number = random.randint(1, 100)
     live=5
    while True:
       
        number = int(input("Enter your number: "))
        if(number == random_number):
            print("Good job! my name is brian, i'm 24 year old ,i'm from korea.")
            break
        elif(number < random_number):
            live-=1
            print(f"you number is less then random number your life now {live}")
        elif (number > random_number):
            live-=1
            print(f"you number is more then random number your life now {live}")
        if(live==0):
            print(f"your live is {live} Game over")
            break
    print(random_number)
test_random()
    