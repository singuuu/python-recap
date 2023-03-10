def named1(name, age):
    print(name, age)


details = {"name": "Bob", "age": 25}

named1(**details)


##################################################################

def named(**kwargs):
    print(kwargs)


details = {"name": "Bob", "age": 25}

named(**details)


##################################################################

def named2(**kwargs):
    print(kwargs)


def print_nicely(**kwargs):
    named2(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")


print_nicely(name="Bob", age=25)


##################################################################

def both(*args, **kwargs):
    print(args)
    print(kwargs)


both(1, 3, 5, name="Bob", age=25)
