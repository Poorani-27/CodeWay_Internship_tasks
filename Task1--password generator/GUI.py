import random
import tkinter as tk 
import string
import pyperclip
root =tk.Tk()
root.geometry("350x350")
root.title("Password Generator")
root.resizable(False,False)
root.config(bg="white")
def generate_password(length):
    characters = string.punctuation+string.ascii_letters+string.digits
    password = "".join(random.choice(characters) for _ in range (length))
    return password
def update_password():
    length= int(get_password.get())
    password = generate_password(length)
    Enter_password.config(state=tk.NORMAL)
    Enter_password.delete(1.0,tk.END) 
    Enter_password.insert(1.0,password)    
    Enter_password.config(state=tk.DISABLED)
    Btn_copy.config(text="Copy Password")       
def copy_password():
    password = Enter_password.get(1.0, tk.END).strip()
    pyperclip.copy(password)
    Btn_copy.config(text="Copied !")
def reset_copy():
    Enter_password.config(state=tk.NORMAL)
    Enter_password.delete(1.0 ,tk.END)
    Enter_password.config(state=tk.DISABLED)
    Btn_copy.config(text="Copy password")
title=tk.Label(root,text="Random Password Generator", font=(("Arial"),15),bg="white",width=30)
title.pack(pady=2)
Enter=tk.Label(root,text="Enter The Length of the password to be generated ", font=(("Arial"),8),bg="white",width=40)
Enter.pack(pady=2)
get_password = tk.Entry(root, font=(("Arial"),17),width=20,bg="White")
get_password.pack(pady=2)
Enter=tk.Label(root,text="Generated Password ", font=(("Arial"),8),bg="white",width=40)
Enter.pack(pady=2)
Enter_password = tk.Text(root, font=(("Arial"),17),width=20,height=2,bg="White" , state= tk.DISABLED )
Enter_password.pack(pady=2)
Btn_generate=tk.Button(root,text ="Generate Password", font=(("Arial"),16),bg="Black",fg="White",bd=4,command=update_password)
Btn_generate.pack(pady=5)
Btn_copy=tk.Button(root,text ="copy Password", font=(("Arial"),16),bg="Black",fg="White",bd=4,command=copy_password)
Btn_copy.pack(pady=5)
root.mainloop()