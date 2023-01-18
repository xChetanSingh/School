def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
def help():
    print('''
This is How to Use the Calculator
    # It works for two numbers 
    # Enter Both Numbers First
    # Select oprator based on ur choice :
        - "+" for adding
        - "-" for subtracting
        - "*" for multiplying
        - "/" for devideing
    ''')
def main():
    help()
    while True :
        a = eval(input("Enter First Number : "))
        b = eval(input("Enter Secound Number : "))
        c = input("Enter Oprator : ")
        if c == "+":
            print(add(a,b))
        elif c == "-":
            print(sub(a,b))
        elif c == "*":
            print(mul(a,b))
        elif c == "/":
            print(div(a,b))
        else :
            print("Invalid Oprator")

        x = int(input('''
Press Any Key to Run Again
        0 to Exit
        3 for Help

        '''))
        if x== 3 :
            help()
        elif x == 0 :
            break

    print("Thx For Using !!!")

if __name__ == '__main__':
    main()