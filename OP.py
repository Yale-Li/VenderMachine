from DataStore import DataStore
from Strategies import SP, ZCF, ICF, RC, DD, DA
from Factory import AbstractFactory


"""
This file implements the Operation class.
"""


class OP:
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

        self.sp.ds = ds
        self.zcf.ds = ds
        self.icf.ds = ds
        self.rc.ds = ds

    def StorePrice(self):
        self.sp.StorePrice()

    def ZeroCF(self):
        self.zcf.ZeroCF()

    def IncreaseCF(self):
        self.icf.IncreaseCF()

    def ReturnCoins(self):
        self.rc.ReturnCoins()

    def DisposeDrink(self, id: int):
        self.dd.DisposeDrink(id)

    def DisposeAdditives(self, A: list):
        self.da.DisposeAdditives(A)
