# from State import State, Start, NoCups, Idle, CoinInserted
from __future__ import annotations
from OP import OP


class MDA_EFSM:
    states: list # 0: Start, 1: NoCups, 2: Idle, 3: CoinInserted
    s: State    # pint to current state

    def __init__(self, op: OP) -> None:
        d = StateData()
        self.states = [Start(op, self, d), NoCups(op, self, d), Idle(op, self, d), CoinInserted(op, self, d)]
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
        print(f'change sate to {s}')
        self.s = self.states[s]

class StateData:
    cups: int = 0
    A: list = [0]*10

class State:
    """
    Abstract class
    """
    op: OP
    m: MDA_EFSM
    d: StateData

    def __init__(self, op: OP, m: MDA_EFSM, d: StateData) -> None:
        self.op = op
        self.m = m
        self.d = d

    def create(self):
        pass
    def insertCups(self, n: int):
        pass
    def setPrice(self):
        pass
    def coin(self, c: bool):
        pass
    def card(self):
        pass
    def disposeDrink(self, id: int):
        pass
    def additive(self, type: int):
        pass
    def cancel(self):
        pass

class Start(State):
    """
    State Start
    """
    def create(self):
        self.op.StorePrice()
        self.d.cups = 0
        self.m.changeState(1)

class NoCups(State):
    """
    State No Cups
    """
    def coin(self, c: bool):
        self.op.ReturnCoins()
    
    def insertCups(self, n: int):
        if n > 0:
            self.d.cups = n
            self.op.ZeroCF()
            self.m.changeState(2)

class Idle(State):
    """
    State Idle
    """
    def coin(self, c: bool):
        
        self.op.IncreaseCF()

        if c:
            self.m.changeState(3)

    def card(self):
        self.op.ZeroCF()
        self.m.changeState(3)

    def insertCups(self, n: int):
        if n > 0:
            self.d.cups += n
    
    def setPrice(self):
        self.op.StorePrice()

class CoinInserted(State):
    """
    State Coin Inserted
    """
    def coin(self, c: bool):
        self.op.ReturnCoins()

    def additive(self, type: int):
        self.d.A[type] = not self.d.A[type]

    def disposeDrink(self, id: int):
        self.op.DisposeDrink(id)
        self.op.DisposeAdditives(self.d.A)

        if self.d.cups > 1:
            self.op.ZeroCF()
            self.d.cups -= 1
            self.m.changeState(2)
        else:
            self.d.cups = 0
            self.m.changeState(1)
        print(self.d.cups, self.d.A)