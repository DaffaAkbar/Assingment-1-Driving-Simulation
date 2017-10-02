number=[]
def inp():
    #input until 10 numbers
    while len(number)<10:
        j = input()
        number.append(int(j)%42)
        if len(number)==10:
            print(len(set(number)))
inp()