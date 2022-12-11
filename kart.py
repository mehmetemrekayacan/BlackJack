import random

card=["HEARTS","DİAMONDS","CLUBS","SPADES"]
number=["A","K","Q","J","10","9","8","7","6","5","4","3","2"]

youCard=random.choice(card)
youNumber=random.choice(number)

dealerCard=random.choice(card)
dealerNumber=random.choice(number)

yourTotal=0
dealerTotal=0
game=True

while game==True:
    def sec():
        select=input("1: HİT\n2: STAY\n")
        return select
    break
    
def you():
    if sec()=="1":
        if youNumber=="A":
            if yourTotal<=11:
                yourTotal+=10
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
    return yourTotal

def dealer():
    if sec()=="1":
        if dealerNumber=="A":
            if dealerTotal<=11:
                dealerTotal+=10
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
    return dealerTotal

if yourTotal<21 and dealerTotal<21:
    if yourTotal>dealerTotal:
        while dealerTotal>=21:
            dealerTotal+=dealer()
            if dealerTotal>21:
                print("Dealer bust! You win!")
            elif dealerTotal==21:
                print("Blackjack! Dealer win!")
            else:
                print("Dealer lost! You win!")
    
        

print(yourTotal)