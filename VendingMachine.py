from Factory import AbstractFactory, ConcreteFactory1, ConcreteFactory2
from DataStore import DataStorage1, DataStorage2
from States import MDA_EFSM
from OP import OP


"""
This file contains the two Vending Machines, VM1 and VM2.
"""


class VM1:
    ds: DataStorage1    # point to DataStore D1
    m: MDA_EFSM       # point to the MDA-EFSM
    af: AbstractFactory

    def __init__(self) -> None:
        af = ConcreteFactory1()
        self.ds = af.getDataStorage()
        op = OP(af, self.ds)
        self.m = MDA_EFSM(op)

    def create(self, p: int):
        self.ds.temp_p = p
        self.m.create()

    def coin(self, v: float):
        self.ds.temp_v = v
        if v + self.ds.cf >= self.ds.price:
            self.m.coin(True)
        else:
            self.m.coin(False)

    def sugar(self):
        self.m.additive(0)

    def latte(self):
        self.m.disposeDrink(1)

    def tea(self):
        self.m.disposeDrink(2)

    def insert_cups(self, n: int):
        self.m.insertCups(n)

    def set_price(self, p: float):
        self.ds.temp_p = p
        self.m.setPrice()

    def cancel(self):
        self.m.cancel()


class VM2:
    ds: DataStorage2            # point to DataStore D2
    m: MDA_EFSM                 # point to the MDA-EFSM
    af: AbstractFactory

    def __init__(self) -> None:
        af = ConcreteFactory2()
        self.ds = af.getDataStorage()
        op = OP(af, self.ds)
        self.m = MDA_EFSM(op)

    def CREATE(self, p: float):
        self.ds.temp_p = p
        self.m.create()

    def COIN(self, v: int):
        self.ds.temp_v = v
        if v + self.ds.cf >= self.ds.price:
            self.m.coin(True)
        else:
            self.m.coin(False)

    def CARD(self, x: int):
        if x > self.ds.price:
            self.m.card()

    def SUGAR(self):
        self.m.additive(0)

    def CREAM(self):
        self.m.additive(1)

    def COFFEE(self):
        self.m.disposeDrink(0)

    def InsertCups(self, n: int):
        self.m.insertCups(n)

    def SetPrice(self, p: int):
        self.ds.temp_p = float(p)
        self.m.setPrice()

    def CANCEL(self):
        self.m.cancel()
