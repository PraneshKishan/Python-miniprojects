my_lst = []


def add_in_stack(x):
    my_lst.append(x)
    print(my_lst)
    
def pop_in_stack():
    if len(my_lst) == 0:
      print("Queue is Empty")
    else:
        my_lst.pop(-1)
    
def find_len():
    print("Length: ",len(my_lst))

def empt_or_not():
    if len(my_lst) == 0:
        print("Stack is Empty")
    else:
        print("There are",len(my_lst),"elements")

while True:
    print("""1.Append
2.Pop
3.find len of list
4.View List
5.Find lst is empty or not
6.Quit""")
    choice = int(input("Enter here: "))
    if choice == 1:
        inp_append = input("Enter the elements: ")
        add_in_stack(inp_append)

    elif choice == 2:
        pop_in_stack()
    elif choice == 3:
        find_len()
    elif choice == 4:
        print(my_lst)
    elif choice == 5:
        empt_or_not()
    elif choice == 6:
        break
    
