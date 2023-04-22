import DataStore


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


class ConcreteFactory2(AbstractFactory):
    def __init__(self) -> None:
        pass

    def getDataStorage(self):
        return DataStore.DataStorage2()