#program for displaying each character using while loop and for loop
#ForloopEx1.py
s="python"
print("Displaying each character using while loop")
i=0
while(i<len(s)):
    print("\t{}".format(s[i]))
    i=i+1
else:
    print("-------------------")
print("Displaying each character using for loop")
for k in s:
    print("\t {}".format(k))
else:
    print("--------------------")