"""
Question 2: Currency Converter (20 points)

Write a program that converts between Thai Baht (THB) and US Dollars (USD).
Requirements:

Ask user to choose conversion direction (THB to USD or USD to THB)
Ask for the amount to convert
Use exchange rate: 1 USD = 35.5 THB
Display result with 2 decimal places
Show the calculation formula used
"""

choose=input("choose conversion direction (1 for THB to USD/ 2 for USD to THB): ")
money=float(input("money for exchange: " ))
if choose == '1':
    result =money / 35.5
    print("your money: ",result,'USD')
elif choose == '2':
    result = money * 35.5
    print("your money: ",result,'THB')
else:
    print("You don't choose number")