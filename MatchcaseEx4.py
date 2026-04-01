#program for accepting the day and decide whether it is working day or holiday
#MatchcaseEx4.py
wdy=input("Enter the day of the week:")
if wdy.upper() in ["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY","MON","TUE","WED","THU","FRI","SAT","SUN"]:
    match (wdy.upper()[0:3]):
        case "MON"|"TUE"|"WED"|"THU"|"FRI":
            print("{} is a working day".format(wdy))
        case "SAT":
            print("{} is a week end".format(wdy))
        case "SUN":
            print("{} is a holiday".format(wdy))
