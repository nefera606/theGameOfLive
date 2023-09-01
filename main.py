import os
import asyncio

rows = 60
cols = 180
fps = 1

def createCanon(x,y):
  return [[24,0],[22,1],[24,1],[12,2],[13,2],[20,2],[21,2],[34,2],[35,2],[11,3],[15,3],[20,3],[21,3],[34,3],[35,3],[0,4],[1,4],[10,4],[16,4],[20,4],[21,4],[0,5],[1,5],[10,5],[14,5],[16,5],[17,5],[22,5],[24,5],[10,6],[16,6],[24,6],[11,7],[15,7],[12,8],[13,8]]

initialElements = createCanon(3,3)

def clrscr():
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      _ = os.system('cls')

def getSurrounding(x,y,matrix):
  next_x = 0 if x == cols-1 else x + 1
  next_y = 0 if y == rows-1 else y + 1
  return [matrix[x-1][y-1],matrix[x-1][y],matrix[x-1][next_y],matrix[x][y-1],matrix[x][next_y],matrix[next_x][y-1],matrix[next_x][y],matrix[next_x][next_y]]

def checkLive(current,surroundings):
  sum = 0
  for i in surroundings:
    if (i):
      sum += 1;
  return True if sum == 3 or (current and sum == 2) else False;
  
def initAlive():
  result = [[0 for _ in range(rows)] for _ in range(cols)]
  for y in range(rows):
    for x in range(cols):
      result[x][y] = False;
  for i in initialElements:
    result[i[0]][i[1]] = True;
  return result;

def getAlive(matrix):
  result = [[0 for _ in range(rows)] for _ in range(cols)]
  for y in range(rows):
    for x in range(cols):
      result[x][y] = checkLive(matrix[x][y],getSurrounding(x,y,matrix))
  return result;

async def pantalla(screens):
  for sc in range (screens):
    if sc == 0:
      alive = initAlive();
    else:
      alive = getAlive(alive);
    sum = 0
    for y in range(rows):
      a = '';
      for x in range(cols):
        a += '#' if alive[x][y] else '*'
        sum = sum + 1 if alive[x][y] else sum
      print(f'{a}');
    print(f'Round: {sc}')
    print(f'Total Life forms: {sum}')
    await asyncio.sleep(0.05);
    clrscr();

asyncio.run(pantalla(1000))