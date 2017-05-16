import minesweeper as ms

game = ms.Game(20, 20, 0.2)

play = True

while play:
    game.print_board()
    x = int(input("X> "))
    y = int(input("Y> "))
    play = not game.move(x, y)
