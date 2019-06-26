# -tc- tu auras avantage à représenter le labyrinthe
# -tc- plus simplement, par exemple avec une liste
# -tc- de position (ligne, colonne) représentant les
# -tc- positions des murs
# define the maze structure
maze = [
    "***P00G0*******",  # 0
    "*****00G*******",  # 1
    "*****000G00**0*",  # 2
    "**0******00G0**",  # 3
    "*0***0******0G*",  # 4
    "*****000**0**0*",  # 5
    "****0*0000*0G0*",  # 6
    "******0**0G0***",  # 7
    "****0G0G00*****",  # 8
    "0***0***0****0*",  # 9
    "***G0*******0**",  # 10
    "***00G00*******",  # 11
    "***0G0G0*0*****",  # 12
    "***00G00**00***",  # 13
    "**G000*********""\n"]  # 14


def welcome():
    print("\nPlease, use your keyboard to move into the maze:\n4 = left, 6 = right, 8 = up, 2 = down.\n\nAnd get the maximum G = gifts!\n")
    # -tc- c'est pareil que for ligne in maze. Enlever le len(maze)
    for i in maze[:len(maze)]:
        print(i)


welcome()


def display():
    # -tc- le nom i est mal choisi
    for i in maze:
        print(i)


# -tc- les chaines de caractère possède déjà une methode replace().
# -tc- cette ne sera toutefois pas utile si tu représentes maze de manière
# -tc- à te simplifier la vie.
def replace(row, i, char):
    """slice to enable characters substitution according to coordinates"""
    s = row[: i] + char + row[i + 1:]
    return s


hits = []   # point collector


def counter():
    # -tc- [list(row) for row in maze] éviter les compréhensions avec deux for
    matrix = [col for row in maze for col in row]
    hits.append(matrix.count(maze[y][x] == "G"))
    score = len(hits)
    print("SCORE =", score, "\n")
    if score == 15:
        print("CONGRATS, YOU WON!!!\n")
    if score != 15 and maze[y] == 14:
        print("Too bad, you didn't take enough gits! Try again ;-)")


# -tc- mettre le code ci-dessous dans une fonction

y = 0     # vertical start position
x = 3     # horizontal start position


while maze[y] != 14:
    a = input()
    # -tc- à partir de là, ça devient complexe et répétitif et la poo te permettra de
    # -tc- réduire à quelque lignes.
    if a == "4":    # left
        if maze[y][x - 1] == "G":
            maze[y] = replace(maze[y], x - 1, "P")
            maze[y] = replace(maze[y], x, "_")
            x = x - 1
            counter()
            x = x + 1
            display()
        if maze[y][x - 1] == "0" or "_" or "1":
            maze[y] = replace(maze[y], x - 1, "P")
            maze[y] = replace(maze[y], x, "_")
            x = x - 1
            display()
    if a == "6":    # right
        if maze[y][x + 1] == "G":
            maze[y] = replace(maze[y], x + 1, "P")
            maze[y] = replace(maze[y], x, "_")
            x = x + 1
            counter()
            x = x - 1
        if maze[y][x + 1] == "0" or "_" or "1":
            maze[y] = replace(maze[y], x + 1, "P")
            maze[y] = replace(maze[y], x, "_")
            x = x + 1
            display()
    if a == "8":    # up
        if maze[y - 1][x] == "G":
            maze[y - 1] = replace(maze[y - 1], x, "P")
            maze[y] = replace(maze[y], x, "_")
            y = y - 1
            counter()
            y = y + 1
            display()
        if maze[y - 1][x] == "0" or "_" or "1":
            maze[y - 1] = replace(maze[y - 1], x, "P")
            maze[y] = replace(maze[y], x, "_")
            y = y - 1
            display()
    if a == "2":    # down
        if maze[y + 1][x] == "G":
            maze[y + 1] = replace(maze[y + 1], x, "P")
            maze[y] = replace(maze[y], x, "_")
            y = y + 1
            counter()
            y = y - 1
            display()
        if maze[y + 1][x] == "0" or "_" or "1":
            maze[y + 1] = replace(maze[y + 1], x, "P")
            maze[y] = replace(maze[y], x, "_")
            y = y + 1
            display()


# -tc- créer une fonction main() contenu le code de ton
# -tc- application
def main():
    welcome()
    # -tc- suite du code

