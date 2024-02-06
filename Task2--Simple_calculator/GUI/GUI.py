import tkinter as tk 
root= tk.Tk()
root.geometry("330x440")
root.title("Simple Calculator")
root.resizable(False, False)
root.config(bg = "white")

calculation = ""
calculation_history=[]

def add(symbol):
    global calculation
    calculation+= str(symbol)
    result.delete(1.0, "end")
    result.insert(1.0 , calculation)
    
def perform():
    global calculation, calculation_history
    try:
        answer= eval(calculation)
        result.delete(1.0, "end")
        result.insert(1.0 , answer)
        calculation_history.append(calculation)
        calculation= str(answer)
    except:
        clear()
        result.insert(1.0, "ERROR")
def clear():
    global calculation
    calculation=""
    result.delete(1.0, "end")
def undo():
    global calculation, calculation_history
    if calculation:
        calculation = calculation_history.pop()
        result.delete(1.0, "end")
        result.insert(1.0, calculation)
def delete():
    global calculation
    if calculation:
        calculation=calculation[:-1]
        result.delete(1.0, "end")
        result.insert(1.0, calculation)
        


result = tk.Text(root, font=('Arial' , 15 ,"bold"), width= 29, height = 1, pady=20)
result.grid(row=1, columnspan= 9)

Btn_7=tk.Button(root,text="7", width=3, height=1, bg="white",fg="black", font=("Arial",20,"bold"), command=lambda:add(7))
Btn_7.grid(row=2, column=3, pady=5, padx=5)

Btn_8=tk.Button(root,text="8", width=3, height=1, bg="white",fg="black", font=("Arial",20,"bold"), command=lambda:add(8))
Btn_8.grid(row=2, column=4, pady=5, padx=5)

Btn_9=tk.Button(root,text="9", width=3, height=1, bg="white",fg="black", font=("Arial",20,"bold"), command=lambda:add(9))
Btn_9.grid(row=2, column=5, pady=5, padx=5)

Btn_4=tk.Button(root,text="4", width=3, height=1, bg="white",fg="black", font=("Arial",20,"bold"), command=lambda:add(4))
Btn_4.grid(row=3, column=3, pady=5, padx=5)

Btn_5=tk.Button(root,text="5", width=3, height=1, bg="white",fg="black", font=("Arial",20,"bold"), command=lambda:add(5))
Btn_5.grid(row=3, column=4, pady=5, padx=5)

Btn_6=tk.Button(root,text="6", width=3, height=1, bg="white",fg="black", font=("Arial",20,"bold"), command=lambda:add(6))
Btn_6.grid(row=3, column=5, pady=5, padx=5)


Btn_3=tk.Button(root,text="3", width=3, height=1, bg="white",fg="black", font=("Arial",20,"bold"), command=lambda:add(3))
Btn_3.grid(row=4, column=3, pady=5, padx=5)

Btn_2=tk.Button(root,text="2", width=3, height=1, bg="white",fg="black", font=("Arial",20,"bold"), command=lambda:add(2))
Btn_2.grid(row=4, column=4, pady=5, padx=5)

Btn_1=tk.Button(root,text="1", width=3, height=1, bg="white",fg="black", font=("Arial",20,"bold"), command=lambda:add(1))
Btn_1.grid(row=4, column=5, pady=5, padx=5)

Btn_plus=tk.Button(root,text="+", width=3, height=1, bg="Orange",fg="black", font=("Arial",20,"bold"), command=lambda:add("+"))
Btn_plus.grid(row=2, column=6, pady=5, padx=5)


Btn_open=tk.Button(root,text="(", width=3, height=1, bg="orange",fg="black", font=("Arial",20,"bold"), command=lambda:add("("))
Btn_open.grid(row=5, column=3, pady=5, padx=5)

Btn_0=tk.Button(root,text="0", width=3, height=1, bg="white",fg="black", font=("Arial",20,"bold"), command=lambda:add("0"))
Btn_0.grid(row=5, column=4, pady=5, padx=5)

Btn_close=tk.Button(root,text=")", width=3, height=1, bg="Orange",fg="black", font=("Arial",20,"bold"), command=lambda:add(")"))
Btn_close.grid(row=5, column=5, pady=5, padx=5)

Btn_minus=tk.Button(root,text="-", width=3, height=1, bg="Orange",fg="black", font=("Arial",20,"bold"), command=lambda:add("-"))
Btn_minus.grid(row=3, column=6, pady=5, padx=5)

Btn_mul=tk.Button(root,text="x", width=3, height=1, bg="Orange",fg="black", font=("Arial",20,"bold"), command=lambda:add("*"))
Btn_mul.grid(row=4, column=6, pady=5, padx=5)

Btn_div=tk.Button(root,text="/", width=3, height=1, bg="Orange",fg="black", font=("Arial",20,"bold"), command=lambda:add("/"))
Btn_div.grid(row=5, column=6, pady=5, padx=5)

Btn_clear=tk.Button(root,text="clear", width=4, height=1, bg="red",fg="black", font=("Arial",15,"bold"), command=clear)
Btn_clear.grid(row=6, column=6, pady=5, padx=0)

Btn_delete=tk.Button(root,text="Del", width=4, height=1, bg="red",fg="black", font=("Arial",15,"bold"), command=delete)
Btn_delete.grid(row=6, column=4, pady=5, padx=0)

Btn_undo=tk.Button(root,text="Undo", width=4, height=1, bg="red",fg="black", font=("Arial",15,"bold"), command=undo)
Btn_undo.grid(row=6, column=3, pady=5, padx=0)

Btn_pow=tk.Button(root,text="pow", width=4, height=1, bg="grey",fg="black", font=("Arial",15,"bold"), command=lambda:add("**"))
Btn_pow.grid(row=6, column=5, pady=5, padx=0)

Btn_equal=tk.Button(root,text="=", width=20, height=1, bg="yellow",fg="black", font=("Arial",15,"bold"), command= perform)
Btn_equal.grid(row=7, columnspan=11, pady=6, padx=5)

root.mainloop()