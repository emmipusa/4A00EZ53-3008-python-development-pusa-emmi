#a
def my_name():
    print("Emmi")

my_name()

#b
def my_name(name):
    print(name)

my_name("Emmi")

#c
def output(text, amount):
    print(text * amount)

output("hello", 2)

#d
def largest(a, b, c):
    if a > b:
        print(a)
    elif b > c:
        print(b)
    else:
        print(c)

largest(3, 5, 9)