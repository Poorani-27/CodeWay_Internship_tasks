import tkinter as tk
import time
from tkinter import messagebox
root = tk.Tk()
root.geometry("460x600")
root.title("To DO List")
root.config(bg="pink")
def add():
    task_text =task.get()
    if task_text:
        task_frame=tk.Frame(Display_task,bg="white")
        task_frame.pack(fill=tk.X,padx=2,pady=5)
        task_label = tk.Label(task_frame,width=40 ,text=task_text,bg="white",anchor="w")
        task_label.pack(side=tk.LEFT)
        remove_button =tk.Button(task_frame,text="remove",bg="red",fg="white", command=lambda:remove_task(task_frame))
        remove_button.pack(side=tk.RIGHT)
        task.delete(0, tk.END)
    else:messagebox.showwarning("WARNING","Enter A Task")
def remove_task(task_frame):task_frame.destroy()
def date():
    date=time.strftime("%A %d %B %y")
    Display_date.config(text=date)
Display_date= tk.Label(root,bg="pink",font=("Arial",10,"bold"),text="")
Display_date.pack(pady=2, padx=2)
Display_title = tk.Label(root,bg="pink",font=("Arial",16,"bold"),text="TO DO LIST")
Display_title.pack(pady=2, padx=2)
task = tk.Entry(root,bg="white",width=30,font=("Arial",16,"bold"))
task.pack(pady=4,padx=2)
Add_button=tk.Button(root,bg="blue",font=("Arial",10,"bold") ,width=20,text="ADD",height=1,command=add,pady=3)
Add_button.pack(pady=3)
Display_task = tk.Frame(root,bg="pink",width=2,height=3)
Display_task.pack(pady=20)
date()
root.mainloop()