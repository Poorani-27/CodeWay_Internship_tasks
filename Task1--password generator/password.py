import random 
import string
def generate_password(length):
    characters = string.punctuation+string.digits+string.ascii_letters
    password = "".join(random.choice(characters) for _ in range (length))
    return password
if __name__=="__main__":
    try:
        print("\n\t\t\t Random password Generator")
        a =int(input("\nEnter The Length Of The password To Be generated : "))
        new_password = generate_password(a)
        print("\n\t\t\tGenerated Password == ", new_password ,"\n\n")
    except ValueError as e:
        print("Invalid Input !! {} !! Try Again".format(e))






