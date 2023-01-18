import csv
f1 = open('student.csv','w',newline= '')
w1 = csv.writer(f1,delimiter=',')
w1.writerow(['RollNo','Name','Marks'])
while True:
    op = int(input('Enter 1 to add and 0 to exit : '))
    if op ==1:
        rollno = input("Enter Roll No : ")
        name = input("Enter Name : ")
        marks = input("Enter Marks : ")
        w1.writerow([rollno,name,marks])
    elif op == 0:
        break
f1.close()