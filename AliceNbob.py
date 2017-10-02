import sys
def GameStart():
    i=int(input("place numbers of stone"))
    #if input is even number than the program will print Alice
    if i %2==0:
        print("Bob")
        retry()
    #If input is odd number than the program will print Bob
    else:
        print("Alice")
        retry()
def retry():
    j=input("Do you want to continue? Y/N")
    if j =="y":
        GameStart()
    if j =="n":
        sys.exit()
GameStart()