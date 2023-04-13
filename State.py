from OP import OP
from MDA_EFSM import MDA_EFSM

class State:
    op: OP
    m: MDA_EFSM
    cups: int

    def __init__(self, op: OP, m: MDA_EFSM) -> None:
        self.cups = 0

    def create(self):
        pass
    def insertCups(self, n: int):
        pass
    def setPrice(self):
        pass
    def coin(self, c: bool):
        pass
    def disposeDrink(self, id: int):
        pass
    def additive(self, type: int):
        pass
    def cancel(self):
        pass

class Start(State):
    def create(self):
        self.op.StorePrice()

class NoCups(State):
    def coin(self, c: bool):
        self.op.ReturnCoins()
    
    def insertCups(self, n: int):
        if n > 0:
            self.cups = n
            self.op.ZeroCF()
            self.m.changeState(2)

class Idle(State):
    def coin(self, c: bool):
        self.op.IncreaseCF()
        if c:
            self.m.changeState(3)
    def insertCups(self, n: int):
        if n > 0:
            self.cups += n
    
class CoinInserted(State):
    pass