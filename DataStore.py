
"""
DataStore of MDA-EFSM pattern, store the platform specific data

DS1 is for VM1, DS2 is for VM2
"""


class DataStore:
    """
    DataStore class, the abstract class of all data stores.
    """
    pass


class DataStorage1(DataStore):
    temp_p: int = 0
    temp_v: float = 0
    price: int = 0
    cf: float = 0


class DataStorage2(DataStore):
    temp_p: float = 0
    temp_v: int = 0
    price: float = 0
    cf: int = 0
