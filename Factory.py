import DataStore
import Strategies

class AbstractFactory:
    def __init__(self) -> None:
        pass

    def getDataStorage(self):
        pass

    def getSP(self):
        pass

    def getZCF(self):
        pass
    
    def getICF(self):
        pass

    def getRC(self):
        pass

    def getDD(self):
        pass

    def getDA(self):
        pass

class ConcreteFactory1(AbstractFactory):
    def __init__(self) -> None:
        pass

    def getDataStorage(self):
        return DataStore.DataStorage1()

    def getSP(self):
        return Strategies.SP1()
    
    def getZCF(self):
        return Strategies.ZCF1()

    def getICF(self):
        return Strategies.ICF1()
    
    def getRC(self):
        return Strategies.RC1()
    
    def getDD(self):
        return Strategies.DD1()
    
    def getDA(self):
        return Strategies.DA1()
    

class ConcreteFactory2(AbstractFactory):
    def __init__(self) -> None:
        pass

    def getDataStorage(self):
        return DataStore.DataStorage2()
    
    def getSP(self):
        return Strategies.SP2()
    
    def getZCF(self):
        return Strategies.ZCF2()
    
    def getICF(self):
        return Strategies.ICF2()
    
    def getRC(self):
        return Strategies.RC2()
    
    def getDD(self):
        return Strategies.DD2()
    
    def getDA(self):
        return Strategies.DA2()
