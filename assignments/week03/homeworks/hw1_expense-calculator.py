"""
Personal Finance Calculator
Student: [Suphasin]
Date: [22/7/2568]
Purpose: Calculate monthly budget and savings
"""

monthly_income=float(input("Monthly income(THB): "))
rent_cost=float(input("Monthly rent/housing cost(THB): "))
food_budget=int(input("Monthly food budget in(THB): "))
transportation_cost=float(input("Monthly trarsportation expenses(THB): "))
entertainment_budget=int(input("Monthly entertainment(THB): "))
emergency_fund_percent=float(input("Percentage to save for emergency(e.g, 10.5): "))
investment_percent=float(input("precentage to investle(e.g., 15.0): "))
Total_fixed_expenses=rent_cost+transportation_cost
Total_variable_expenses=food_budget+entertainment_budget
Total_Expenses=Total_fixed_expenses+Total_variable_expenses
Remaining_income=monthly_income-Total_Expenses
Emergency_fund_amount=monthly_income*(emergency_fund_percent/100)
Investment_amount=monthly_income*(investment_percent/100)
Available_for_savings=Remaining_income-Emergency_fund_amount-Investment_amount
Expense_ratio=(Total_Expenses/monthly_income)*100
print()
print("===MONTHLY BUDGET REPORT===")
print("income: ",monthly_income,'THB')
print("Fixed Expenses: ",Total_fixed_expenses,'THB')
print("Variable Expenses: ",Total_variable_expenses,'THB')
print("Total Expenses: ",Total_Expenses,'THB')
print("Remaining: ",Remaining_income,'THB')
print()
print("===SAVINGS BREAKDOWN===")
print("Emergency Fund(" +str(emergency_fund_percent)+"%:)",Emergency_fund_amount,'THB')
print("Investment(" +str(investment_percent) + "%):",Investment_amount,'THB')
print("Available for Savings: ",Available_for_savings,'THB')
print()
print("===ANALYSIS===")
print("Expense Ration: ",Expense_ratio,'%')