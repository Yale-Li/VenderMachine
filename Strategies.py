from DataStore import DataStore


"""
This file Implements the strategy pattern.
"""


class SP:
    """
    This class is the strategy of StorePrice.
    Save the temporary price to the data store.
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
    This class is the strategy of ZeroCF.
    Reset the number of coins inserted to zero.
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
    """
    This class is the strategy of IncreaseCF.
    Increase the number of coins inserted by the amount of the current coin.
    """
    ds: DataStore

    def IncreaseCF(self):
        pass


class ICF1(ICF):
    def IncreaseCF(self):
        self.ds.cf += self.ds.temp_v
        self.ds.temp_v = 0


class ICF2(ICF):
    def IncreaseCF(self):
        self.ds.cf += self.ds.temp_v
        self.ds.temp_v = 0


class RC:
    """
    This class is the strategy of ReturnCoins.
    Return the coins inserted.
    """
    ds: DataStore

    def ReturnCoins(self):
        pass


class RC1(RC):
    def ReturnCoins(self):
        if self.ds.temp_v > 0:
            print('Return Coins: ', self.ds.temp_v)
            self.ds.temp_v = 0
        else:
            print('Return All Coins: ', self.ds.cf)
            self.ds.cf = 0


class RC2(RC):
    def ReturnCoins(self):
        if self.ds.temp_v > 0:
            print('Return Coins: ', self.ds.temp_v)
            self.ds.temp_v = 0
        else:
            print('Return All Coins: ', self.ds.cf)
            self.ds.cf = 0


class DD:
    """
    This class is the strategy of DisposeDrink.
    Dispose the drink.
    """

    def DisposeDrink(self, id: int):
        pass


class DD1(DD):
    def DisposeDrink(self, id: int):
        print('Dispose Drink: ', id)


class DD2(DD):
    def DisposeDrink(self, id: int):
        print('Dispose Drink: ', id)


class DA:
    """
    This class is the strategy of DisposeAdditives.
    Dispose the additives.
    """

    def DisposeAdditives(self, A: list):
        pass


class DA1(DA):
    def DisposeAdditives(self, A: list):
        print('Dispose Additives: ', A)


class DA2(DA):
    def DisposeAdditives(self, A: list):
        print('Dispose Additives: ', A)
