import random
l=["GOOGLE","FREEDOM","WISDOM","TEMPER","FACEBOOK","ACCESS","SANDWICH","FLORIDE","ENGLAND","INDIA","MASTER","APPROACH"]
while True:
    i = random.choice(l)
    word=len(i)*" _"
    letter=word.split()
    print(f"Word:{word}")
    actual_word=list(i)
    j=1
    l1=[]
    while(j<=10):
        n = input("Enter letter:")
        if n.upper() not in l1:
            l1.append(n.upper())
            m=0
            for k in range(len(actual_word)):
                if n.upper() in actual_word:
                    position=actual_word.index(n.upper())
                    letter[position]=n.upper()
                    actual_word[position]="?"
                    m+=1
                if m==0:
                    print("INVALID, LETTER NOT IN WORD")
                    j+=1
                    print(f"Attempt Remaining:{11-j}")
                    if j==2:
                        print("-------")
                    if j==3:
                        print("-------")
                        print("|     ")
                    if j==4:
                        print("-------")
                        print("|     |")
                    if j==5:
                        print("-------")
                        print("|     |")
                        print("|     ")
                    if j==6:
                        print("-------")
                        print("|     |")
                        print("|     O")
                    if j==7:
                        print("-------")
                        print("|     |")
                        print("|     O")
                        print('|      \ ')
                    if j==8:
                        print("-------")
                        print("|     |")
                        print("|     O")
                        print('|     |\ ')
                    if j==9:
                        print("-------")
                        print("|     |")
                        print("|     O")
                        print('|    /|\ ')

                    if j==10:
                        print("-------")
                        print("|     |")
                        print("|     O")
                        print('|    /|\ ')
                        print("___")
                    if j==11:
                        print("-------")
                        print("|     |")
                        print("|     |")
                        print("|     |")
                        print("___   O")
                        print('     /|\ ')
                    break
        else:
            print("You Already have used this Letter")
        if letter == list(i):
            print(f"Congratulations You guess the right word:{i}")
            break
        print("Word:", end="")
        print(" ".join(letter))
    else:
        print(f"You loss actual word was:{i}")
    check = input("Do you want to continue (Y/N):").upper()
    if check == "N":
        break