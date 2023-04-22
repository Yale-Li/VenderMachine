
from DataStore import DataStorage1, DataStorage2
from MDA_EFSM import MDA_EFSM

class VM1:
    d: DataStorage1    # point to DataStore D1
    m: MDA_EFSM       # point to the MDA-EFSM

    def __init__(self) -> None:
        self.d = DataStorage1()
        self.m = MDA_EFSM()

    def create(self, p: int):
        self.d.temp_p = p
        self.m.create()

    def coin(self, v: float):
        self.d.temp_v = v 
        if v + self.d.cf >= self.d.price:
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
        self.d.temp_p = p
        self.m.setPrice()

    def cancel(self):
        self.m.cancel()


class VM2:
    d: DataStorage2            # point to DataStore D2
    m: MDA_EFSM       # point to the MDA-EFSM

    def __init__(self) -> None:
        self.d = DataStorage2()
        self.m = MDA_EFSM()

    def CREATE(self, p):
        self.d.temp_p = p
        self.m.create()

    def COIN(self, v):
        self.d.temp_v = v 
        if v + self.d.cf >= self.d.price:
            self.m.coin(True)
        else:
            self.m.coin(False)

    def CARD(self, x):
        self.d.temp_v = x
        if x > self.d.price:
            self.m.coin(True)

    def SUGAR(self):
        self.m.additive(0)

    def CREAM(self):
        self.m.additive(1)

    def COFFEE(self):
        self.m.additive(1)

    def InsertCups(self, n):
        self.m.insertCups(n)

    def SetPrice(self, p):
        self.d.temp_p = p
        self.m.setPrice()

    def CANCEL(self):
        self.m.cancel()
