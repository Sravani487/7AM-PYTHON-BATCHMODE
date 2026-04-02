#Program accepting line of text and display the words of the
# line in opposite order
#ForloopEx10.py
line=input("Enter a line of text:")#python is an oop lang
words=line.split()#words=["python","is,"an","oop","lang"]
if len(words)!=0:
    for word in words[::-1]:
        print(word,"-->",word[::-1])
    print("----------------------------")
    for index in range(len(words)-1,-1,-1):
        print(words[index])
    print("----------------------------")
    for index in range(len(words)-1,-1,-1):
        print(words[index],"--->",words[index][::-1])


