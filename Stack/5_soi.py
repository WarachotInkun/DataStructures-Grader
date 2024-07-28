s = input("******** Parking Lot ********\nEnter max of car,car in soi,operation : ").split(" ")
s[1] = s[1].split(",")
s[1] = [int(i) for i in s[1] ]
if 0 in s[1]:
    s[1]=[] 
if s[2]=="arrive":
    if len(s[1]) == int(s[0]):
        print(f"car {s[3]} cannot arrive : Soi Full")
        print(s[1])
    else:
        if int(s[3]) in s[1]:
            print(f"car {s[3]} already in soi")
            print(s[1])
        else:
            s[1].append(int(s[3]))
            print(f"car {s[3]} arrive! : Add Car {s[3]}")
            print(s[1])
else:
    if len(s[1]) == 0:
        print(f"car {s[3]} cannot depart : Soi Empty")
        print(s[1])
    else:
        if int(s[3]) not in s[1]:
            print(f"car {s[3]} cannot depart : Dont Have Car {s[3]}")
            print(s[1])
        else:
            s[1].remove(int(s[3]))
            print(f"car {s[3]} depart ! : Car {s[3]} was remove")
            print(s[1])