import curses
from curses.ascii import ESC
from random import randint

#ask the user

print("\n\n welcome to Snake! To start playing, please set the mapsize")
sizex = input("\n\n What is the map sizex? : ")
sizex = int(sizex)
sizey = input("\n\n What is the map sizey? : ")
sizey = int(sizey)

#screen setup (window)

curses.initscr()

win = curses.newwin(sizey, sizex, 0, 0) #y, x (for some reason) and initialize the window
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1) #continues without a new keypress

#snake & food
snake = [(4, 10), (4, 9), (4, 8)] #storing the coordinates
food = (10, 20)

win.addch(food[0], food[1], '#')

#game logic
score = 0

ESC = 27
key = curses.KEY_RIGHT

while key != ESC:
    win.addstr(0, 2, 'Score ' + str(score) + ' ' + 'ESC')
    win.timeout(150 - (len(snake)) // 5 + len(snake)//10 % 120) #increase speed based on the lenght of the snake

    prev_key = key
    event = win.getch()
    key = event if event != -1 else prev_key

    if key not in [curses.KEY_LEFT, curses.KEY_DOWN, curses.KEY_UP, curses.KEY_RIGHT, ESC]:
        key = prev_key

    #caluclate the next coordinate

    y = snake[0][0]
    x = snake[0][1]

    if key == curses.KEY_DOWN:
        y += 1 
    if key == curses.KEY_UP:
        y -= 1 
    if key == curses.KEY_LEFT:
        x -= 1 
    if key == curses.KEY_RIGHT:
        x += 1 

    snake.insert(0, (y, x)) #append 0(n)

    #check if we hit the border
    if y == 0: break
    if y == sizey - 1: break
    if x == 0: break
    if x == sizex - 1: break

    #if snake runs over himself
    if snake[0] in snake[1:]: break #listslicing

    if snake[0] == food:
        #eat the food
        score += 1
        food = ()
        while food == ():
            food = (randint(1,18), randint(1, 58))
            if food in snake:
                food = ()
        win.addch(food[0], food[1], '#')
    else:
        #move snake 
        last = snake.pop()
        win.addch(last[0], last[1], ' ')

    win.addch(snake[0][0], snake[0][1], '*')

curses.endwin()
print(f'Final score = {score}')