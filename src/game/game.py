import random
class Decision:
    HIT         = "HIT"
    STAND       = "STAND"
    DOUBLE      = "DOUBLE DOWN"
    SPLIT       = "SPLIT"
    INSUREON    = "ACCEPT INSURANCE"
    INSUREOFF   = "REFUSE INSURANCE"
    EQUAL       = "ACCEPT EQUAL PAYMENT"
    ERROR       = "ERROR"
class HandState:
    INITIAL     = "INITIAL"
    INPROGRESS  = "IN PROGRESS"
    COMPLETED   = "COMPLETED"
class HandResult:
    WONBJ       = "WON\t+150%"
    WON         = "WON\t+100%"
    LOST        = "LOST\t-100%"
    EQUAL       = "EQUAL\t0%"
    INSURED     = "INSURED\t50%"
class HandInsurance:
    INSURED     = "INSURED"
    UNINSURED   = "UNINSURED"
    EQUAL       = "EQUAL"
class Hand():    
    def __init__(self):
        self.cards = []
        self.state = HandState.INITIAL
        self.value = 0
        self.result = 0
        self.insurance = 0
    def analysis(self, croupier):
        croupierCard = croupier.getVisibleCard()
        self.cards.sort()
        print "* Hand Analysis"
        if croupier.initialBlackjackVerification == 1:
            print "! Croupier might have a blackjack"
            return Decision.INSUREOFF
        else:
            if len(self.cards) == 2:
                return self.analyzeInitialHand(croupierCard)
            else:
                return self.analyzeOtherHand(croupierCard)
    def analyzeInitialHand(self, croupierCard):
        decision = 0
        self.displayCards()
        if self.detectBlackjack():
            print "+ Blackjack detection"
            decision = Decision.STAND
        elif self.detectAces():
            print "+ Ace detection"
            if Cards.TWO in self.cards:
                print "  Ace and %s" % (Cards.TWO.name)
                if croupierCard.value >= 5 and croupierCard.value <= 6:
                    decision = Decision.DOUBLE
                else:
                    decision = Decision.HIT
            elif Cards.THREE in self.cards:
                print "  Ace and %s" % (Cards.THREE.name)
                if croupierCard.value >= 5 and croupierCard.value <= 6:
                    decision = Decision.DOUBLE
                else:
                    decision = Decision.HIT
            elif Cards.FOUR in self.cards:
                print "  Ace and %s" % (Cards.FOUR.name)
                if croupierCard.value >= 4 and croupierCard.value <= 6:
                    decision = Decision.DOUBLE
                else:
                    decision = Decision.HIT
            elif Cards.FIVE in self.cards:
                print "  Ace and %s" % (Cards.FIVE.name)
                if croupierCard.value >= 4 and croupierCard.value <= 6:
                    decision = Decision.DOUBLE
                else:
                    decision = Decision.HIT
            elif Cards.SIX in self.cards:
                print "  Ace and %s" % (Cards.SIX.name)
                if croupierCard.value >= 3 and croupierCard.value <= 6:
                    decision = Decision.DOUBLE
                else:
                    decision = Decision.HIT
            elif Cards.SEVEN in self.cards:
                print "  Ace and %s" % (Cards.SEVEN.name)
                if croupierCard.value >= 2 and croupierCard.value <= 8:
                    decision = Decision.STAND
                else:
                    decision = Decision.HIT
            elif Cards.EIGHT in self.cards:
                print "  Ace and %s" % (Cards.EIGHT.name)
                decision = Decision.STAND
            elif Cards.NINE in self.cards:
                print "  Ace and %s" % (Cards.NINE.name)
                decision = Decision.STAND
            elif Cards.ACE in self.cards:
                print "  Ace and %s" % (Cards.ACE.name)
                decision = Decision.SPLIT
        elif self.detectInitialDuplicateCard():
            print "+ Duplicate card detection"
            if Cards.TWO in self.cards:
                print "  Two %ss" % (Cards.TWO.name)
                if croupierCard.value >= 2 and croupierCard.value <= 7:
                    decision = Decision.SPLIT
                else:
                    decision = Decision.HIT
            if Cards.THREE in self.cards:
                print "  Two %ss" % (Cards.THREE.name)
                if croupierCard.value >= 2 and croupierCard.value <= 7:
                    decision = Decision.SPLIT
                else:
                    decision = Decision.HIT
            if Cards.FOUR in self.cards:
                print "  Two %ss" % (Cards.FOUR.name)
                if croupierCard.value >= 5 and croupierCard.value <= 6:
                    decision = Decision.SPLIT
                else:
                    decision = Decision.HIT
            if Cards.FIVE in self.cards:
                print "  Two %ss" % (Cards.FIVE.name)
                if croupierCard.value >= 2 and croupierCard.value <= 9:
                    decision = Decision.DOUBLE
                else:
                    decision = Decision.HIT
            if Cards.SIX in self.cards:
                print "  Two %ss" % (Cards.SIX.name)
                if croupierCard.value >= 2 and croupierCard.value <= 6:
                    decision = Decision.SPLIT
                else:
                    decision = Decision.HIT
            if Cards.SEVEN in self.cards:
                print "  Two %ss" % (Cards.SEVEN.name)
                if croupierCard.value >= 2 and croupierCard.value <= 7:
                    decision = Decision.SPLIT
                else:
                    decision = Decision.HIT
            if Cards.EIGHT in self.cards:
                print "  Two %ss" % (Cards.EIGHT.name)
                decision = Decision.SPLIT
            if Cards.NINE in self.cards:
                print "  Two %ss" % (Cards.NINE.name)
                if croupierCard.value >= 2 and croupierCard.value<= 9:
                    decision = Decision.SPLIT
                else:
                    decision = Decision.STAND
            if Cards.TEN in self.cards:
                print "  Two %ss" % (Cards.TEN.name)
                decision = Decision.STAND
            if Cards.JACK in self.cards:
                print "  Two %ss" % (Cards.JACK.name)
                decision = Decision.STAND
            if Cards.QUEEN in self.cards:
                print "  Two %ss" % (Cards.QUEEN.name)
                decision = Decision.STAND
            if Cards.KING in self.cards:
                print "  Two %ss" % (Cards.KING.name)
                decision = Decision.STAND
        else:
            print "- General hand"
            genSum = 0
            decision = self.analysisGeneralHand(croupierCard)
        print "  Croupier has %s" % (croupierCard.name)
        print "* You should %s" % (decision)
        return decision
    def analysisGeneralHand(self, croupierCard):
        decision = 0
        genSum = 0
        for card in self.cards:
            genSum = genSum + card.value
        if genSum > 21 and self.detectAces():
            print "I am choosing ace = 1"
            genSum = genSum - 10
        elif genSum <= 21 and self.detectAces():
            print "I am choosing ace = 11"
        print "  Player has \t%s" % (genSum)        
        if genSum >= 5 and genSum <= 8:
            decision = Decision.HIT
        elif genSum == 9:
            if croupierCard.value >= 3 and croupierCard.value <= 6:
                decision = Decision.DOUBLE
            else:
                decision = Decision.HIT
        elif genSum == 10:
            if croupierCard.value >= 2 and croupierCard.value <= 9:
                decision = Decision.DOUBLE
            else:
                decision = Decision.HIT
        elif genSum == 11:
            if croupierCard.value >= 2 and croupierCard.value <= 10:
                decision = Decision.DOUBLE
            else:
                decision = Decision.HIT
        elif genSum == 12:
            if croupierCard.value >= 4 and croupierCard.value <= 6:
                decision = Decision.STAND
            else:
                decision = Decision.HIT 
        elif genSum >= 13 and genSum <= 16:
            if croupierCard.value >= 2 and croupierCard.value <= 6:
                decision = Decision.STAND
            else:
                decision = Decision.HIT
        else:
            decision = Decision.STAND
        return decision
    def analyzeOtherHand(self, croupierCard):
        return self.analysisGeneralHand(croupierCard)
    def detectBlackjack(self):
        if len(self.cards) > 2:
            return 0
        if self.detectAces():
            sum = 0
            for card in self.cards:
                sum = sum + card.value
            if sum == 21:
                return 1
    def detectAces(self):
        for card in self.cards:
            if card.value == 11:
                return 1
    def detectInitialDuplicateCard(self):
        if self.cards[0].name == self.cards[1].name:
            return 1
    def displayCards(self):
        for card in self.cards:
            print "# %s\t\t%s" % (card.name, card.value)
    def calculateValue(self):
        sum = 0
        for card in self.cards:
            sum = sum + card.value
        if self.detectBlackjack():
            return 1
        if self.detectAces() and sum > 21:
            for card in self.cards:
                if card == Cards.ACE:
                    card.value = 1
        else:
            return sum
