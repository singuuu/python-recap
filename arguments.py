def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg

    return total


print(multiply(5, 7, 9))


##################################################################


def add(x, y):
    return x + y


nums = [3, 5]
print(add(*nums))

##################################################################

nums = {"x": 15, "y": 2}
print(add(**nums))


##################################################################

def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()."


print(apply(1, 2, 3, 4, 5, operator="*"))
