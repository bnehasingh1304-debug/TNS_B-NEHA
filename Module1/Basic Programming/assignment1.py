# ============================================================
# ASSIGNMENT 1
# Python Conditions, Built-in Functions, Modules and Packages
# ============================================================


# ------------------------------------------------------------
# PROGRAM 1: Using Conditions
# Scenario: Movie Ticket Price Calculator
# ------------------------------------------------------------

print("PROGRAM 1: MOVIE TICKET PRICE CALCULATOR")

age = int(input("Enter your age: "))

if age < 12:
    print("Ticket Price: ₹100")
elif age < 60:
    print("Ticket Price: ₹200")
else:
    print("Ticket Price: ₹120")


# ------------------------------------------------------------
# PROGRAM 2: Using a Built-in Function
# Scenario: Online Shopping Cart
# ------------------------------------------------------------

print("\nPROGRAM 2: ONLINE SHOPPING CART")

cart = ["T-Shirt", "Jeans", "Shoes", "Watch"]

number_of_items = len(cart)

print("Products in your cart:", cart)
print("Total number of items:", number_of_items)


# ------------------------------------------------------------
# PROGRAM 3: User-defined Functions, Module and Package
# Scenario: Student Result
# ------------------------------------------------------------

print("\nPROGRAM 3: STUDENT RESULT")

def calculate_total(marks1, marks2, marks3):
    return marks1 + marks2 + marks3


def calculate_average(total):
    return total / 3


def check_result(average):
    if average >= 40:
        return "Pass"
    else:
        return "Fail"


marks1 = 75
marks2 = 80
marks3 = 65

total = calculate_total(marks1, marks2, marks3)
average = calculate_average(total)
result = check_result(average)

print("Total Marks:", total)
print("Average Marks:", average)
print("Result:", result)
