import DataStore

class OP:
    d: DataStore

    def StorePrice(self):
        print('StorePrice')
        pass

    def ZeroCF(self):
        print('ZeroCF')
        pass

    def IncreaseCF(self):
        print('IncreaseCF')
        pass

    def ReturnCoins(self):
        print('ReturnCoins')
        pass

    def DisposeDrink(self, id: int):
        tem_dic = {0: 'coffe', 1: 'Latte', 2: 'Tea'}
        print('DisposeDrink: ', tem_dic[id])
        pass

    def DisposeAdditives(self, A: list):
        print('DisposeAdditives, additives: ', A)
        pass