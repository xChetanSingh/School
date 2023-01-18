import pickle

def set_data():
    empcode = int(input('Enter Employee code: '))
    name = input('Enter Employee name: ')
    salary = int(input('Enter salary: '))
    print()
    employee = [empcode,name,salary]
    
    return employee


def display_data(employee):
    print('Employee code:', employee[0])
    print('Employee name:', employee[1])
    print('Salary:', employee[2])
    print()


def write_record():
    outfile = open('emp.dat', 'ab')
    pickle.dump(set_data(), outfile)
    outfile.close()


def read_records():
    infile = open('emp.dat', 'rb')
    while True:
        try:
            employee = pickle.load(infile)
            display_data(employee)
        except EOFError:
            break
    infile.close()

def search_record():
    infile = open('emp.dat', 'rb')
    empcode = int(input('Enter employee code to search: '))
    flag = False
    while True:
        try:
            employee = pickle.load(infile)
            if employee[0] == empcode:
                display_data(employee)
                flag = True
                break
            
        except EOFError:
            break

    if flag == False:
        print('Record not Found')
        print()
        
    infile.close()

def show_choices():
    print('Menu')
    print('1. Add Record')
    print('2. Display Records')
    print('3. Search a Record')
    print('4. Exit')

def main():
    while(True):
        show_choices()
        choice = input('Enter choice(1-4): ')
        print()
        
        if choice == '1':
            write_record()
            
        elif choice == '2':
            read_records()

        elif choice == '3':
            search_record()

        elif choice == '4':
            break
        
        else:
            print('Invalid input')
            
#call the main function.
main()