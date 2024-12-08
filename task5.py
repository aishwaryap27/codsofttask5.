print("\t\t\t CONTACT BOOK\t\t\t")
print("Main Menu")
d1={}
def getdata():
    name=input("enter the name")
    phno=int(input("enter the ph no"))
    email=input("enter email id")
    address=input("enter the address")
    d1[name]={"name":name,"phno":phno,"email":email,"address":address}
    print("details updated successfully")
def show():
    if not d1:
        print("empty list")
    else:
        for name,details in d1.items():
            print(f"Name: {details['name']}")
            print(f"Phone: {details['phno']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}\n")
while(True):
    print("1.Add contact \n 2.View contacts \n 3.Search contact \n 4.Update contact \n 5.Delete contact")
    n=int(input("enter your choice"))
    if(n==1):
            # print("enter nam
        a=int(input("enter the number of contacts "))
        for i in range(a):
            getdata()
            
                #break;
    elif(n==2):
        show()
    elif(n==3):
        print("option selected:search contact:\n")
        contact=input("enter the name of the contact you want to search")
        if contact in d1:
            contactnew = d1[contact]
            print(f"Name: {contactnew['name']}")
            print(f"Phone: {contactnew['phno']}")
            print(f"Email: {contactnew['email']}")
            print(f"Address: {contactnew['address']}\n")
        else:
            print("entered contact is not there in the contact list")
    elif(n==4):
        print("list has to be updated")
        updatedc=input("enter the name u want to updated")
        if updatedc in d1:
             print("Choose what to update:")
             print("1. Phno")
             print("2. Email")
             print("3. Address")
             ch=int(input("Enter your choice: "))
             if(ch== 1):
                 print("choice opted:phone number to be updated")
                 newphn=int(input("enter the new phone number"))
                 d1[updatedc]['phno']=newphn
             if(ch==2):
                 print("email has to be updated")
                 nwemail=input("enter the new email")
                 d1[updatedc]['email']=nwemail
             if(ch==3):
                 print("address has to be updated")
                 nwadd=input("enter the new email")
                 d1[updatedc]['address']=nwadd
             else:
                 print("invalid choice")
        else:
            print("contact dteails not found")
    elif(n==5):
        print("delete contact\n")
        dela=input("enter the contact nmae you want to delete")
        if dela in d1:
            #dela=input("enter name to delete")
            del d1[dela]
            print(f"contact{dela}deleted successfully")
        else:
            print("contact found")
    elif (n==6):
        print("exiting the contact the book")
        break
    else:
        print("invalid choice")
        
        
        
            





   
    
       
