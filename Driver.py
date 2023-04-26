from VendingMachine import VM1, VM2


"""
    Driver.py
"""


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
    cmd = ''
    vm1 = VM1()
    while cmd != 'q':
        print('0. create(int), 1. coin(int), 2. sugar(), 3. tea(), 4. latte(), 5. insert_cups(int), 6. set_price(float), 7. cancel()')
        cmd = input('Enter operation code: ')
        if cmd == '0':
            n = input('Enter number of price: ')
            vm1.create(int(n))
        elif cmd == '1':
            n = input('Enter number of coin: ')
            vm1.coin(float(n))
        elif cmd == '2':
            print('Operation: sugar()')
            vm1.sugar()
        elif cmd == '3':
            print('Operation: tea()')
            vm1.tea()
        elif cmd == '4':
            print('Operation: latte()')
            vm1.latte()
        elif cmd == '5':
            n = input('Enter number of cups: ')
            vm1.insert_cups(int(n))
        elif cmd == '6':
            p = input('Enter price: ')
            vm1.set_price(float(p))
        elif cmd == '7':
            print('Operation: cancel()')
            vm1.cancel()
        else:
            print('Invalid operation code')


def vm2():
    print('         Vending Machine-2 Execution')
    cmd = ''
    vm2 = VM2()
    while cmd != 'q':
        print('0. CREATE(float), 1. COIN(int), 2. CARD(int), 3. SUGAR(), 4. CREAM(), 5. COFFEE(int), 6. InsertCups(int), 7. SetPrice(), 8. CANCEL()')
        cmd = input('Enter operation code: ')
        if cmd == '0':
            p = input('Enter price: ')
            vm2.CREATE(float(p))
        elif cmd == '1':
            v = input('Enter value of coin: ')
            vm2.COIN(int(v))
        elif cmd == '2':
            x = input('Enter value of card: ')
            vm2.CARD(int(x))
        elif cmd == '3':
            print('Operation: SUGAR()')
            vm2.SUGAR()
        elif cmd == '4':
            print('Operation: CREAM()')
            vm2.CREAM()
        elif cmd == '5':
            print('Operation: COFFEE()')
            vm2.COFFEE()
        elif cmd == '6':
            n = input('Enter number of cups: ')
            vm2.InsertCups(int(n))
        elif cmd == '7':
            p = input('Enter price: ')
            vm2.SetPrice(float(p))
        elif cmd == '8':
            print('Operation: CANCEL()')
            vm2.CANCEL()
        else:
            print('Invalid operation code')
        


if __name__ == '__main__':
    vm1()
