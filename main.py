def start(): #Генерация верхушки
  print('|-------------------------------------|')
  print('|          Добро пожаловать в         |')
  print('|       Игре "Крестики - Нолики"      |')
  print('|-------------------------------------|')
  print('|       Формат ввода: x y             |')
  print('|       x - номер строки              |')
  print('|       y - номер столбца             |')
  print('|-------------------------------------|')

def table(): #Генерация таблицы
  print()
  print('   | 0 | 1 | 2 | ')
  print('----------------')
  for i, row in enumerate(field):
    row_str = f' {i} | {" | ".join(row)} | '
    print(row_str)
    print('----------------')
  print()

def ask(): #Ввод координат и проверка их
  while True:
    coords = input ('  Ваш ход: ').split()
    
    if len(coords) != 2:
      print("Введите 2 координаты!")
      continue
      
    x, y = coords
    if not(x.isdigit()) or not(y.isdigit()):
      print('  Введите числа!')
      continue
      
    x, y = int(x), int(y)
    if (0 > x) or (x > 2) or (0 > y) or (y > 2):
      print('  Числа вне диапозона!')
      continue

    if field[x][y] != " ":
      print(' Клетка занята!')
      continue
      
    return x, y

def check_win():
  win_coord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
              ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
              ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
  for coords in win_coord:
    symbols = []
    for c in coords:
      symbols.append(field[c[0]][c[1]])
    if symbols == ['X', 'X', 'X']:
      table()
      print('  Выиграл X!')
      return True
    if symbols == ['0', '0', '0']:
      table()
      print('  Выиграл 0!')
      return True
  return False

start() #Вывод верхушки
count = 0
field = [[" "] * 3 for i in range(3)]

while True:
  count+=1
  table()
  if count % 2 == 0: #Счётчик кто ходит
    print('   Ходит нолик')
  else:
    print('  Ходит крестик ')

  x, y = ask()
  
  if count % 2 == 0:
    field[x][y] = '0'
  else:
    field[x][y] = 'X'

  if check_win():
    break
  
  if count == 9: #Ничья
    print('\n      НИЧЬЯ')
    break