from DataStore import DataStore

class SP:
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
        print('Return Coins: ', self.ds.cf)
        self.ds.cf = 0

class RC2(RC):
    def ReturnCoins(self):
        print('Return Coins: ', self.ds.cf)
        self.ds.cf = 0

class DD:
    ds: DataStore

    def DisposeDrink(self, id: int):
        pass

class DD1(DD):
    def DisposeDrink(self, id: int):
        print('Dispose Drink: ', id)

class DD2(DD): 
    def DisposeDrink(self, id: int):
        print('Dispose Drink: ', id)

class DA:
    ds: DataStore

    def DisposeAdditives(self, A: list):
        pass

class DA1(DA):
    def DisposeAdditives(self, A: list):
        print('Dispose Additives: ', A)

class DA2(DA):
    def DisposeAdditives(self, A: list):
        print('Dispose Additives: ', A)