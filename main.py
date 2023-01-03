import pygame, sys
import random
import time
import pygame as pg
import sqlite3

mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
WIDTH = 800
HEIGHT = 600
black=(0,0,0)
gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))#setting game display size
pygame.display.set_caption('Keyboard Jump Game')
font = pygame.font.Font('comic.ttf', 40)
font_name = pygame.font.match_font('comic.ttf')

word_speed = 0.5

def Easy_word():
    global displayword, yourword, x_cor, y_cor, text, word_speed
    x_cor = random.randint(300,700)     #randomly choose x-cor between 300-700
    y_cor = 100  #y-cor
    word_speed += 0.10
    yourword = ''
    words = open("Easy_words.txt").read().split(', ')
    displayword = random.choice(words)
    l= [x_cor,y_cor,word_speed,yourword,displayword]
    return l

def Hard_word():
    global displayword, yourword, x_cor, y_cor, text, word_speed
    x_cor = random.randint(300,700)     #randomly choose x-cor between 300-700
    y_cor = 100  #y-cor
    word_speed += 0.10
    yourword = ''
    words = open("Hard_words.txt").read().split(', ')
    displayword = random.choice(words)
    l= [x_cor,y_cor,word_speed,yourword,displayword]
    return l

def draw_text(display, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, black)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    gameDisplay.blit(text_surface, text_rect)

