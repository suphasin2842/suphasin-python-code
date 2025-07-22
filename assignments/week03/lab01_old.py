
# Complete this program to classify people by age
age = int(input("Enter age: "))

# Add your if-elif-else statements here
# 0-12: Child
# 13-19: Teenager  
# 20-59: Adult
# 60+: Senior
# Your code here:

age = int(input("Enter your age: "))
if age >=60:
    print("your are senior")
elif 19< age <=59:
    print("your are adult")
elif 12< age <=19:
    print("your are teenager")
else:
    print("Your are child")
