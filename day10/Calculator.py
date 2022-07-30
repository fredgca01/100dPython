#add
def add(n1,n2):
    """Add 2 numbers and return the result"""
    return n1+n2

def withdraw(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

def calculate(n1,symbol,n2):
    for operand in operations:
        if(operand==symbol):
            function=operations[operand]
            result=function(n1,n2)
            return result

operations={
    "*":multiply,
    "+":add,
    "-":withdraw,
    "/":divide
}

print("Welcome to the calculator\n")


while True:
    num1 = float(input("Give your first number: "))
    operation = input("What is the operation you want to apply ? (+,/,*,-): ")
    num2 = float(input("Give your second number: "))
    result = calculate(num1,operation,num2)
    print(f"{num1:.2f} {operation} {num2:.2f} = {result:.2f}")
    next=True
    while next:
        answer = input(f"Another operation with {result:.2f}? (Y/N): ").lower()
        if(answer=="y"):
            globalResult=result
            operation = input("What is the operation you want to apply ? (+,/,*,-): ")
            num3 = float(input("Give your second number: "))
            result = calculate(globalResult, operation, num3)
            print(f"{globalResult:.2f} {operation} {num3:.2f} = {result:.2f}")
        else:
            next=False


