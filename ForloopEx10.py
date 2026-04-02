#Program accepting line of text and display the words of the line.
#ForloopEx10.py
line=input("Enter a line of text:")#python is an oop lang
words=line.split() # words=["python" "is" "an" "oop" "lang"]
if len(words)!=0:
    for word in words:
        print("\t{}".format(word))
else:
    print("Ur line is empty-can't find no of words")

