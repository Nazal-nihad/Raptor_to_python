import pygame
from random import randint
from sys import exit
# Initialize Pygame
pygame.init()

size = (600, 700)
line_width = 15
font = pygame.font.Font("freesansbold.ttf", 40)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tic Tac Toe")

# main board which is updated later according to conditions
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

# check empty space


def not_filled(row, col):
    if board[row][col] == 0:
        return True
    else:
        return False

# draw lines on the board


def draw_board():
    pygame.draw.line(screen, 'white', (0, 200), (600, 200), 3)
    pygame.draw.line(screen, 'white', (0, 400), (600, 400), 3)
    pygame.draw.line(screen, 'white', (200, 0), (200, 600), 3)
    pygame.draw.line(screen, 'white', (400, 0), (400, 600), 3)

# import x image and draw at position


def drawX(cell, x_pos=0, y_pos=0):
    x = pygame.image.load(
        'Lab_cycle_3/QN1/img/x.png').convert_alpha()
    x = pygame.transform.rotozoom(x, 0, 0.175)
    cell.blit(x, (x_pos, y_pos))

# import o img and draw


def drawO(cell, x_pos=0, y_pos=0):
    o = pygame.image.load(
        'Lab_cycle_3/QN1/img/o.png').convert_alpha()
    o = pygame.transform.rotozoom(o, 0, 0.3)
    cell.blit(o, (x_pos, y_pos))


def checkwin():
    for i in range(3):
        # horizontal condition
        if board[0][i] == board[1][i] == board[2][i] == player:
            pygame.draw.line(screen, 'white', (0, i*200+100),
                             (600, i*200+100), line_width)
            # print(player, "won")
            return True
        # vertical condition
        elif board[i][0] == board[i][1] == board[i][2] == player:
            pygame.draw.line(screen, 'white', (i*200+100, 0),
                             (i*200+100, 600), line_width)
            return True
    # diagonal condition
    if board[0][0] == board[1][1] == board[2][2] == player:
        pygame.draw.line(screen, 'white', (0, 0), (600, 600), line_width)
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        pygame.draw.line(screen, 'white', (600, 0), (0, 600), line_width)
        return True


# randomly choose first
player = randint(1, 2)
win_check = False


def check_tie():
    # check if the board is filled
    flag = 0
    for row in range(3):
        for col in range(3):
            if board[row][col] != 0:
                flag += 1
    if flag == 9:
        return True


def end_button():
    # restart button
    game_msg = font.render('Restart', False, 'black')
    game_msg = pygame.transform.rotozoom(game_msg, 0, 1.25)
    game_msg_rect = game_msg.get_rect(center=(300, 635))
    pygame.draw.rect(screen, 'white', (0, 600, 600, 100))
    screen.blit(game_msg, game_msg_rect)
    if not checkwin():
        if player == 1:
            player_msg = font.render('X turn', False, 'black')
        elif player == 2:
            player_msg = font.render('O turn', False, 'black')
    if check_tie():
        player_msg = font.render('TIE', False, 'blue')
    if checkwin():
        if player == 1:
            player_msg = font.render('X won', False, 'blue')
        elif player == 2:
            player_msg = font.render('O won', False, 'blue')
    player_msg_rect = player_msg.get_rect(midbottom=(300, 700))
    screen.blit(player_msg, player_msg_rect)


def restart():
    global board
    board = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
    win_check = False
    global player
    player = randint(1, 2)
    screen.fill('black')
    draw_board()


# game loop starts
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # find mouse click position change to single digit and divide to get simplified cooridnates
            x_point = event.pos[0]//100
            y_point = event.pos[1]//100
            m_row = x_point//2
            m_col = y_point//2
            # print(x_point, y_point)
            # print(m_row, m_col)
            if x_point > 5 or y_point > 5:
                restart()
                continue
            win_check = not checkwin()
            if win_check and not_filled(m_row, m_col):
                if player == 1:
                    drawX(screen, (m_row)*200, (m_col)*200)
                    board[m_row][m_col] = 1
                    if checkwin():
                        # checkwin()
                        win_check = False
                        # print("Player 1 won")
                    else:
                        player = 2
                elif player == 2:
                    drawO(screen, (m_row)*200+20, (m_col)*200+20)
                    board[m_row][m_col] = 2
                    if checkwin():
                        # checkwin()
                        win_check = False
                        # print("player 2 won")
                    else:
                        player = 1
                # print(board)

    draw_board()
    end_button()

    # Update the display
    pygame.display.update()
    clock.tick(60)
