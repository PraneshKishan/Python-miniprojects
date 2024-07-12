import random

class contact_detail:
    def __init__(self,fname='',lname='',ph_no=0,email=''): #polymorphism
        self.ID = random.randint(0,1000)
        self.fname = fname
        self.lname = lname
        self.ph_no = ph_no
        self.email = email


class contact_operation:
    def __init__(self):
        self.contacts = []

    def see_all_contacts(self):
        all_cont_list = []
        for i in range(len(self.contacts)):
            all_cont_list.append(self.contacts[i].fname)
        return f".{all_cont_list}"
    
    def store_contact(self,st_contact):
        self.contacts.append(st_contact)

    def read_contact(self,read_con_inp):
        subset_vals = []
        for contact in self.contacts:
            value = contact_detail(contact)
            if read_con_inp  in contact.fname:
                subset_vals.append(contact)
        return subset_vals
    
    
            
    def edit_contact(self,to_be_edited,field,newValue):
        if field == 1:
            to_be_edited.fname = newValue
        elif field == 2:
            to_be_edited.lname = newValue
        elif field == 3:
            to_be_edited.ph_no = newValue
        elif field == 4:
            to_be_edited.email = newValue
        for Index in range(len(self.contacts)):
            contact = self.contacts[Index]
            print(contact.ID, to_be_edited.ID)  
            if contact.ID == to_be_edited.ID:
                self.contacts[Index] = to_be_edited
                
    def delete_contact(self,to_be_del):
        for Index in range(len(self.contacts)):
            contact = self.contacts[Index]
            if contact.ID == to_be_del.ID:
                del self.contacts[Index]
                print("Deleted successfully ")
                break
        

class selector:
    def selecting_contact(self,selecting_con):
        for i in range(len(selecting_con)):
                print(i,'.',selecting_con[i].fname,selecting_con[i].ID)
        select_con = int(input("\nEnter the contact: "))
        return selecting_con[select_con]
                
class main:
       
    se = selector()
    co = contact_operation()
    co.store_contact(contact_detail(fname="abc"))
    co.store_contact(contact_detail(fname = "pranesh"))
    co.store_contact(contact_detail(fname = "prane"))
    while True:
        print("What do you want to do?")
        print("A. Create a contact")
        print("B. Read the contact")
        print("C. Update the contact")
        print("D. Delete the contact")
        print("Q. Quit program")
        
        inp = str(input("Enter your option: "))
        
        if inp.lower() == 'a':
            fir_name = fir_name = str(input("Enter first name: "))
            last_name = str(input("Enter last name: "))
            phone = int(input("Enter phone number: "))
            mail = input("Enter E-mail: ")
            person = contact_detail(fir_name,last_name,phone,mail)
            co.store_contact(person)
            print("Contact Successfully created\n")      

        elif inp.lower() == 'b':
            read_inp = str(input("Enter your contact name:"))
            read_ans = co.read_contact(read_inp)
            print(read_ans)
            for i in read_ans:
                print(i.fname,i.lname,i.ph_no,i.email)
            
        elif inp.lower() == 'c':
            up_con_key = input("Enter contact name you want to edit: ")
            up_con = co.read_contact(up_con_key)
            print(up_con)
            selected_to_be_edited = se.selecting_contact(up_con)
            print("1.fname , 2.lname, 3.Phone number, 4.E-mail")
            selected_field = int(input("select field:"))
            update_value = input("value to be edited: ")
            co.edit_contact(selected_to_be_edited,selected_field,update_value)
            
        elif inp.lower() == 'd':
            del_con_key = input("Enter contact name you want to delete: ")
            del_con_read = co.read_contact(del_con_key)
            del_con = se.selecting_contact(del_con_read)
            co.delete_contact(del_con)
            
        elif inp.lower() == 'q':
            break
