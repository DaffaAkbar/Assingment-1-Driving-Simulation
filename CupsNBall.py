numlist=["ball","jackpot","3"]
def inputa():
    #swap index value
    numlist[0],numlist[1]=numlist[1],numlist[0]
    return numlist
def inputb():
    #swap index value
    numlist[1],numlist[2]=numlist[2],numlist[1]
    return numlist
def inputc():
    #swap index value
    numlist[0],numlist[2]=numlist[2],numlist[0]
    return numlist
def main():
    while(True):
        global numlist
        f=input("")
        aw=numlist.index("ball")
        if f=="a":
            inputa()
        if f=="b":
            inputb()
        if f=="c":
            inputc()
        #for showing the ball location
        if f=="show":
            print(aw+1)
main()


