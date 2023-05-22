class Deck():
    def __init__(self) -> None:
        pass

def game_of_war():
    d = Deck()
    d.shuffle()

    player1 = Player()
    player2 = Player()

    half_deck = d.half()
    player1.retrieve(half_deck)

    half_deck = d.half()
    player2 