def draw_text_score(display, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, (255,255,255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    gameDisplay.blit(text_surface, text_rect)


def main_screen():
    
    click = False
    while True:
        global word_speed
        word_speed=0.5
        background = pygame.image.load('WallpaperDog-5564532.jpg')
        background_main = pygame.transform.scale(background, (WIDTH, HEIGHT))  #scale image
        gameDisplay.blit(background_main, (0,0)) 
        
        draw_text(gameDisplay, "Please Select an Option!", 54, WIDTH / 2, 500)
    
        mx, my = pygame.mouse.get_pos()
    
        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)
        button_3 = pygame.Rect(50, 300, 200, 50)

        draw_text(gameDisplay, "KeyBoard", 54, 500, 120)
        draw_text_score(gameDisplay, "Jump", 54, 500, 200)
        draw_text(gameDisplay, "Game", 54, 500, 280)

        if button_1.collidepoint((mx, my)):
            if click:
                Easy_Mode()
        if button_2.collidepoint((mx, my)):
            if click:
                Hard_Mode()
        if button_3.collidepoint((mx, my)):
            if click:
                Highscore(background_main)
        pygame.draw.rect(gameDisplay, (255, 0, 0), button_1)
        pygame.draw.rect(gameDisplay, (255, 0, 0), button_2)
        pygame.draw.rect(gameDisplay, (255, 0, 0), button_3)
        draw_text(gameDisplay, "Easy Mode", 40, 150, 115)
        draw_text(gameDisplay, "Hard Mode", 40, 150, 215)
        draw_text(gameDisplay, "High Scores", 40, 150, 315)
        
    
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
    
        pygame.display.update()
        mainClock.tick(60)


def Easy_Mode():
    mode="Easy"
    l=Easy_word()
    score = 0
    game_over=4
    while True:
        if game_over==4:
        # if game_over>0:
            game_over -= 1

        
        background = pygame.image.load('1873.jpg')
        background = pygame.transform.scale(background, (WIDTH, HEIGHT))
        character = pygame.image.load('Char1.jpg')
        character = pygame.transform.scale(character, (50,50))
        wood = pygame.image.load('plank.png')
        wood = pygame.transform.scale(wood, (90,50))


        gameDisplay.blit(background, (0,0))

        l[1] += l[2]
        gameDisplay.blit(wood,(l[0]-50,l[1]+15))
        gameDisplay.blit(character,(l[0]-100,l[1]))
        draw_text(gameDisplay, str(l[4]), 40, l[0], l[1])
        draw_text(gameDisplay, 'Score : '+str(score) + '  Lives : ' + str(game_over), 40, WIDTH/2 , 5)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                l[3] += pygame.key.name(event.key)

                if l[4].startswith(l[3]):
                    if l[4] == l[3]:
                        score += len(l[4])
                        l=Easy_word()
                elif game_over>0 :
                    game_over-=1
                    l=Easy_word()
                    Other_screen(game_over,score,background,mode)
                    # yourword=''
                elif game_over==0:
                    Other_screen(game_over,score,background,mode)
                    time.sleep(2)
                    pygame.quit()
                    
        if l[1] < HEIGHT-5:
            pygame.display.update()
        else:
            game_over-=1
            Easy_word()
            Other_screen(game_over,score,background,mode)

def Hard_Mode():
    mode="Hard"
    l=Hard_word()
    score = 0
    game_over=4
    while True:
        if game_over==4:
        # if game_over>0:
            game_over -= 1

        
        background = pygame.image.load('1873.jpg')
        background = pygame.transform.scale(background, (WIDTH, HEIGHT))
        character = pygame.image.load('Char1.jpg')
        character = pygame.transform.scale(character, (50,50))
        wood = pygame.image.load('plank.png')
        wood = pygame.transform.scale(wood, (90,50))


        gameDisplay.blit(background, (0,0))

        l[1] += l[2]
        gameDisplay.blit(wood,(l[0]-50,l[1]+15))
        gameDisplay.blit(character,(l[0]-100,l[1]))
        draw_text(gameDisplay, str(l[4]), 40, l[0], l[1])
        draw_text(gameDisplay, 'Score : '+str(score) + '  Lives : ' + str(game_over), 40, WIDTH/2 , 5)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                l[3] += pygame.key.name(event.key)

                if l[4].startswith(l[3]):
                    if l[4] == l[3]:
                        score += len(l[4])
                        l=Hard_word()
                elif game_over>0 :
                    game_over-=1
                    l=Hard_word()
                    Other_screen(game_over,score,background,mode)
                    # yourword=''
                elif game_over==0:
                    Other_screen(game_over,score,background,mode)
                    time.sleep(2)
                    pygame.quit()
                    
        if l[1] < HEIGHT-5:
            pygame.display.update()
        else:
            game_over-=1
            Hard_word()
            Other_screen(game_over,score,background,mode)
    
def Other_screen(game_over,score,background,mode):
    gameDisplay.blit(background, (0,0))
    if game_over==0 :
        draw_text(gameDisplay, "GAME OVER!", 90, WIDTH / 2, HEIGHT / 4)
        draw_text(gameDisplay,"Final Score : " + str(score), 70, WIDTH / 2, HEIGHT /2)

    elif game_over==4:
        # greenButton=button( (0, 255, 0), 150, 225, 250, 100, 'click Me :)')
        draw_text(gameDisplay, "Press a key to begin!", 54, WIDTH / 2, 500)
    else:
        draw_text(gameDisplay, 'Retry with' + '  Lives : ' + str(game_over), 90, WIDTH / 2, HEIGHT / 4)
        draw_text(gameDisplay,"Score : " + str(score), 70, WIDTH / 2, HEIGHT /2)
        draw_text(gameDisplay, "Press a key to begin!", 54, WIDTH / 2, 500)
    waiting = True
    
    pygame.display.update()
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN :
                waiting = False
            if event.type == pygame.KEYDOWN and game_over==0:
                input_screen(score,mode)
                pygame.quit()

def input_screen(score,mode):
    # screen = pg.display.set_mode((640, 480))
    font = pg.font.Font(None, 32)
    clock = pg.time.Clock()
    input_box = pg.Rect(100, 100, 140, 32)
    color_inactive = pg.Color('lightskyblue3')
    color_active = pg.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pg.KEYDOWN:
                if active:
                    if event.key == pg.K_RETURN:
                        database(text,score,mode)
                    elif event.key == pg.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        gameDisplay.fill((30, 30, 30))
        draw_text_score(gameDisplay, 'Please Enter your Name', 60, (WIDTH/2)-20, 300)
        draw_text_score(gameDisplay, 'Press Enter after filling Name', 40, 520, 110)
        draw_text_score(gameDisplay, 'by clicking on Textbox', 60, (WIDTH/2)-20, 370)
        draw_text_score(gameDisplay, 'Your Score is : '+str(score), 60, (WIDTH/2)-20, 500)

        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        gameDisplay.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pg.draw.rect(gameDisplay, color, input_box, 2)

        pg.display.update()
        clock.tick(30)

def database(text,score,mode):
    print(text, score)
    conn = sqlite3.connect('highscore.db')
    #conn = sqlite3.connect(':memory:')
    #create a cursor
    c= conn.cursor()
    if mode=="Easy":
        c.execute("INSERT INTO easy_score VALUES(?,?)",(text,int(score)))
    if mode=="Hard":
        c.execute("INSERT INTO hard_score VALUES(?,?)",(text,int(score)))
    conn.commit()
    conn.close()
    main_screen()

def Highscore(background):
    gameDisplay.blit(background, (0,0))

    conn = sqlite3.connect('highscore.db')
    #conn = sqlite3.connect(':memory:')

    #create a cursor
    c= conn.cursor()
# c.execute("SELECT rowid, * from customers")
    c.execute("SELECT rowid, * FROM easy_score ORDER BY score DESC LIMIT 5")
    items = c.fetchall()
    y=130
    draw_text(gameDisplay, 'High Scores', 60, (WIDTH/2)-20, 15)
    draw_text(gameDisplay, 'Easy Mode Scores', 50, 220 , 70)
    draw_text(gameDisplay, 'Hard Mode Scores', 50 ,630, 70)
    draw_text(gameDisplay, "Press Esc for Main Menu!", 54, WIDTH / 2, 500)


    for item in items:
        draw_text(gameDisplay, item[1]+ " ------> "+ str(item[2]), 40, 200, y)
        y+=40
    
    d=conn.cursor()
    d.execute("SELECT rowid, * FROM hard_score ORDER BY score DESC LIMIT 5")
    hard_items = d.fetchall()
    y=130

    for item in hard_items:
        draw_text(gameDisplay, item[1]+ " ------> "+ str(item[2]), 40, 600, y)
        y+=40
    conn.commit()
    conn.close()
    run= True
    while run:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main_screen()

main_screen()

