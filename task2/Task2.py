import sys
def elipse(x,y,x0,y0,a,b):
    result = (x-x0)**2/a**2+(y-y0)**2/b**2
    if result == 1:
        s = '0'
    elif result < 1:
        s = '1'
    else:
        s = '2'
    print(s)
    # return result

print("Все аргументы:", sys.argv)

if len(sys.argv) ==1 or len(sys.argv)>3:
    print('Ошибка!!! \nОжидаю 2 параметра!')


mass = []
with open(sys.argv[1], "r") as file:
    for line in file:
        #mass = [int(x) for x in line.split()]
        mass.append(line)

x0 = int(mass[0][0])
y0 = int(mass[0][2])
a = int(mass[1][0])
b = int(mass[1][2])

with open(sys.argv[2], "r") as file:
    for line in file:
        if line != "\n":
            ar = [int(x) for x in line.split()]
            #print(2+int(line.split()))
            x = ar[0]
            y =ar[1]
            #y=int(line[2])
            #x = int(line.split())
            #y = int(line.split())
            elipse(x, y, x0, y0, a, b)