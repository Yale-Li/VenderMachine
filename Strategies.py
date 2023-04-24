from DataStore import DataStore
"""
This file contains the strategies for the operations.
"""


class SP:
    """
    This class is the strategy for StorePrice.
    """
    ds: DataStore

    def StorePrice(self):
        pass

class SP1(SP):
    def StorePrice(self):
        self.ds.price = self.ds.temp_p

class SP2(SP):
    def StorePrice(self):
        self.ds.price = self.ds.temp_p


class ZCF:
    """
    This class is the strategy for reset .
    """
    ds: DataStore

    def ZeroCF(self):
        pass

class ZCF1(ZCF):
    def ZeroCF(self):
        self.ds.cf = 0

class ZCF2(ZCF):
    def ZeroCF(self):
        self.ds.cf = 0


class ICF:
    ds: DataStore

    def IncreaseCF(self):
        pass

class ICF1(ICF):
    def IncreaseCF(self):
        self.ds.cf += self.ds.temp_v

class ICF2(ICF):
    def IncreaseCF(self):
        self.ds.cf += self.ds.temp_v


class RC:
    ds: DataStore

    def ReturnCoins(self):
        pass

class RC1(RC):
    def ReturnCoins(self):
        if self.ds.temp_v > 0:
            self.ds.temp_v = 0
            print('Return Coins: ', self.ds.temp_v)
        else:
            self.ds.cf = 0
            print('Return Coins: ', self.ds.temp_v)
        

class RC2(RC):
    def ReturnCoins(self):
        if self.ds.temp_v > 0:
            self.ds.temp_v = 0
            print('Return Coins: ', self.ds.temp_v)
        else:
            self.ds.cf = 0
            print('Return Coins: ', self.ds.temp_v)


class DD:
    def DisposeDrink(self, id: int):
        pass

class DD1(DD):
    def DisposeDrink(self, id: int):
        print('Dispose Drink: ', id)

class DD2(DD): 
    def DisposeDrink(self, id: int):
        print('Dispose Drink: ', id)


class DA:
    def DisposeAdditives(self, A: list):
        pass

class DA1(DA):
    def DisposeAdditives(self, A: list):
        print('Dispose Additives: ', A)

class DA2(DA):
    def DisposeAdditives(self, A: list):
        print('Dispose Additives: ', A)