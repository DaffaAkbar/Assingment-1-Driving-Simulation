# u=Initial Velocity
# a=Acceleration=input
# t=Time Spent=input
# T=Time
# d=Distance=input
# sl=speedlimit
while (True):
    T =0
    sl = 60
    p = 2
    o=10
    d = int(input("Distance is"))
    a = int(input("Acceleration is"))
    t = int(input("Time spent is"))
    while (T <= t):
        Destination = int(a * T * T / p)
        finalvel =int(a * t)
        destination = int((a * T * T / p)/10)
        if (T<= t):
            print("Duration:", T, "Distance:", "*"* destination)
            T = T + 1
    while (T>=t):
        finalvel = (a * t)
        Destination =(t / 2) * finalvel
        if finalvel > sl:
            print("Max Speed was",finalvel,"m/s, congratz you went over the speed limit")
        if finalvel <= sl:
            print("Max speed was",finalvel," m/s")
        if Destination >= d:
            print("Reached at",Destination,"m")
        if Destination < d:
            print("did not reach destination",Destination,"m")
        if (T>=t):
            quit()




