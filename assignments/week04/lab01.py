"""
Personal Information Manager 

#Create a tuple to store a person's basic info: (name, age, city, country)
#Create a list to store their hobbies

Allow the user to:

Display all information
Add new hobbies
Remove hobbies
Update age (by creating a new tuple)

"""
"""
# Complete this program
def personal_info_manager():
    # Create initial person tuple
    person = ("", 0, "", "")  # name, age, city, country
    hobbies = []
    
    # Your code here
    pass

if __name__ == "__main__":
    personal_info_manager()
"""

def personal_info_manager():
    person = ("suphasin nongyai",19,"pattaya","chonburi")
    hobbies=[]

    while True:
        choice=input("1. all info \n2.Add the Hobby \n3.Remove the Hobby \n4.update age\n Enter your choice: ")

        if choice == "1":
            print("Name: ",person[0])
            print("Age: ",person[1])
            print("City: ",person[2])
            print("country: ",person[3])
            print("Hobby: ",hobbies)
        elif choice == "2":
            hobby=input("What is your new hobby: ")
            hobbies.append(hobby)

        elif choice == "3":
            hobbies.pop()

        elif choice == "4":
            person_list = list(person)
            age= input("How old are you: ")
            person_list[1]=age
            person= tuple(person_list)

        elif choice == "5":
            break
        
if __name__ == "__main__":
    personal_info_manager()