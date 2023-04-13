"""
DataStore of MDA-EFSM, store the platform specific data

DS1 is for VM1, DS2 is for VM2
"""

class DataStore:
    additives: list

class DS1(DataStore):
    temp_p: int
    temp_v: float
    price: int
    cf: float

class DS2(DataStore):
    temp_p: float
    temp_v: int
    price: float
    cf: int