import os
chances = 5
guessingstr = input("First Person Enter the string:")
postoShow = []
n = int(input("Enter the index you want to show the guesser:"))
while n != -1:
    postoShow.append(n)
    n = int(input("Enter the index you want to show the guesser:"))
strtoshow = ""
os.system('cls')
for i in range(0, len(guessingstr)):
    if i in postoShow:
        strtoshow = strtoshow + guessingstr[i]
    elif guessingstr[i] == " ":
        strtoshow += " "
    else:
        strtoshow += "_"
while chances != 0 and guessingstr != strtoshow:
    print("\nGuess the character for:", strtoshow, " Chances left:", chances)
    ch = input("Enter your input:")
    if ch in guessingstr:
        for i in range(0, len(guessingstr)):
            if guessingstr[i] == ch:
                if(i!=0 and i!=len(guessingstr)-1):
                    strtoshow=strtoshow[:i]+ch+strtoshow[i+1:]
                elif(i==0):
                    strtoshow=ch+strtoshow[i+1:]
                elif(i==len(guessingstr)-1):
                    strtoshow=strtoshow[:i]+ch
    else:
        chances-=1
    # os.system('cls')
if(guessingstr==strtoshow):
    print("Guesser Won")
else:
    print("Word selector won.")