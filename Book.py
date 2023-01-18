Book = []
def Addnew(s):
    Name = input('Enter Book Name : ')
    Book.append(Name)

def Remove():
    if Book==[]:
        print("Stack Empty , Underflow !")
    else :
        print("DEleted Book is : ",Book.pop())