class Player:    
    def __init__(self, name):
        self.name = name
        self.hands = []
        self.hands.append(Hand())
        self.bet = 0
        self.balance = 0
class Croupier(Player):
    initialBlackjackVerification = 0
    def getVisibleCard(self):
        return self.hands[0].cards[1]
    def analysis(self):
        hand = self.hands[0]
        decision = 0
        if hand.detectBlackjack():
            print "Croupier has a Blackjack."
            hand.state = HandState.COMPLETED
            return HandState.COMPLETED
        sum = 0
        soft = 0
        for card in hand.cards:
            sum = sum + card.value
        if hand.detectAces() and sum > 21:
            print "Ace will be treated as 1"
            soft = 1
            sum = sum - 10
        elif hand.detectAces():
            soft = 1
            print "Ace will be treated as 11"
        print "Croupier has %d" % (sum)
        if soft:
            if sum <= 17:
                decision = Decision.HIT
            else:
                decision = Decision.STAND
        else:
            if sum <= 16:
                decision = Decision.HIT
            else:
                decision = Decision.STAND
        return decision
class Card:
    def __init__(self, name, value):
        self.name = name
        self.value = value
class Cards:
    TWO     = Card("two",2)
    THREE   = Card("three",3)
    FOUR    = Card("four",4)
    FIVE    = Card("five",5)
    SIX     = Card("six",6)
    SEVEN   = Card("seven",7)
    EIGHT   = Card("eight",8)
    NINE    = Card("nine",9)
    TEN     = Card("ten",10)
    JACK    = Card("jack",10)
    QUEEN   = Card("queen",10)
    KING    = Card("king",10)
    ACE     = Card("ace",11)
