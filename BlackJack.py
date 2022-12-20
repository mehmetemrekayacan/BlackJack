import random

money=int(input("Enter your money: "))
print(f"Your money {money}$")

while money>0:
    bet=int(input("Enter your bet: "))
    card=["HEARTS","DİAMONDS","CLUBS","SPADES"]
    number=["A","K","Q","J","10","9","8","7","6","5","4","3","2"]

    youCard=random.choice(card)
    youNumber=random.choice(number)

    dealerCard=random.choice(card)
    dealerNumber=random.choice(number)

    yourTotal=0
    dealerTotal=0

    if youNumber=="A":
        if yourTotal<=11:
            yourTotal+=11
        else:
            yourTotal+=1
    elif youNumber=="K":
        yourTotal+=10
    elif youNumber=="Q":
        yourTotal+=10
    elif youNumber=="J":
        yourTotal+=10
    elif youNumber=="10":
        yourTotal+=10
    elif youNumber=="9":
        yourTotal+=9
    elif youNumber=="8":
        yourTotal+=8
    elif youNumber=="7":
        yourTotal+=7
    elif youNumber=="6":
        yourTotal+=6
    elif youNumber=="5":
        yourTotal+=5
    elif youNumber=="4":
        yourTotal+=4
    elif youNumber=="3":
        yourTotal+=3
    elif youNumber=="2":
        yourTotal+=2

    if dealerNumber=="A":
        if dealerTotal<=11:
            dealerTotal+=11
        else:
            dealerTotal+=1
    elif dealerNumber=="K":
        dealerTotal+=10
    elif dealerNumber=="Q":
        dealerTotal+=10
    elif dealerNumber=="J":
        dealerTotal+=10
    elif dealerNumber=="10":
        dealerTotal+=10
    elif dealerNumber=="9":
        dealerTotal+=9
    elif dealerNumber=="8":
        dealerTotal+=8
    elif dealerNumber=="7":
        dealerTotal+=7
    elif dealerNumber=="6":
        dealerTotal+=6
    elif dealerNumber=="5":
        dealerTotal+=5
    elif dealerNumber=="4":
        dealerTotal+=4
    elif dealerNumber=="3":
        dealerTotal+=3
    elif dealerNumber=="2":
        dealerTotal+=2
        
    print(f"Your hand {youCard} {youNumber}, Total: {yourTotal}\nDealer hand {dealerCard} {dealerNumber}, Total: {dealerTotal}")

    while yourTotal<21 and dealerTotal<17:
        select=input("1: HİT or 2: STAY\n:")
        
        if select=="1":
            youCard=random.choice(card)
            youNumber=random.choice(number)
            if youNumber=="A":
                if yourTotal<=11:
                    yourTotal+=11
                else:
                    yourTotal+=1
            elif youNumber=="K":
                yourTotal+=10
            elif youNumber=="Q":
                yourTotal+=10
            elif youNumber=="J":
                yourTotal+=10
            elif youNumber=="10":
                yourTotal+=10
            elif youNumber=="9":
                yourTotal+=9
            elif youNumber=="8":
                yourTotal+=8
            elif youNumber=="7":
                yourTotal+=7
            elif youNumber=="6":
                yourTotal+=6
            elif youNumber=="5":
                yourTotal+=5
            elif youNumber=="4":
                yourTotal+=4
            elif youNumber=="3":
                yourTotal+=3
            elif youNumber=="2":
                yourTotal+=2
        
        elif select=="2":
            while dealerTotal<17:
                dealerNumber=random.choice(number)
                if dealerNumber=="A":
                    if dealerTotal<=11:
                        dealerTotal+=11
                    else:
                        dealerTotal+=1
                elif dealerNumber=="K":
                    dealerTotal+=10
                elif dealerNumber=="Q":
                    dealerTotal+=10
                elif dealerNumber=="J":
                    dealerTotal+=10
                elif dealerNumber=="10":
                    dealerTotal+=10
                elif dealerNumber=="9":
                    dealerTotal+=9
                elif dealerNumber=="8":
                    dealerTotal+=8
                elif dealerNumber=="7":
                    dealerTotal+=7
                elif dealerNumber=="6":
                    dealerTotal+=6
                elif dealerNumber=="5":
                    dealerTotal+=5
                elif dealerNumber=="4":
                    dealerTotal+=4
                elif dealerNumber=="3":
                    dealerTotal+=3
                elif dealerNumber=="2":
                    dealerTotal+=2

        print(f"Your hand {youCard} {youNumber} Your total {yourTotal}")

    print(f"Your total {yourTotal}, Dealer total {dealerTotal}") 

        
    if yourTotal<=21 and dealerTotal<=21:
            if dealerTotal==21:
                print("Blackjack! Dealer win!")
                money-=bet
            elif yourTotal==21:
                print("Blackjack! You win!")
                money+=bet
            elif yourTotal>dealerTotal:
                print("Dealer lost! You win!")
                money+=bet
            elif yourTotal<dealerTotal:
                print("You lost! Dealer win!")
                money-=bet
    elif yourTotal>21:
        print("You bust! Dealer win!")
        money-=bet
    elif dealerTotal>21:
        print("Dealer bust! You win!")
        money+=bet
    print(f"Your money {money}$")
    if money>0:
        select_coe=input("1.Continue or 2.End: ")
        if select_coe=="1":
            continue
        elif select_coe=="2":
            break
    else:
        break
if money<=0:
    print("You sank!")