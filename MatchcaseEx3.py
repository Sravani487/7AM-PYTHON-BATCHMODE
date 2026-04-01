#program for accepting the day and decide whether it is working day or holiday
#MatchcaseEx3.py
wdy=input("Enter the day of the week:")
wdy=wdy.upper()
match (wdy):
    case "MONDAY"|"TUESDAY"|"WEDNESDAY"|"THURSDAY"|"FRIDAY":
        print("{} is a working day".format(wdy))
    case "SATURDAY":
        print("{} is a week day".format(wdy))
    case "SUNDAY":
        print("{} is a Holiday".format(wdy))
    case _:
        print("{} is not a weekday".format(wdy))