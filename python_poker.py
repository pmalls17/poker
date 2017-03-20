import random
## Code by Paul Mallary && Brendan Aszklar
#python project



class hand:
    """model of hand
       Attriutes:
           card1
           card2
           card3
    """
    card1=0,0
    card2=0,0
    card3=0,0
class card:
    """model of hand
    Attributes:
        rank
        suit
    """
    rank=2
    suit=20

stake=100
ante=10
def main():
    """Main method of the program
       Parameters: n/a
    """
    global stake
    global ante
    startup()
    randomNumber()
    sort_hand(hand)
    print("player hand")
    printHand(hand.card1,hand.card2,hand.card3)
    randomNumber()
    sort_hand(hand)
    print("computer hand")
    printHand(hand.card1,hand.card2,hand.card3)
    if playOrFold()=="y":
        stake=stake+ante
    else:
        stake=stake-ante
    main()
    
def playOrFold():
    """ determines if the player is going to play or fold
        Parameters: n/a
        returns: Play or fold
    """
    answer="p"
    while answer=="p":
        answer=input("play or fold")
        if answer=="play":
            return "y" 
        elif answer=="fold":
            return "n" 
        else:
            answer="p"

print("hello welcome to python three card poker") 
def startup():
    """determines if the players stake is twice the ante, then asks them if they want to continue playing
    parameters: none
    return: yes if they want to continue playing"""
    if stake>=(2*ante):
        play="k"
        while play!=("y" or "n"):
            print("youre stake is",stake," and the ante is 10") 
            play=input("would you like to keep playing")
            if play=="y":
                return "y"
            elif play=="n":
                print("goodbye")
                break
            else:
                play="p"
    else:
        return "y"
    
        
 


def randomNumber():
    """ creates 3 instances of card, which makes an instance of hand
    parameters:none
    return:none"""
    rank1=random.randint(2,14)
    suit1=random.randint(20,23)
    rank2=random.randint(2,14)
    suit2=random.randint(20,23)
    rank3=random.randint(2,14)
    suit3=random.randint(20,23)
    c1=card()
    c1.rank=rank1
    c1.suit=suit1
    hand.card1=c1
    c2=card()
    c2.rank=rank2
    c2.suit=suit2
    hand.card2=c2
    c3=card()
    c3.rank=rank3
    c3.suit=suit3
    hand.card3=c3


def sort_hand(hand):
    """Sort a hand of cards into ascending order in place
    Parameter: hand; instance of Hand
    Returns: None"""
    if hand.card1.rank>hand.card2.rank:
        temp=hand.card1
        hand.card1=hand.card2
        hand.card2=temp
    if hand.card2.rank>hand.card3.rank:
        temp=hand.card2
        hand.card2=hand.card3
        hand.card3=temp
    if hand.card1.rank>hand.card2.rank:
        temp=hand.card1
        hand.card1=hand.card2
        hand.card2=temp
    

