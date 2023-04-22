from DataStore import DataStore
from Strategies import SP, ZCF, ICF, RC, DD, DA
from Factory import AbstractFactory

class OP:
    ds: DataStore
    sp: SP
    zcf: ZCF
    icf: ICF
    rc: RC
    dd: DD
    da: DA

    def __init__(self, af: AbstractFactory, ds: DataStore) -> None:
        self.sp = af.getSP()
        self.zcf = af.getZCF()
        self.icf = af.getICF()
        self.rc = af.getRC()
        self.dd = af.getDD()
        self.da = af.getDA()
        
        self.ds = ds
        self.sp.ds = self.ds
        self.zcf.ds = self.ds
        self.icf.ds = self.ds
        self.rc.ds = self.ds
        self.dd.ds = self.ds
        self.da.ds = self.ds

    def StorePrice(self):
        self.sp.StorePrice()

    def ZeroCF(self):
        self.zcf.ZeroCF()

    def IncreaseCF(self):
        self.icf.IncreaseCF()

    def ReturnCoins(self):
        self.rc.ReturnCoins()

    def DisposeDrink(self, id: int):
        tem_dic = {0: 'coffe', 1: 'Latte', 2: 'Tea'}
        print('Here is your drink: ', tem_dic[id])
        self.dd.DisposeDrink(id)

    def DisposeAdditives(self, A: list):
        self.da.DisposeAdditives(A)

