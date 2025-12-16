#to do list
fulllist=[] # fulllist= the list that contains the tasks


def entering (tasklist):
    while True:
        task = input("Enter what to add in the list:") #task = adds each task to the tasklist
        if task.lower() == "exit":
            break
        else:
            tasklist.append(task)
    return tasklist


while not fulllist:
    entering(fulllist)
    if not fulllist:
        print("list is empty.")

for i in fulllist:
    print("-",i)
