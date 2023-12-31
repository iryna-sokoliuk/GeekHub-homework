'''
Ну і традиційно - калькулятор :slightly_smiling_face: 
Повинна бути 1 ф-цiя, яка б приймала 3 аргументи - один з яких операцiя, яку зробити! 
Аргументи брати від юзера (можна по одному - 2, окремо +, окремо 2; можна всі разом - типу 1 + 2). 
Операції що мають бути присутні: +, -, *, /, %, //, **. 
Не забудьте протестувати з різними значеннями на предмет помилок!
'''


def get_number():
    while True:
        num = input("Напишіть число: ")
        try:
            num = float(num) or int(num)
            return num
        except ValueError:
            print("Невірне число, введіть ще раз!")


def get_operation():
    while True:
        operation = input("Напишіть математичну операцію (+, -, *, /, %, //, **): ")
        operations = ["+", "-", "*", "/", "%", "//", "**"]
        if operation in operations:
            return operation
        else:
            print("Некоретно написана дія. Спробуйте ще раз!")


a = get_number()
b = get_number()
c = get_operation()


def calculate(x, y, operation):
    if operation == "-":
        print(f"Відповідь: {x - y} ")
    elif operation == "+":
        print(f"Відповідь: {x + y} ")
    elif operation == "*":
        print(f"Відповідь: {x * y} ")
    elif operation in "/":
        if y == 0:
            print("На нуль ділити не можна!")
        else:
            print(f"Відповідь: {x / y} ")
    elif operation == "//":
        if y == 0:
            print("На нуль ділити не можна!")
        else:
            print(f"Відповідь: {x // y} ")
    elif operation == "%":
        print(f"Відповідь: {x % y} ")
    elif operation == "**":
        print(f"Відповідь: {x ** y} ")


calculate(a, b, c)
