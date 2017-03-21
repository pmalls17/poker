import random
stake=100
ante=10
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

def main():
    """Main method of the program
       Parameters: n/a
    """
    global stake
    global ante
    if startup()=="y":
        randomNumber()
        sort_hand(hand)
        hand1=hand()
        PlayerHand=checkRank(hand1)
        print(":player hand")
        printHand(hand.card1,hand.card2,hand.card3)
        randomNumber()
        sort_hand(hand)
        hand2=hand()
        ComputerHand=checkRank(hand2)
        if playOrFold()=="y":
            if doesComputerFold(hand2)==False:
                if higher_hand(PlayerHand,ComputerHand)==True:
                    stake=stake+2*ante
                    print("player wins!")
                else:
                    stake=stake-2*ante
                    print("computer wins!")
            else:
                stake=stake+ante
                print(":computer folds")
        else:
            stake=stake-ante
        print(":computer hand")
        printHand(hand.card1,hand.card2,hand.card3)  
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
        print("goodbye")
        return "n"
    
        
 


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
        d="2C"
    elif x==3 and y==20:
        d="3C"
    elif x==4 and y==20:
        d="4C"
    elif x==5 and y==20:
        d="5C"
    elif x==6 and y==20:
        d="6C"
    elif x==7 and y==20:
        d="7C"
    elif x==8 and y==20:
        d="8C"
    elif x==9 and y==20:
        d="9C"
    elif x==10 and y==20:
        d="10C"
    elif x==11 and y==20:
        d="JC"
    elif x==12 and y==20:
        d="QC"
    elif x==13 and y==20:
        d="KC"
    elif x==14 and y==20:
        d="AC"
    elif x==2 and y==21:
        d="2D"
    elif x==3 and y==21:
        d="3D"
    elif x==4 and y==21:
        d="4D"
    elif x==5 and y==21:
        d="5D"
    elif x==6 and y==21:
        d="6D"
    elif x==7 and y==21:
        d="7D"
    elif x==8 and y==21:
        d="8D"
    elif x==9 and y==21:
        d="9D"
    elif x==10 and y==21:
        d="10D"
    elif x==11 and y==21:
        d="JD"
    elif x==12 and y==21:
        d="QD"
    elif x==13 and y==21:
        d="KD"
    elif x==14 and y==21:
        d="AD" 
    elif x==2 and y==22:
        d="2H"
    elif x==3 and y==22:
        d="3H"
    elif x==4 and y==22:
        d="4H"
    elif x==5 and y==22:
        d="5H"
    elif x==6 and y==22:
        d="6H"
    elif x==7 and y==22:
        d="7H"
    elif x==8 and y==22:
        d="8H"
    elif x==9 and y==22:
        d="9H"
    elif x==10 and y==22:
        d="10H"
    elif x==11 and y==22:
        d="JH"
    elif x==12 and y==22:
        d="QH"
    elif x==13 and y==22:
        d="KH"
    elif x==14 and y==22:
        d="AH"
    elif x==2 and y==23:
        d="2S"
    elif x==3 and y==23:
        d="3S"
    elif x==4 and y==23:
        d="4S"
    elif x==5 and y==23:
        d="5S"
    elif x==6 and y==23:
        d="6S"
    elif x==7 and y==23:
        d="7S"
    elif x==8 and y==23:
        d="8S"
    elif x==9 and y==23:
        d="9S"
    elif x==10 and y==23:
        d="10S"
    elif x==11 and y==23:
        d="JS"
    elif x==12 and y==23:
        d="QS"
    elif x==13 and y==23:
        d="KS"
    elif x==14 and y==23:
        d="AS"
    x=card2.rank
    y=card2.suit
    if x==2 and y==20:
        c="2C"
    elif x==3 and y==20:
        c="3C"
    elif x==4 and y==20:
        c="4C"
    elif x==5 and y==20:
        c="5C"
    elif x==6 and y==20:
        c="6C"
    elif x==7 and y==20:
        c="7C"
    elif x==8 and y==20:
        c="8C"
    elif x==9 and y==20:
        c="9C"
    elif x==10 and y==20:
        c="10C"
    elif x==11 and y==20:
        c="JC"
    elif x==12 and y==20:
        c="QC"
    elif x==13 and y==20:
        c="KC"
    elif x==14 and y==20:
        c="AC"
    elif x==2 and y==21:
        c="2D"
    elif x==3 and y==21:
        c="3D"
    elif x==4 and y==21:
        c="4D"
    elif x==5 and y==21:
        c="5D"
    elif x==6 and y==21:
        c="6D"
    elif x==7 and y==21:
        c="7D"
    elif x==8 and y==21:
        c="8D"
    elif x==9 and y==21:
        c="9D"
    elif x==10 and y==21:
        c="10D"
    elif x==11 and y==21:
        c="JD"
    elif x==12 and y==21:
        c="QD"
    elif x==13 and y==21:
        c="KD"
    elif x==14 and y==21:
        c="AD" 
    elif x==2 and y==22:
        c="2H"
    elif x==3 and y==22:
        c="3H"
    elif x==4 and y==22:
        c="4H"
    elif x==5 and y==22:
        c="5H"
    elif x==6 and y==22:
        c="6H"
    elif x==7 and y==22:
        c="7H"
    elif x==8 and y==22:
        c="8H"
    elif x==9 and y==22:
        c="9H"
    elif x==10 and y==22:
        c="10H"
    elif x==11 and y==22:
        c="JH"
    elif x==12 and y==22:
        c="QH"
    elif x==13 and y==22:
        c="KH"
    elif x==14 and y==22:
        c="AH"
    elif x==2 and y==23:
        c="2S"
    elif x==3 and y==23:
        c="3S"
    elif x==4 and y==23:
        c="4S"
    elif x==5 and y==23:
        c="5S"
    elif x==6 and y==23:
        c="6S"
    elif x==7 and y==23:
        c="7S"
    elif x==8 and y==23:
        c="8S"
    elif x==9 and y==23:
        c="9S"
    elif x==10 and y==23:
        c="10S"
    elif x==11 and y==23:
        c="JS"
    elif x==12 and y==23:
        c="QS"
    elif x==13 and y==23:
        c="KS"
    elif x==14 and y==23:
        c="AS"
    x=card3.rank
    y=card3.suit
    if x==2 and y==20:
        b="2C"
    elif x==3 and y==20:
        b="3C"
    elif x==4 and y==20:
        b="4C"
    elif x==5 and y==20:
        b="5C"
    elif x==6 and y==20:
        b="6C"
    elif x==7 and y==20:
        b="7C"
    elif x==8 and y==20:
        b="8C"
    elif x==9 and y==20:
        b="9C"
    elif x==10 and y==20:
        b="10C"
    elif x==11 and y==20:
        b="JC"
    elif x==12 and y==20:
        b="QC"
    elif x==13 and y==20:
        b="KC"
    elif x==14 and y==20:
        b="AC"
    elif x==2 and y==21:
        b="2D"
    elif x==3 and y==21:
        b="3D"
    elif x==4 and y==21:
        b="4D"
    elif x==5 and y==21:
        b="5D"
    elif x==6 and y==21:
        b="6D"
    elif x==7 and y==21:
        b="7D"
    elif x==8 and y==21:
        b="8D"
    elif x==9 and y==21:
        b="9D"
    elif x==10 and y==21:
        b="10D"
    elif x==11 and y==21:
        b="JD"
    elif x==12 and y==21:
        b="QD"
    elif x==13 and y==21:
        b="KD"
    elif x==14 and y==21:
        b="AD" 
    elif x==2 and y==22:
        b="2H"
    elif x==3 and y==22:
        b="3H"
    elif x==4 and y==22:
        b="4H"
    elif x==5 and y==22:
        b="5H"
    elif x==6 and y==22:
        b="6H"
    elif x==7 and y==22:
        b="7H"
    elif x==8 and y==22:
        b="8H"
    elif x==9 and y==22:
        b="9H"
    elif x==10 and y==22:
        b="10H"
    elif x==11 and y==22:
        b="JH"
    elif x==12 and y==22:
        b="QH"
    elif x==13 and y==22:
        b="KH"
    elif x==14 and y==22:
        b="AH"
    elif x==2 and y==23:
        b="2S"
    elif x==3 and y==23:
        b="3S"
    elif x==4 and y==23:
        b="4S"
    elif x==5 and y==23:
        b="5S"
    elif x==6 and y==23:
        b="6S"
    elif x==7 and y==23:
        b="7S"
    elif x==8 and y==23:
        b="8S"
    elif x==9 and y==23:
        b="9S"
    elif x==10 and y==23:
        b="10S"
    elif x==11 and y==23:
        b="JS"
    elif x==12 and y==23:
        b="QS"
    elif x==13 and y==23:
        b="KS"
    elif x==14 and y==23:
        b="AS"
    print(d,c,b)


