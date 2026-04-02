#Program for displaying each char from a given string.
#ForloopEx8.py
s="python"
print("----------------------------------------------")
print("By using for loop without Indices in Forward Direction")
for ch in s:
    print("\t{}".format(ch))
print("----------------------------------------------")
print("By using for loop with +VE Indices in Forward Direction")
for i in range(0,len(s)):
    print("\t{}".format(s[i]))
print("----------------------------------------------")
print("By using for loop with -VE Indices in Forward Direction")
for i in range(-len(s),0):
    print("\t{}".format(s[i]))
print("----------------------------------------------")
print("By using for loop without Indices in Backward Direction ")
for ch in s[::-1]:
    print("\t{}".format(ch))
print("----------------------------------------------")
print("By using for loop with +VE Indices in Backward Direction ")
for i in range(len(s)-1,-1,-1):
    print("\t{}".format(s[i]))
print("----------------------------------------------")
print("By using for loop with -VE Indices in Backward Direction ")
for i in range(-1,-(len(s)+1),-1):
    print("\t{}".format(s[i]))
