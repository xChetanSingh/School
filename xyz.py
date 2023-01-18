import csv
f1 = open('xyz.csv','w',newline= '')
w1 = csv.writer(f1,delimiter='\t')
w1.writerow(['BookNo','BookName','Pages'])
while True:
    op = int(input('Enter 1 to add and 0 to exit : '))
    if op ==1:
        Bookno = int(input("Enter Book No : "))
        Bookname = input("Enter Book Name : ")
        pages = int(input("Enter Pages : "))
        w1.writerow([Bookno,Bookname,pages])
    elif op == 0:
        break
f1.close()