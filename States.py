from __future__ import annotations
from OP import OP


"""
This file implements the Decentralized state pattern.
"""


class MDA_EFSM:
    """
    Context of the state pattern
    """
    states: list    # 0: Start, 1: NoCups, 2: Idle, 3: CoinInserted
    s: State        # pint to current state

    def __init__(self, op: OP) -> None:
        d = StateData()
        self.states = [Start(self, d, op), NoCups(self, d, op), Idle(
            self, d, op), CoinInserted(self, d, op)]
        self.s = self.states[0]

    def create(self):
        self.s.create()

    def insertCups(self, n: int):
        self.s.insertCups(n)

    def setPrice(self):
        self.s.setPrice()

    def coin(self, c: bool):
        self.s.coin(c)

    def card(self):
        self.s.card()

    def disposeDrink(self, id: int):
        self.s.disposeDrink(id)

    def additive(self, type: int):
        self.s.additive(type)

    def cancel(self):
        self.s.cancel()

    def changeState(self, s: int):
        # todo: delete
        tem_dic = {0: 'Start', 1: 'NoCups', 2: 'Idle', 3: 'CoinInserted'}
        print(f'change sate to {tem_dic[s]}')
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

    def __init__(self, m: MDA_EFSM, d: StateData,  op: OP) -> None:
        self.m = m
        self.d = d
        self.op = op

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

        if c == True:
            self.d.A = [0]*10
            self.m.changeState(3)

    def card(self):
        self.op.ZeroCF()
        self.d.A = [0]*10
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

    def cancel(self):
        self.op.ReturnCoins()
        self.m.changeState(2)
