def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()
greet("Sohel")

def student(name, age, department):
    print(name, age, department)

student(age=22, department="CSE", name="Sohel")

def add_numbers(*args):
    print(args)
    print(sum(args))

add_numbers(10, 20)
add_numbers(10, 20, 30, 40)


def display_info(**kwargs):
    print(kwargs)

display_info(name="Sohel", age=22, city="Dhaka")


def example(a, b=10, *args, **kwargs):
    print("a:", a)
    print("b:", b)
    print("args:", args)
    print("kwargs:", kwargs)

example(5, 20, 30, 40, name="Sohel", city="Dhaka")