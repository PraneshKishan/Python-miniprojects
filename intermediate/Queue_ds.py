my_lst = []


def add_in_que(x):
    my_lst.append(x)
    print(my_lst)
    print("Element added")
    
def pop_in_que():
    if len(my_lst) == 0:
      print("Queue is Empty")
    else:
      my_lst.pop(0)
      print("Element popped")

while True:
    print("""1.Append
2.Pop
3.Quit""")
    choice = int(input("Enter here: "))
    if choice == 1:
        inp_append = input("Enter the elements: ")
        add_in_que(inp_append)
    elif choice == 2:
        pop_in_que()
    elif choice == 3:
        break
    
