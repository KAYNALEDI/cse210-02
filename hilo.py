import random 
def main():
    player_points  = 300
    points_won  = 100
    points_lost  = 75 
    print("Welcome to the High Low Game.Enjoy guessing!")

        
    #First card that the dealer picks
    def card():
        number  = random.randint(1,14)
        return number 
    #Second card that the dealer picks 
    def deal():
        deal = random.randint(1,14)
        return deal
    #While playing game is true 
    Playing_game  = True 
    while Playing_game:
        first_card  = card()
        print(f"The card is {first_card}")
        user  = input("High or Low?: ")
        card_deal  = deal()
        print(f"The new card is {card_deal}")
    

        if user == "high" and (card_deal > first_card):
            player_points += points_won 
        elif user =="high" and (card_deal < first_card):
            player_points -= points_lost
        elif user =="low" and (card_deal > first_card):
            player_points -= points_lost
        elif user == "low" and (card_deal < first_card):
            player_points += points_won 
        
        print(player_points)
        playing  = input("Do you want to keep playing? ")
        if playing == "no" or player_points == 0:
            Playing_game = False 

if __name__ == "__main__":
    main()



