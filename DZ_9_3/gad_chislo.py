__all__=['get_random_num']

from random import randint as rnd
from sys import argv
#from math import sqrt as sq

#print (rnd(1, 100))
#x = [1, 2]
#print (size(x))
#print (sq(100))

" ugaday chisla"
__all__ = ['get_random_num']


START = 0

STOP = 100

AMAUND = 2

def get_random_num(start:int, end:int, amaund = AMAUND):
    num = rnd(start, end)
    flag =False
    while amaund > 0:
        num_user = int(input('vedite chislo'))
        if num_user==num:
            print('YES')
            flag = True
        elif num_user < num:
            print ('>')
            amaund -= 1
        else:
            print ('<')
            amaund -= 1
    return flag
if __name__ == '__main__':
    name,*param = argv
    print(get_random_num(*(int(elem) for elem in param)))
