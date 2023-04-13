from State import State, Start, NoCups, Idle, CoinInserted


class MDA_EFSM:
    states: list
    s: State

    def __init__(self) -> None:
        self.states = [Start(), NoCups(), Idle(), CoinInserted()]
        self.s = self.states[0]

    def create(self):
        self.s.create()

    def insertCups(self, n: int):
        self.s.insertCups(n)

    def setPrice(self):
        self.s.setPrice()
    
    def coin(self, c: bool):
        self.s.coin(c)

    def disposeDrink(self, id: int):
        self.s.disposeDrink(id)

    def additive(self, type: int):
        self.s.additive(type)

    def cancel(self):
        self.s.cancel()

    def changeState(self, s: int):
        self.s = self.states[s]