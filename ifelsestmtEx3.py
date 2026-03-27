#Program for accepting a digit and displaying its name.
#ifelsestmtex3.py
d=int(input("Enter the value:"))
if d==0:
    print("zero")
else:
    if d==1:
        print("one")
    else:
        if d==2:
            print("two")
        else:
            if d==3:
                print("three")
            else:
                if d==4:
                    print("four")
                else:
                    if d == 5:
                        print("five")
                    else:
                        if d == 6:
                            print("six")
                        else:
                            if d == 7:
                                print("seven")
                            else:
                                if d == 8:
                                    print("eight")
                                else:
                                    if d == 9:
                                        print("nine")
                                    else:
                                        if d>9:
                                            print("{} is a number".format(d))
                                        else:
                                            if d in [-1,-2,-3,-4,-5,-6,-7,-8,-9]:
                                                print("{} is a -ve digit".format(d))
                                            else:
                                                if d<0 and d not in [-1,-2,-3,-4,-5,-6,-7,-8,-9] :
                                                    print("{} is a -ve number".format(d))


