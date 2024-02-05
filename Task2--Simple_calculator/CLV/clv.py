import math
def calculate():
    def sum(a,b):
        print(f"\nThe result of adding {a} and {b}  = {a+b}")
    def sub(a,b):
        print(f"\nThe result of subtracting {a} and {b}  = {a-b}")
    def mul(a,b):
        print(f"\nThe result of multiplying {a} and {b}  = {a*b}")
    def div(a,b):
        print(f"\nThe result of dividing {a} and {b}  = {a/b}")  
    print("\n\t\t\tSimple calculator")
    a=float(input("\nEnter the first number : "))
    b=float(input("\nEnter the Second number : "))
    while True:
        print(''' Press 'q' or "quit" or "end to stop" ''')
        option = input ("\nEnter The Operation to be performed \n1.Addition \t2.Subtraction \t3.Multiplication \t4.Division :\t").lower()
        if option == "add" or option== "addition" or option=="1":
            sum(a,b)
        elif option == "sub" or option== "subtraction" or option=="2":
            sub(a,b)
        elif option == "mul" or option== "multiplication" or option=="3":
            mul(a,b)
        elif option == "div" or option== "division" or option=="4":
            div(a,b)   
        elif option == "q" or option== "quit" or option=="end":
            print("Existing Calculator")
            break 
        else:
            print ("Something Went wrong")
        continue
if __name__ == "__main__":
    try:
        do =calculate()
    except Exception as e:
        print("Error ! {}".format(e))