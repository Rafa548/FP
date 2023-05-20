# A set of functions to deal with bags of money.
#
# JMR 2017


# Face values of coins (in cents):
from binascii import b2a_base64


COINS = [200, 100, 50, 20, 10, 5, 2, 1]

def value(bag):
    x = 0
    for coin,number in bag.items():
        x += (coin*number)
    return x



def transfer1coin(bag1, c, bag2):
    if c in bag1 and bag1[c] != 0 :
        if c not in bag2.keys():
            bag2[c] = 1
        else:
            bag2[c] += 1
        bag1[c] -= 1
        return True
    else:
        return False


def transfer(bag1, amount, bag2):
    f = amount
    if amount == 0:
        return True
    if value(bag1) < amount:
        return False
    else:
        if value(bag2) != amount:
            x = 0
            for coin,number in bag1.items():
                if bag1[coin] > 0 and x != amount and coin <= f :
                    x += coin
                    bag1[coin] -= 1
                    f -= coin
                    print(bag1)
                    if bag1[coin] not in bag2:
                        bag2[coin] = 1
                        print(bag2)
                    if coin in bag2:
                        bag2[coin] += 1
        return True
        
            

def strbag(bag):
    x = ""
    h = 0
    f = (len(bag)-1)
    for coin,number in bag.items():
        x += str(coin)
        x += "x"
        x += str(number)
        if h != f:
            x += "+"
            h += 1
        else:
            x = x
    x += "="
    x += str(value(bag))
    return x


def main():
    # A bag of coins is represented by a dict of {coin: number} items
    bag1 = {1: 4, 2: 0, 5:1, 10: 0, 20: 5, 50: 4, 100: 2, 200: 1}
    bag2 = {}
    # Test the value function.
    assert value({}) == 0
    assert value({1:7, 5:2, 20:4, 100:1}) == 197

    # Test the strbag function.
    print( strbag({1:7, 5:2, 20:4, 100:1}) )        # 1x100+4x20+2x5+7x1=197
    print( strbag({1:7, 5:2, 10:0, 20:4, 100:1}) )  # 1x100+4x20+2x5+7x1=197

    print("bag1:", strbag(bag1))    # bag1: 1x200+2x100+4x50+5x20+1x5+4x1=709
    print("bag2:", strbag(bag2))    # bag2: =0
    
    print(transfer1coin(bag1, 10, bag2))    # False!
    print("bag1:", strbag(bag1))    # bag1: 1x200+2x100+4x50+5x20+1x5+4x1=709
    print("bag2:", strbag(bag2))    # bag2: =0

    print(transfer1coin(bag1, 20, bag2))    # True
    print("bag1:", strbag(bag1))    # bag1: 1x200+2x100+4x50+4x20+1x5+4x1=689
    print("bag2:", strbag(bag2))    # bag2: 1x20=20

    print(transfer1coin(bag1, 20, bag2))    # True
    print("bag1:", strbag(bag1))    # bag1: 1x200+2x100+4x50+3x20+1x5+4x1=669
    print("bag2:", strbag(bag2))    # bag2: 2x20=40

    print(transfer(bag1, 157, bag2))        # True (should be easy)
    print("bag1:", strbag(bag1))    # bag1: 1x200+1x100+3x50+3x20+2x1=512
    print("bag2:", strbag(bag2))    # bag2: 1x100+1x50+2x20+1x5+2x1=197

    print(transfer(bag1, 60, bag2)) # not easy, but possible...
    print("bag1:", strbag(bag1))
    print("bag2:", strbag(bag2))

    return

if __name__ == "__main__":
    main()