def higher_hand(hand1,hand2):
    if hand1>=hand2:
        return True
    else:
        return False

def checkRank(hand):
    if straightFlush(hand)==True:
        return 7
    else:
        if threeOfAKind(hand)==True:
            return 6
        else:
            if straight(hand)==True:
                return 5
            else:
                if flush(hand)==True:
                    return 4
                else:
                    if pair(hand)==True:
                        return 3
                    else:
                        if hand.card3.rank==2:
                            return 1.02
                        elif hand.card3.rank==3:
                            return 1.03
                        elif hand.card3.rank==4:
                            return 1.04
                        elif hand.card3.rank==5:
                            return 1.05
                        elif hand.card3.rank==6:
                            return 1.06
                        elif hand.card3.rank==7:
                            return 1.07
                        elif hand.card3.rank==8:
                            return 1.08
                        elif hand.card3.rank==9:
                            return 1.09
                        elif hand.card3.rank==10:
                            return 1.1
                        elif hand.card3.rank==11:
                            return 1.11
                        elif hand.card3.rank==12:
                            return 1.12
                        elif hand.card3.rank==13:
                            return 1.13
                        elif hand.card3.rank==14:
                            return 1.14


def straightFlush(hand):
    if ((hand.card3.rank-1)==(hand.card2.rank)) and ((hand.card2.rank-1)==hand.card1.rank) and ((hand.card1.suit==hand.card2) and (hand.card2.suit==hand.card3.suit)):
        return True
    else:
        return False

def threeOfAKind(hand):
    if (hand.card1.rank==hand.card2.rank) and (hand.card2.rank==hand.card3.rank):
       return True
    else:
        return False

def straight(hand):
    if (hand.card3.rank-1)==(hand.card2.rank) and ((hand.card2.rank-1)==hand.card1.rank):
        return True
    else:
        return False

def flush(hand):
    if ((hand.card1.suit==hand.card2) and (hand.card2.suit==hand.card3.suit)):
        return True
    else:
        return False
def pair(hand):
    if (hand.card1.rank==hand.card2.rank) or (hand.card1.rank==hand.card3.rank) or (hand.card2.rank==hand.card3.rank):
        return True
    else:
        return False
 
def doesComputerFold(hand2):
    if checkRank(hand2)>=1.12:
       return False
    else:
        return True
    
##def noRepeatCard(hand):
##    if (hand.card1.rank==hand.card2.rank and hand.card1.suit==hand.card2.suit) or (hand.card1.rank==hand.card3.rank and hand.card1.suit==hand.card3.suit) or (hand.card2.rank==hand.card3.rank and hand.card2.suit==hand.card3.suit): 
##        return False
##    else:
##        return True
main()     
    
    
        
        
    
        
    
        