class Deck:
    def __init__(self):
        self.cards = []
        self.cards.append(Cards.TWO)
        self.cards.append(Cards.THREE)
        self.cards.append(Cards.FOUR)
        self.cards.append(Cards.FIVE)
        self.cards.append(Cards.SIX)
        self.cards.append(Cards.SEVEN)
        self.cards.append(Cards.EIGHT)
        self.cards.append(Cards.NINE)
        self.cards.append(Cards.TEN)
        self.cards.append(Cards.JACK)
        self.cards.append(Cards.QUEEN)
        self.cards.append(Cards.KING)
        self.cards.append(Cards.ACE)
        for i in range(2):
            self.cards.extend(self.cards)
class Shoe:
    def __init__(self, numberOfDecks):
        self.shoe = []
        for i in range(numberOfDecks):
            self.shoe.extend(Deck().cards)
        self.shuffle()
    def shuffle(self):
        random.shuffle(self.shoe)
class Game:
    numberOfPlayers = 6
    numberOfDecksInAShoe = 8
    players = []
    def initialization(self):
        self.shoe = Shoe(self.numberOfDecksInAShoe)
        for i in range(self.numberOfPlayers):
            self.players.append(Player(i))
        self.croupier = Croupier("Casino de Montreal")
        print "Number of cards: %d" % (len(self.shoe.shoe))
    def distributeCards(self):
        for i in range(2):
            for player in self.players:
                player.balance = player.balance - 1.0
                player.hands[0].cards.append(self.shoe.shoe.pop())
            self.croupier.hands[0].cards.append(self.shoe.shoe.pop())
    def play(self):     
        croupierHand = self.croupier.hands[0]
        if self.croupier.getVisibleCard() == Cards.ACE:
            print "CROUPIER HAS DECLARED INSURANCE IS OPENED."
            self.croupier.initialBlackjackVerification = 1
            for player in self.players:
                for hand in player.hands:
                    decision = hand.analysis(self.croupier)
                    if decision == Decision.INSUREOFF:
                        print "Insurance not taken."
                        hand.insurance = HandInsurance.UNINSURED
                    elif decision == Decision.INSUREON:
                        print "Insurance taken."
                        hand.money = hand.money * 0.5
                        hand.insurance = HandInsurance.INSURED
                    elif decision == Decision.EQUAL:
                        print "You have a blackjack and are asking for equal payment."
                        hand.money = hand.money * 2
                        hand.insurance = HandInsurance.EQUAL
                        hand.state = HandState.COMPLETED
                        hand.result = HandResult.WON
            print "Croupier has:"
            for card in croupierHand.cards:
                print card.name
            if croupierHand.detectBlackjack():
                print ">"
                print "! CROUPIER HAS A BLACKJACK"
                print ">"
                for player in self.players:
                    print "PLAYER:\t%s" % (player)
                    for hand in player.hands:
                        print "HAND:\t%s" % (hand)
                        if hand.insurance == HandInsurance.UNINSURED:
                            print "Hand was uninsured, it's a 100% loss."
                            hand.state = HandState.COMPLETED
                            hand.result = HandResult.LOST
                        elif hand.insurance == HandInsurance.INSURED:
                            print "Hand was insured, it's a 50% loss."
                            player.balance = player.balance + hand.money
                        elif hand.insurance == HandInsurance.EQUAL:
                            print "Player had a Blackjack and accepted equal payment."
                            print "Hand was won a 100%."
                            player.balance = player.balance + hand.money
                self.croupier.initialBlackjackVerification = 0
                return
            else:
                print "! CROUPIER DOESN'T HAVE A BLACKJACK."
                self.croupier.initialBlackjackVerification = 0
        playersAnalysisInProgress = 1
        while playersAnalysisInProgress > 0:
            playersAnalysisInProgress = 0
            for player in self.players:
                print ""
                print "PLAYER:\t%s" % (player)
                for hand in player.hands:
                    print "HAND:\t%s" % (hand)
                    if hand.state == HandState.INITIAL or hand.state == HandState.INPROGRESS:
                        print "STATE:\t%s" % (hand.state)
                        decision = hand.analysis(self.croupier)
                        if decision == Decision.HIT:
                            playersAnalysisInProgress = playersAnalysisInProgress + self.hit(hand)
                        elif decision == Decision.STAND:
                            playersAnalysisInProgress = playersAnalysisInProgress + self.stand(hand)
                        elif decision == Decision.DOUBLE:
                            playersAnalysisInProgress = playersAnalysisInProgress + self.double(player, hand)
                        elif decision == Decision.SPLIT:
                            playersAnalysisInProgress = playersAnalysisInProgress + self.split(player, hand)
                    elif hand.state == HandState.COMPLETED:
                        print "STATE:\tCOMPLETED (already)"
        print ""
        print "* START CROUPIER PLAY"
        croupierAnalysisInProgress = 1
        while croupierAnalysisInProgress:
            croupierAnalysisInProgress = 0
            if croupierHand.state == HandState.INITIAL or croupierHand.state == HandState.INPROGRESS:
                decision = self.croupier.analysis()
                if decision == Decision.HIT:
                    croupierAnalysisInProgress = croupierAnalysisInProgress + self.hit(croupierHand)
                if decision == Decision.STAND:
                    croupierAnalysisInProgress = croupierAnalysisInProgress + self.stand(croupierHand)
            elif croupierHand.state == HandState.COMPLETED:
                self.completed(croupierHand)
        print "FINAL:\t%s" % (croupierHand.value)
        print "* END CROUPIER PLAY"
        print ""
        print "* START FINAL ANALYSIS"
        for player in self.players:
            print ""
            print "PLAYER:\t%s" % (player)
            for hand in player.hands:
                print "HAND:\t%s" % (hand)
                print "FINAL:\t%s" % (hand.value)
                if hand.value > 21:
                    print "MSG:\tPLAYER BUSTED"
                    hand.result = HandResult.LOST
                elif hand.value == 1:
                    print "MSG:\tPLAYER BLACKJACK"
                    hand.result = HandResult.WONBJ
                elif croupierHand.value > 21:
                    print "MSG:\tCROUPIER BUSTED"
                    hand.result = HandResult.WON
                elif hand.value > croupierHand.value:
                    print "MSG:\tPLAYER WON"
                    hand.result = HandResult.WON
                elif hand.value == croupierHand.value:
                    print "MSG:\tPLAYER EQUAL CROUPIER"
                    hand.result = HandResult.EQUAL
                else:
                    print "MSG:\tPLAYER DEFAULT LOSS"
                    hand.money = 0
                    hand.result = HandResult.LOST
                print "RESULT:\t%s" % (hand.result)
        print ""
        print "* END FINAL ANALYSIS"
    def clear (self):
        for player in self.players:
            del player.hands[:]
            player.hands = []
            player.hands.append(Hand())
        del self.croupier.hands[:]
        self.croupier.hands = []
        self.croupier.hands.append(Hand())
    def hit(self, hand):
        card = self.shoe.shoe.pop()
        hand.cards.append(card)
        print "OPERA:\tHIT %s" % (card.name)
        hand.state = HandState.INPROGRESS
        print "STATE:\tIN PROGRESS"
        return 1
    def stand(self, hand):
        self.completed(hand)
        print "OPERA:\tSTAND on %s" % (hand.calculateValue())
        print "STATE:\tCOMPLETED"
        return 0
    def double(self, player, hand):
        card = self.shoe.shoe.pop()
        hand.cards.append(card)
        print "OPERA:\tDOUBLE DOWN %s" % (card.name)
        self.completed(hand)
        print "STATE:\tCOMPLETED"
        return 0
    def split(self, player, hand):
        card = hand.cards.pop()
        print "Splitting your %s in two hands" % (card.name)
        # Preparing first hand
        hand1 = Hand()
        hand1.cards.append(card)
        print "HAND1:\t%s" % (hand1)
        self.hit(hand1)
        player.hands.append(hand1)
        # Preparing second hand
        hand2 = Hand()
        hand2.cards.append(card)
        print "HAND2:\t%s" % (hand2)
        self.hit(hand2)
        player.hands.append(hand2)
        # Deleting the original hand
        player.hands.remove(hand)
        return 1
    def completed(self, hand):
        hand.value = hand.calculateValue()
        hand.state = HandState.COMPLETED
        return hand.value
    def stats(self):
        for player in self.players:
            print "PLAYER:\t%s" % (player)
            print "BALANCE:\t%d" % (player.balance)
            print "INVESTED:\t%d" % (player.bet)
g = Game()
g.initialization()
for i in range(5):
    g.stats()
    g.distributeCards()
    g.play()
    g.clear()