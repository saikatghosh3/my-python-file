def add(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiply(x, y):
    return x * y

def divide(x, y):
        return x / y


print("select operation :")
print("1.add")
print("2.subtraction")
print("3.multiply")
print("4.divide")

while True:
    choice = input("Enter your choice(1/2/3/4... :")
    if choice in ('1', '2', '3', '4'):

        num1 = float(input("Enter the first number :"))
        num2 = float(input("Enter the seacond number"))
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtraction(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        next_calculation = input("Next calculation? yes/ no : ")
        if next_calculation == "no":
            break

    else:
        print("Invalid Input")
