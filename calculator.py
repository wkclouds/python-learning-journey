
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


if __name__ == "__main__":
    print("Testing calculator functions:")

    print("Addition:", add(10, 30))
    print("Subtraction:", subtract(50, 20))
    print("Multiplication:", multiply(5, 4))
    print("Division:", divide(100, 10))
