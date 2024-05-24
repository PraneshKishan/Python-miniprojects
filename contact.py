
    
class Contact_person:
    def __init__(self, fname, lname, ph_no, email):
        self.fname = fname
        self.lname = lname
        self.ph_no = ph_no
        self.email = email
        
class Contact_operations:
    def __init__(self):
        self.contact_list = []
               
    def save_contact(self, contact_person):
        self.contact_list.append(contact_person)
        
    def view_contact(self):
        print(self.contact_list)
        for i in self.contact_list:
            print(f"Full Name: {i.fname} {i.lname}\nPhone number: {i.ph_no}\nE-mail: {i.email}")
            print(i)
        
        

c1 = Contact_person("First name","Last name","Phone number","yourgmail@gmail.com")   

a1 = Contact_operations()
a1.save_contact(c1)
a1.view_contact()



