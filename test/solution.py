with open('input.txt', 'r') as INPUT:
    INPUT = INPUT.read()
    INPUT = INPUT.split()
    
#Класс корабли который будет создавать (ну или запоминать) кораблики, их расположение и так же запускать счетчик кораблей такого типа.
class Ship:
    def __init__(self, x, y):
        self.x = max(x, y)
        self.y = min(x, y)
        self.count = 1

    def __str__(self):
        return " ".join(map(str, [self.x, self.y, self.count]))

    def __lt__(self, other):
        return self.x > other.x or self.y > other.y

#Массив для обработки найденного корабля. Смотрим на длину и ширину через координаты, если есть такой корабль, то добавляем к счетчику 1, если нет, то добавляем новый корабль в словарь.
def get_ship(y, x):
    dy, dx = 1, 1
    while y + dy < n and field[y + dy][x]:
        dy += 1
    while x + dx < m and field[y][x + dx]:
        dx += 1
    new_ship = Ship(dx, dy)
    new_ship_key = tuple([new_ship.x, new_ship.y])
    if new_ship_key in ships.keys():
        ships[new_ship_key].count += 1
    else:
        ships[new_ship_key] = new_ship
    for i in range(y, y + dy):
        for j in range(x, x + dx):
            found[i][j] = True

#Создание поля где будут кораблики в виде двумерного массива.
n, m = map(int, input().split())
field = [   
    list(map(lambda x: True if x == "1" else False, list(input())))
    for i in range(n)
]

#Создание вспомогательного поля, с помощью которого будем искать корабли на поле ну и словаря где будем хранить кораблики и их число.
found = [[False for j in range(m)] for i in range(n)]
ships = dict()
for yi in range(n):
    for xi in range(m):
        if field[yi][xi] and not found[yi][xi]:
            get_ship(yi, xi)

f = open('output.txt', 'w')
for a in sorted(ships.keys()):
    f.write(str(ships[a]) + '\n')
