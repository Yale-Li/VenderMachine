from MDA_EFSM import MDA_EFSM
from OP import OP

def vm1():
    print('         Vending Machine-1')
    print('     MENU of Operations')
    print('0. create(int)')
    print('1. coin(int)')
    print('2. sugar()')
    print('3. tea()')
    print('4. latte()')
    print('5. insert_cups(int)')
    print('6. set_price(float)')
    print('7. cancel()')
    print('q. Quit the demo program')
    print(' Please make a note of these operations')
    print('         Vending Machine-1 Execution')
    cmd =  input()



def vm2():
    print('         Vending Machine-2')
    print('     MENU of Operations')
    print('0. create(int)')
    print('1. coin(int)')
    print('2. sugar()')
    print('3. tea()')
    print('4. latte()')
    print('5. insert_cups(int)')
    print('6. set_price(float)')
    print('7. cancel()')
    print('q. Quit the demo program')
    print(' Please make a note of these operations')
    print('         Vending Machine-2 Execution')


if __name__ == '__main__':
    # vm1()

    m = MDA_EFSM(OP())
    m.create()
    m.insertCups(2)
    m.setPrice()
    m.coin(True)
    m.additive(0)
    m.additive(1)
    m.disposeDrink(1)
    m.coin(True)
    m.disposeDrink(1)
    m.cancel()
