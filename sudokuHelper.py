from copy import deepcopy

ordinance = {
  1: "1st",
  2: "2nd",
  3: "3rd",
  4: "4th",
  5: "5th",
  6: "6th",
  7: "7th",
  8: "8th",
  9: "9th"
}

sudokuRaw = []
for time in ordinance.values():
  sudokuRaw.append(
    input(f"Enter {time} row of Sudoku (no gaps between numbers!):"))

sudoku = []

for i in sudokuRaw:
  sudoku.append([])
  for j in i:
    sudoku[-1].append(j)

# For testing purposes
# Coopzeitung Nr. 20
# sudoku = [[' ', '7', '3', '1', '4', '9', ' ', ' ', '2'], [' ', '4', '9', '8', ' ', '6', '1', ' ', '3'], [' ', '8', '1', '5', ' ', '3', ' ', '7', '9'], ['1', '2', '6', '9', '5', '4', '7', '3', '8'], ['3', '9', '4', '6', '8', '7', '5', '2', '1'], ['8', '5', '7', '2', '3', '1', '9', '6', '4'], ['7', '1', '8', '4', '6', '2', '3', '9', '5'], ['9', '6', '5', '3', '1', '8', '2', '4', '7'], ['4', '3', '2', '7', '9', '5', '8', '1', '6']]
# SU-DOKU MEGASTAR Fortgeschritten Nr. 15 S. 11
# sudoku = [['2', '4', '6', '7', '3', '1', '5', '9', '8'], ['3', '5', '7', '6', '8', '9', '1', '2', '4'], ['8', '9', '1', '4', ' ', ' ', '3', '7', '6'], ['6', ' ', ' ', '1', '7', '4', '9', '3', '5'], ['7', '3', ' ', '2', ' ', '6', '4', '8', '1'], [' ', '1', '4', '3', ' ', '8', '7', '6', '2'], ['1', '2', '3', '8', ' ', '7', ' ', '5', '9'], ['9', '6', '8', '5', '1', ' ', ' ', '4', '7'], [' ', '7', ' ', '9', ' ', ' ', ' ', '1', '3']]
# SU-DOKU MEGASTAR Fortgeschritten Nr. 15 S. 12
# sudoku = [['2', ' ', '4', ' ', '7', '9', ' ', '3', ' '], ['5', '3', ' ', '8', ' ', '2', ' ', '7', '9'], [' ', '7', ' ', ' ', '5', '3', ' ', '2', ' '], [' ', ' ', '7', '5', '3', '6', '8', '1', '2'], [' ', '2', ' ', '7', '1', '4', ' ', '9', ' '], ['1', '5', '3', '9', '2', '8', '7', '6', '4'], [' ', ' ', ' ', ' ', ' ', '7', '9', '5', '1'], ['7', ' ', '5', '2', ' ', '1', ' ', '4', ' '], ['3', ' ', ' ', ' ', '9', '5', '2', '8', '7']]
# Coopzeitung Rätzelbeilage Nr.19 einfach
# sudoku = [['1', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '3'], ['4', ' ', '5', ' ', '8', ' ', '2', ' ', '7'], [' ', ' ', ' ', '3', '2', '5', ' ', ' ', ' '], ['9', ' ', '4', ' ', ' ', ' ', '3', ' ', '6'], [' ', '6', ' ', ' ', '4', ' ', ' ', '7', ' '], ['2', ' ', '1', ' ', ' ', ' ', '4', ' ', '5'], [' ', ' ', ' ', '9', '3', '1', ' ', ' ', ' '], ['5', ' ', '6', ' ', '7', ' ', '9', ' ', '8'], ['3', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '4']]
# Coopzeitung Rätzelbeilage Nr.19 einfach 2
# sudoku = [['1', ' ', ' ', '6', ' ', ' ', ' ', ' ', '5'], [' ', '4', '5', '9', ' ', ' ', '1', '6', ' '], [' ', '3', ' ', ' ', ' ', '5', ' ', '8', ' '], [' ', ' ', '3', ' ', '9', ' ', ' ', '2', '8'], [' ', ' ', ' ', '3', '6', '2', ' ', ' ', ' '], ['2', '1', ' ', ' ', '5', ' ', '4', ' ', ' '], [' ', '8', ' ', '1', ' ', ' ', ' ', '7', ' '], [' ', '9', '4', ' ', ' ', '7', '2', '5', ' '], ['3', ' ', ' ', ' ', ' ', '6', ' ', ' ', '9']]
# Coopzeitung Rätzelbeilage Nr.19 mittel
# sudoku = [['3', ' ', '7', ' ', '1', '4', '6', '8', ' '], ['8', ' ', '5', ' ', ' ', ' ', '1', '7', '4'], ['1', '4', '6', ' ', ' ', '8', ' ', '9', '5'], ['4', '5', '3', '2', '8', '9', '7', '1', '6'], ['7', '8', '1', ' ', '4', ' ', ' ', ' ', '9'], ['2', '6', '9', ' ', ' ', '1', '4', ' ', '8'], ['9', '7', '8', '1', ' ', ' ', ' ', '4', '3'], [' ', '3', '2', '4', '9', ' ', '8', ' ', '1'], [' ', '1', '4', '8', ' ', ' ', '9', ' ', ' ']]
# Sudoku von https://de.wikipedia.org/wiki/Sudoku
# sudoku = [[' ', '3', '4', '6', '7', '8', ' ', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'], [' ', ' ', '8', '3', '4', '2', ' ', '6', '7'], ['8', ' ', ' ', ' ', '6', '1', '4', ' ', '3'], ['4', ' ', '6', '8', '5', '3', '7', ' ', '1'], ['7', ' ', '3', ' ', '2', '4', '8', ' ', '6'], [' ', '6', ' ', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'], [' ', '4', ' ', '2', '8', '6', '1', '7', '9']]
# Sudoku mit nur 17 vordefinierten Feldern (auch von Wikipedia)
# sudoku = [['6', '9', ' ', ' ', '8', ' ', '5', '1', '2'], ['4', '8', ' ', '5', '1', '2', '9', ' ', '6'], ['1', '2', '5', '9', '6', ' ', '8', ' ', ' '], ['9', '3', '2', '6', '5', '1', '4', '8', '7'], ['5', '6', '8', ' ', '4', ' ', '3', '9', '1'], ['7', '4', '1', '3', '9', '8', '6', '2', '5'], ['3', '1', '9', '4', '7', '5', '2', '6', '8'], ['8', '5', '6', '1', '2', '9', '7', ' ', ' '], ['2', '7', '4', '8', '3', '6', '1', '5', '9']]
# Coopzeitung Nr.22
# sudoku = [[' ', '2', ' ', ' ', '7', '3', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', '1', '6'], [' ', '5', ' ', '1', ' ', ' ', '7', ' ', '2'], [' ', '4', '3', '9', ' ', ' ', '1', ' ', ' '], [' ', ' ', ' ', ' ', '6', ' ', ' ', ' ', ' '], [' ', ' ', '6', ' ', ' ', '1', '2', '5', ' '], ['5', ' ', '4', ' ', ' ', '2', ' ', '3', ' '], ['8', '9', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', '5', '9', ' ', ' ', '8', ' ']]

