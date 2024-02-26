# exercise 1
# Write a program to find Perimeter and Area of a Rectangle with integers of Width and height entered by user.
# import pandas as pd
import datetime
import random
import pandas as pd


def perimeter(width, height):
    return 2 * (width + height)


def area(width, height):
    return width * height


# exercise 2
# : Write a program to convert centimeter to decimeter and inch with float centimeter
def convert_cm_to_dm_and_inch(cm):
    dm = cm / 10
    inch = cm / 2.54
    return dm, inch


# exercise 3
# : Write a program to random an integer number and check whether this number having two or three digits.

def is_two_or_three_digits(n):
    return 10 <= n <= 99 or 100 <= n <= 999

# exercise 4
# Write a program to random an integer number in range [-100, 100] check whether this number positive or negative number and have two digits


def is_two_digits(n):
    return 10 <= n <= 99 or -99 <= n <= -10

# exercise 5
#  Write a program to random an integer number in range [10, 150] and normalize it into range [0, 1]


def normalize(n):
    return (n - 10) / (150 - 10)

# exercise 6
# Write a program to find degree and radian angle between hours and minute hands with integers hour and minite


def degree_and_radian(hour, minute):
    degree = abs(30 * hour - 5.5 * minute)
    radian = degree * 3.14 / 180
    return degree, radian

# exercise 7
# rite a program to Solve the quadratic equation x^2 + 5*x + 6 = 0 and print step by step (discriminant, check condition of discriminant, solutions)


def solve_quadratic_equation(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("No solution")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"Solution: x = {x}")
    else:
        x1 = (-b + delta ** 0.5) / (2 * a)
        x2 = (-b - delta ** 0.5) / (2 * a)
        print(f"Solution: x1 = {x1}, x2 = {x2}")

# exercise 8


# exercise 9
#  From the keyboard input the student profile including :Name of Subject 1,2,3 and Mark of Subject 1,2,3. Name of Student and Date of Birth And print the profile of these students with Average Mark


def print_student_profile(name, dob, subjects, marks):
    print(f"Name: {name}")
    print(f"Date of birth: {dob}")
    for i in range(len(subjects)):
        print(f"{subjects[i]}: {marks[i]}")
    print(f"Average mark: {sum(marks) / len(marks)}")


# exercise 10
# : From keyboard input two points with (x,y) and print Euclidean, Manhattan, Cosine distance of points


def euclidean_distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def cosine_distance(x1, y1, x2, y2):
    return (x1 * x2 + y1 * y2) / ((x1 ** 2 + y1 ** 2) ** 0.5 * (x2 ** 2 + y2 ** 2) ** 0.5)


# exercise 11
# Input from keyboards your birthday with day, month year and print information about weekday name, month name, and your age now


def print_birthday_info(day, month, year):
    weekday_name = datetime.date(year, month, day).strftime("%A")
    month_name = datetime.date(year, month, day).strftime("%B")
    age = datetime.date.today().year - year
    print(f"Weekday name: {weekday_name}")
    print(f"Month name: {month_name}")
    print(f"Age: {age}")

# exercise 12
# Input four lists of Customer, Product, Quantity A. Create a DataFrame from three lists above B. Seperate column QuantityList to Quantity and Unit C. Find customer information who bought Pork over 2kg
# CustomerList = ["John", "John", "Marry", "Marry", "Marry"]
# ProductList = ["Beer", "Pork", "Milk", "Vegetable", "Pork"]
# QuantityList = ["2 Bottles", "1 kg", "5 boxes", "2 bunches", "3 kg"]


def menu():
    print("1. Exercise 1")
    print("2. Exercise 2")
    print("3. Exercise 3")
    print("4. Exercise 4")
    print("5. Exercise 5")
    print("6. Exercise 6")
    print("7. Exercise 7")
    print("8. Exercise 8")
    print("9. Exercise 9")
    print("10. Exercise 10")
    print("11. Exercise 11")
    print("12. Exercise 12")
    print("0. Exit")
    choice = int(input("Enter choice: "))
    return choice


while True:
    choice = menu()
    if choice == 0:
        break
    elif choice == 1:
        width = float(input("Enter width: "))
        height = float(input("Enter height: "))
        print(f"Perimeter = {perimeter(width, height)}")
        print(f"Area = {area(width, height)}")
    elif choice == 2:
        cm = float(input("Enter cm: "))
        dm, inch = convert_cm_to_dm_and_inch(cm)
        print(f"dm = {dm}")
        print(f"inch = {inch}")
    elif choice == 3:
        n = random.randint(1, 1000)
        print(f"n = {n}")
        print(f"n is two or three digits: {is_two_or_three_digits(n)}")
    elif choice == 4:
        n = random.randint(-100, 100)
        print(f"n = {n}")
        print(f"n is two digits: {is_two_digits(n)}")
    elif choice == 5:
        n = random.randint(10, 150)
        print(f"n = {n}")
        print(f"n normalized = {normalize(n)}")
    elif choice == 6:
        hour = int(input("Enter hour: "))
        minute = int(input("Enter minute: "))
        degree, radian = degree_and_radian(hour, minute)
        print(f"degree = {degree}")
        print(f"radian = {radian}")
    elif choice == 7:
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        c = int(input("Enter c: "))
        solve_quadratic_equation(a, b, c)
    elif choice == 8:
        s = "Today is Sunday and we don't need to wake up at 6 am"
        words = s.split()
        print(f"Number of words: {len(words)}")
        for i in range(len(words)):
            if words[i].isdigit():
                print(f"Position of number: {i}")
                break
    elif choice == 9:
        name = input("Enter name: ")
        dob = input("Enter date of birth: ")
        subjects = []
        marks = []
        for i in range(3):
            subjects.append(input(f"Enter subject {i + 1}: "))
            marks.append(float(input(f"Enter mark {i + 1}: ")))
        print_student_profile(name, dob, subjects, marks)
    elif choice == 10:
        x1 = int(input("Enter x1: "))
        y1 = int(input("Enter y1: "))
        x2 = int(input("Enter x2: "))
        y2 = int(input("Enter y2: "))
        print(f"Euclidean distance: {euclidean_distance(x1, y1, x2, y2)}")
    elif choice == 11:
        day = int(input("Enter day: "))
        month = int(input("Enter month: "))
        year = int(input("Enter year: "))
        print_birthday_info(day, month, year)
    elif choice == 12:
        CustomerList = ["John", "John", "Marry", "Marry", "Marry"]
        ProductList = ["Beer", "Pork", "Milk", "Vegetable", "Pork"]
        QuantityList = ["2 Bottles", "1 kg", "5 boxes", "2 bunches", "3 kg"]

        df = pd.DataFrame(
            {"Customer": CustomerList, "Product": ProductList, "Quantity": QuantityList})
        print(df)

        df["Quantity"] = df["Quantity"].apply(lambda x: x.split())
        df["Quantity"] = df["Quantity"].apply(lambda x: [float(x[0]), x[1]])
        print(df)

        df = df[df["Product"] == "Pork"]
        df = df[df["Quantity"].apply(lambda x: x[1] == "kg")]
        df = df[df["Quantity"].apply(lambda x: x[0] > 2)]
        print(df)
    else:
        print("Invalid choice")
        continue
    input("Press Enter to continue...")
    print()
