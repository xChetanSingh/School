Package = []
def MakePush(Package):
    a = int(input('Enter Package Title : '))
    Package.append(a)

def MakePop(Package):
    if Package==[]:
        print("Stack Empty , Underflow !")
    else :
        print("DEleted Book is : ",Package.pop())