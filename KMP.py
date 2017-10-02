s=str(input(""))
#split the input name by"-"
x=s.split("-")
def ninp():
    for i in x:
        print(i[0].title(),end="")
ninp()