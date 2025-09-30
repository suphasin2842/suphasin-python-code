"""
Create a Personal Information Validator program that:
    Asks user for their name, age, and phone number
    Validates that name contains only alphabetic characters and spaces
    Converts age from string to integer and validates it's between 18-65
    Validates phone number contains exactly 10 digits
    
    Uses appropriate string methods for validation
    Displays formatted output with proper string formatting
    
    USE: isalpha(), isdigit(), upper(), string formatting with % or .format()
    
Example Result

=== PERSONAL INFORMATION VALIDATOR ===
Enter your name: John Doe
Enter your age: 25
Enter your phone number: 9876543210

Validation Results:
Name: Valid (contains only letters and spaces)
Age: Valid (25 years old)
Phone: Valid (10-digit number)

Formatted Information:
Name: JOHN DOE
Age Group: Young Adult (18-30)
Phone: +91-9876543210

"""

print("=== PERSONAL INFORMATION VALIDATOR ===")
name = input("Enter your name: ")
age = input ("Enter your age: ")
phone = input("Enter your phone number: ")
int(age)
#name validation ช่วงตรวจเงื่อนไขชื่อ
nameflag = True
for char in name:
    print(char, char.isalpha())
    if char.isalpha() or char == " ":
        nameflag=True
    else:
        nameflag=False
    
    
#print(nameflag)

ageflag = True
if int(age) < 18 or int(age) > 65 :
    ageFlag = False

phoneflag = True
if len(phone) != 10:
    phoneflag = False
else:
    for char in phone:
        if char.isdigit() == False:
            phoneflag = False
            break

print("Validation Results:")
if nameflag:
    print("Name: Valid (contains only letters and spaces)")
else:
    print("Name: Invalid (not contains only letters and spaces)")

if ageflag:
    print(f"Age: Valid ({age} years old)")
else:
    print(f"Age: Invalid (less then 18 or more then 65 year old)")

if phoneflag:
    print("Phone: Valid (10-digit number)")
else:
    print("Phone: Invalid (Not 10-digit number)")


print("Formatted Information:")
print("Name: ", name.upper())
if int(age) >= 18 and int(age) <=30:
    print("Age Group: Young Adult (18-30)")
else:
    print("Age Group: not Young Adult")

print(f"Phone:+{phone}")