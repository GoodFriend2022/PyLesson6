import Task as t
import os

os.system('cls')
file = 'direct.txt'


while True:
    number = t.Menu()
    if not number in range(1, 8):
        os.system('cls')
        print('Такого номера в меню не представлено. Перезапустите программу и попробуйте еще раз.\n')
        break
    elif number == 1:
        t.PrintFile(file)
        
    











