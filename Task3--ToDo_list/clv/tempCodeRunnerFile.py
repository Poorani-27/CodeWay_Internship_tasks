import random
task=[]
print("To Do List")
def add():
    global task
    print("\nAdd Task")
    n = int(input("Enter the number of task(s) you wanted to add : "))
    for i in range(n):
        tasks = input("Enter the Task : ")
        task.append(tasks)
def show():
    global task
    if not task: print("No task")
    else: print("\ntask To do : \t",task)   
def mark_complete():
    print("Mark The Task(s) that are completed")
    n = int(input("Enter the number of task(s) you completed : "))
    for i in range(n):
        print(task)
        tasks = input("Enter the Task completed : ")
        task.remove(tasks)
def choose_random():
    global task
    if not task : print("no task")
    else :
        dispaly_random = random.choice(task)
        print("random Choice : " ,dispaly_random)
while True:
    enter = input("\nSelect The Operation To do : \n1.Add \t2.Show \t3.choose random\t4.mark completed\t5.quit \nEnter: ").lower().strip()
    if enter == "1" or enter == "add": add()
    elif enter == "2" or enter == "show": show()
    elif enter == "3" or enter == "chooserandom": choose_random()
    elif enter == "4" or enter == "markcomplete": mark_complete()
    elif enter == "5" or enter == "quit":
        print("Exiting")
        break
    