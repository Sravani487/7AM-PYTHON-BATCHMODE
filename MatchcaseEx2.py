#program for accepting the days of a week and displaying whether it is weekday or holiday
#MatchcaseEx2.py
wdy=input("Enter the day of week:")
wdy=wdy.upper()
match (wdy) :
    case "MONDAY":
        print("{} is a working day".format(wdy))
    case "TUESDAY":
        print("{} is a working day".format(wdy))
    case "WEDNESDAY":
        print("{} is a working day".format(wdy))
    case "THURSDAY":
        print("{} is a working day".format(wdy))
    case "FRIDAY":
        print("{} is a working day".format(wdy))
    case "SATURDAY":
        print("{} is a week end".format(wdy))
    case "SUNDAY":
        print("{} is a Holiday".format(wdy))
    case _:
        print("{} is not a week day".format(wdy))