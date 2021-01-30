# 通过def关键字定义函数
# def func_name(arg0...):
def say_hello():
    print("Hello world")


say_hello()
say_hello()


# 函数参数，逗号分割（形式参数）
def print_max(a, b):
    if a > b:
        print(a)
    elif a == b:
        print("equal")
    else:
        print(b)


print_max(10, 20)
print_max(10, 10)
print_max(20, 10)
x = 5
y = 7
print_max(x, y)


# 局部变量和全局变量
def func():
    global x
    x = 25


func()
print(x)


# 默认参数
def func_1(a, b=5, c=10):
    print(a + b + c)


func_1(3)
func_1(2, 6, 7)
func_1(2, c=5)


# 可变参数
def func_2(a, *numbers, **testNumbers):
    print(a)
    for number in numbers:
        print(number)
    for first_part, second_part in testNumbers.items():
        print(first_part, second_part)
print(func_2(10,1,2,3,Jack=1123,John=2231,Inge=1560))

help(print)