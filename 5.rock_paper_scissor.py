#rock paper scissor game
player1=input("Enter the name of player1 :")
player2=input("Enter the name of player2 :")

print("press 1 for rock,2 for paper and 3 for scissor")

ans1=int(input("%s, what do you choose?" %player1))
ans2=int(input("%s, what do you choose?" %player2))

def compare(a1,a2):
    if a1==a2:
        return("its a tie")

    elif a1==1:
        if a2==2:
            return("%s wins" %player2)
        else:
            return("%s wins" %player1)

    elif a1==2:
        if a2==3:
            return("%s wins" %player2)
        else:
            return("%s wins" %player1)

    elif a1==3:
        if a2==1:
            return("%s wins" %player2)
        else:
            return("%s wins" %player1)

    else:
        return("you haven't entered 1,2 or 3, please try again")
        

print(compare(ans1,ans2))
