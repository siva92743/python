x = 2
y = 2
def add(x, y):
    return x + y

def substract(x, y):
    return x - y

def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter choice(1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):
        x = float(input("enter first num : "))
        y = float(input("enter second num : "))

        if choice == '1':
            print(x, "+", y, "=", x+y)

        if choice == '2':
            print(x, "-", y, "=", x-y)

        if choice == '3':
            print(x, "*", y, "=", x*y)

        if choice == '4':
            print(x, "/", y, "=", x/y)