def printSudoku(sudoku):
  icount = 0
  print(" +-----------------+-----------------+-----------------+")
  for i in sudoku:
    icount += 1
    jcount = 0
    print(" | ", end="")
    for j in i:
      jcount += 1
      print(j.ljust(2).rjust(3).ljust(4).rjust(
        5) if j != " " else "  .  ", end="")
      if jcount >= 3:
        print(" | ", end="")
        jcount = 0
    print()
    if icount >= 3:
      print(" +-----------------+-----------------+-----------------+")
      icount = 0


print("Raw Sudoku:")
print(sudoku)

print("Before checking anything:")
printSudoku(sudoku)

# Checking presence of numbers in rows (horizontally)
def rowChecking(sudoku):
  for iIndex, i in enumerate(sudoku):
    rowPossibilities = ""
    for j in range(1, 10):
      if str(j) not in i:
        rowPossibilities += str(j)
    for jIndex, j in enumerate(i):
      if not j.isdigit() or len(j) != 1:
        sudoku[iIndex][jIndex] = rowPossibilities
  return sudoku

sudoku = rowChecking(sudoku)

print("After checking rows:")
printSudoku(sudoku)

# Checking presence of numbers in colums (vertically) (i and j are flipped compared to the rows section)
def colChecking(sudoku):
  sudokuCols = [list(col) for col in zip(*sudoku)]

  for iIndex, i in enumerate(sudokuCols):
    colPossibilities = ""
    for j in range(1, 10):
      if str(j) not in i:
        colPossibilities += str(j)
    for jIndex, j in enumerate(i):
      if not j.isdigit() or len(j) != 1:
        combined = ''.join(sorted(set(j) & set(colPossibilities)))
        sudokuCols[iIndex][jIndex] = combined

  sudoku = [list(col) for col in zip(*sudokuCols)]
  return sudoku

sudoku = colChecking(sudoku)

print("After checking columns:")
printSudoku(sudoku)

# Checking presence of numbers in boxes (3x3)
def boxID(i, j):
  ret = []
  for k in range(3):
    for l in range(3):
      ret.append([i*3+k, j*3+l])
  return ret

def inBox(number, box, sudoku):
  for field in box:
    if str(number) == sudoku[field[0]][field[1]]:
      return True
  return False

def boxChecking(sudoku):
  for i in range(3):
    for j in range(3):
      box = boxID(i, j)
      boxPossibilities = ""
      for k in range(1, 10):
        if not inBox(k, box, sudoku):
          boxPossibilities += str(k)
      for field in box:
        f = sudoku[field[0]][field[1]]
        if not f.isdigit() or len(f) != 1:
          combined = ''.join(sorted(set(f) & set(boxPossibilities)))
          sudoku[field[0]][field[1]] = combined
  return sudoku

sudoku = boxChecking(sudoku)

print("After checking boxes:")
printSudoku(sudoku)

progress = True
while progress:
  before = deepcopy(sudoku)
  sudoku = boxChecking(colChecking(rowChecking(sudoku)))
  progress = (sudoku != before)

print("After checking rows, columns and boxes again a few times:")
printSudoku(sudoku)

def hintRemover(sudoku):
  for iIndex, i in enumerate(sudoku):
    for jIndex, j in enumerate(i):
      if len(j) > 1:
        sudoku[iIndex][jIndex] = " "
  return sudoku

sudoku = hintRemover(sudoku)

print("Final sudoku:")
printSudoku(sudoku)

print("Raw final Sudoku:")
print(sudoku)
