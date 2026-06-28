import sys
#import multiprocessing

def seq(n,m):
    i = 1
    s = ''
    while True:
        s += str(i)
        # print(i, end='')
        i = 1 + (i + m - 2) % n
        if i == 1:
            break
    return s

if len(sys.argv) > 1 and len(sys.argv)<=5:
   print(seq(int(sys.argv[1]),int(sys.argv[2]))+seq(int(sys.argv[3]),int(sys.argv[4])))
else:
    print('Ошибка!!! \nОтсутствуют обязательные параметры!\nОжидаю 4 параметра!')