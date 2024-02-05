import math
def calculate():
    def sum(a,b):
        print(f"The result of adding {a} and {b}  = {a+b}")
    def sub(a,b):
        print(f"The result of subtracting {a} and {b}  = {a-b}")
    def mul(a,b):
        print(f"The result of multiplying {a} and {b}  = {a*b}")
    def div(a,b):
        print(f"The result of dividing {a} and {b}  = {a/b}")  
    print("Simple calculator")
    a=float(input("\nEnter the first number : "))
    b=float(input("\nEnter the Second number : "))
    option = input ("\nEnter The Operation to be performed \n1.Addition \t2.Subtraction \t3.Multiplication \t4.Division").lower()
    if option == "add" or option== "addition" or option=="1":
        sum(a,b)
    elif option == "sub" or option== "subtraction" or option=="2":
        sub(a,b)
    elif option == "mul" or option== "multiplication" or option=="3":
        mul(a,b)
    elif option == "div" or option== "division" or option=="4":
        div(a,b)    
    else:
        print ("Something Went wrong")
    
if __name__ == "__main__":
    try:
        do =calculate()
    except Exception as e:
        print("Error ! {}".format(e))