def printHand(card1,card2,card3):
    """ Determines the cards given to the players
        parameters: card1,card2,card3
        return: cards to the hand
    """
    x=card1.rank
    y=card1.suit
    if x==2 and y==20:
        print("2C")
    elif x==3 and y==20:
        print("3C")
    elif x==4 and y==20:
        print("4C")
    elif x==5 and y==20:
        print("5C")
    elif x==6 and y==20:
        print("6C")
    elif x==7 and y==20:
        print("7C")
    elif x==8 and y==20:
        print("8C")
    elif x==9 and y==20:
        print("9C")
    elif x==10 and y==20:
        print("10C")
    elif x==11 and y==20:
        print("JC")
    elif x==12 and y==20:
        print("QC")
    elif x==13 and y==20:
        print("KC")
    elif x==14 and y==20:
        print("AC")
    elif x==2 and y==21:
        print("2D")
    elif x==3 and y==21:
        print("3D")
    elif x==4 and y==21:
        print("4D")
    elif x==5 and y==21:
        print("5D")
    elif x==6 and y==21:
        print("6D")
    elif x==7 and y==21:
        print("7D")
    elif x==8 and y==21:
        print("8D")
    elif x==9 and y==21:
        print("9D")
    elif x==10 and y==21:
        print("10D")
    elif x==11 and y==21:
        print("JD")
    elif x==12 and y==21:
        print("QD")
    elif x==13 and y==21:
        print("KD")
    elif x==14 and y==21:
        print("AD")
    elif x==2 and y==22:
        print("2H")
    elif x==3 and y==22:
        print("3H")
    elif x==4 and y==22:
        print("4H")
    elif x==5 and y==22:
        print("5H")
    elif x==6 and y==22:
        print("6H")
    elif x==7 and y==22:
        print("7H")
    elif x==8 and y==22:
        print("8H")
    elif x==9 and y==22:
        print("9H")
    elif x==10 and y==22:
        print("10H")
    elif x==11 and y==22:
        print("JH")
    elif x==12 and y==22:
        print("QH")
    elif x==13 and y==22:
        print("KH")
    elif x==14 and y==22:
        print("AH")
    elif x==2 and y==23:
        print("2S")
    elif x==3 and y==23:
        print("3S")
    elif x==4 and y==23:
        print("4S")
    elif x==5 and y==23:
        print("5S")
    elif x==6 and y==23:
        print("6S")
    elif x==7 and y==23:
        print("7S")
    elif x==8 and y==23:
        print("8S")
    elif x==9 and y==23:
        print("9S")
    elif x==10 and y==23:
        print("10S")
    elif x==11 and y==23:
        print("JS")
    elif x==12 and y==23:
        print("QS")
    elif x==13 and y==23:
        print("KS")
    elif x==14 and y==23:
        print("AS")
    x=card2.rank
    y=card2.suit
    if x==2 and y==20:
        print("2C")
    elif x==3 and y==20:
        print("3C")
    elif x==4 and y==20:
        print("4C")
    elif x==5 and y==20:
        print("5C")
    elif x==6 and y==20:
        print("6C")
    elif x==7 and y==20:
        print("7C")
    elif x==8 and y==20:
        print("8C")
    elif x==9 and y==20:
        print("9C")
    elif x==10 and y==20:
        print("10C")
    elif x==11 and y==20:
        print("JC")
    elif x==12 and y==20:
        print("QC")
    elif x==13 and y==20:
        print("KC")
    elif x==14 and y==20:
        print("AC")
    elif x==2 and y==21:
        print("2D")
    elif x==3 and y==21:
        print("3D")
    elif x==4 and y==21:
        print("4D")
    elif x==5 and y==21:
        print("5D")
    elif x==6 and y==21:
        print("6D")
    elif x==7 and y==21:
        print("7D")
    elif x==8 and y==21:
        print("8D")
    elif x==9 and y==21:
        print("9D")
    elif x==10 and y==21:
        print("10D")
    elif x==11 and y==21:
        print("JD")
    elif x==12 and y==21:
        print("QD")
    elif x==13 and y==21:
        print("KD")
    elif x==14 and y==21:
        print("AD")
    elif x==2 and y==22:
        print("2H")
    elif x==3 and y==22:
        print("3H")
    elif x==4 and y==22:
        print("4H")
    elif x==5 and y==22:
        print("5H")
    elif x==6 and y==22:
        print("6H")
    elif x==7 and y==22:
        print("7H")
    elif x==8 and y==22:
        print("8H")
    elif x==9 and y==22:
        print("9H")
    elif x==10 and y==22:
        print("10H")
    elif x==11 and y==22:
        print("JH")
    elif x==12 and y==22:
        print("QH")
    elif x==13 and y==22:
        print("KH")
    elif x==14 and y==22:
        print("AH")
    elif x==2 and y==23:
        print("2S")
    elif x==3 and y==23:
        print("3S")
    elif x==4 and y==23:
        print("4S")
    elif x==5 and y==23:
        print("5S")
    elif x==6 and y==23:
        print("6S")
    elif x==7 and y==23:
        print("7S")
    elif x==8 and y==23:
        print("8S")
    elif x==9 and y==23:
        print("9S")
    elif x==10 and y==23:
        print("10S")
    elif x==11 and y==23:
        print("JS")
    elif x==12 and y==23:
        print("QS")
    elif x==13 and y==23:
        print("KS")
    elif x==14 and y==23:
        print("AS")
    x=card3.rank
    y=card3.suit
    if x==2 and y==20:
        print("2C")
    elif x==3 and y==20:
        print("3C")
    elif x==4 and y==20:
        print("4C")
    elif x==5 and y==20:
        print("5C")
    elif x==6 and y==20:
        print("6C")
    elif x==7 and y==20:
        print("7C")
    elif x==8 and y==20:
        print("8C")
    elif x==9 and y==20:
        print("9C")
    elif x==10 and y==20:
        print("10C")
    elif x==11 and y==20:
        print("JC")
    elif x==12 and y==20:
        print("QC")
    elif x==13 and y==20:
        print("KC")
    elif x==14 and y==20:
        print("AC")
    elif x==2 and y==21:
        print("2D")
    elif x==3 and y==21:
        print("3D")
    elif x==4 and y==21:
        print("4D")
    elif x==5 and y==21:
        print("5D")
    elif x==6 and y==21:
        print("6D")
    elif x==7 and y==21:
        print("7D")
    elif x==8 and y==21:
        print("8D")
    elif x==9 and y==21:
        print("9D")
    elif x==10 and y==21:
        print("10D")
    elif x==11 and y==21:
        print("JD")
    elif x==12 and y==21:
        print("QD")
    elif x==13 and y==21:
        print("KD")
    elif x==14 and y==21:
        print("AD")
    elif x==2 and y==22:
        print("2H")
    elif x==3 and y==22:
        print("3H")
    elif x==4 and y==22:
        print("4H")
    elif x==5 and y==22:
        print("5H")
    elif x==6 and y==22:
        print("6H")
    elif x==7 and y==22:
        print("7H")
    elif x==8 and y==22:
        print("8H")
    elif x==9 and y==22:
        print("9H")
    elif x==10 and y==22:
        print("10H")
    elif x==11 and y==22:
        print("JH")
    elif x==12 and y==22:
        print("QH")
    elif x==13 and y==22:
        print("KH")
    elif x==14 and y==22:
        print("AH")
    elif x==2 and y==23:
        print("2S")
    elif x==3 and y==23:
        print("3S")
    elif x==4 and y==23:
        print("4S")
    elif x==5 and y==23:
        print("5S")
    elif x==6 and y==23:
        print("6S")
    elif x==7 and y==23:
        print("7S")
    elif x==8 and y==23:
        print("8S")
    elif x==9 and y==23:
        print("9S")
    elif x==10 and y==23:
        print("10S")
    elif x==11 and y==23:
        print("JS")
    elif x==12 and y==23:
        print("QS")
    elif x==13 and y==23:
        print("KS")
    elif x==14 and y==23:
        print("AS")
    
    
    
main()     
