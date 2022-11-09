import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Shooter")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)
background = pygame.image.load("background1.png.jpg")
play = pygame.font.SysFont("freesansbolt.ttf", 64)
textX = 340
textY = 250
spaceinvaders = pygame.font.SysFont("freesansbolt.ttf", 132)
spaceX = 220
spaceY = 150


def show_title(x, y):
    show_text = play.render("SPACE SHOOTER :)", True, (250, 0, 250))
    screen.blit(show_text, (x, y))


def show_play(x, y):
    play_text = play.render("PLAY", True, (250, 250, 250))
    screen.blit(play_text, (x, y))


running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            print("A keystroke is pressed")
            if event.key == pygame.K_KP_ENTER:
                import pygame
                import math
                import random
                from pygame import mixer

                # intialize the pygame
                pygame.init()

                # create the screen
                screen = pygame.display.set_mode((800, 600))  # width and height

                # background
                background = pygame.image.load("background.png.jpg")

                # background sound
                mixer.music.load('background.wav')
                mixer.music.play(-1)
                # caption and icon
                pygame.display.set_caption("Space shooter")
                icon = pygame.image.load("ufo.png")
                pygame.display.set_icon(icon)

                # player
                playerImg = pygame.image.load("spaceship.png")
                playerX = 370
                playerY = 480
                playerX_change = 0

                # Enemy
                enemyImg = []
                enemyX = []
                enemyY = []
                enemyX_change = []
                enemyY_change = []
                no_of_enemies = 6

                for i in range(no_of_enemies):
                    enemyImg.append(pygame.image.load("enemy.png"))
                    enemyX.append(random.randint(0, 768))
                    enemyY.append(random.randint(50, 150))
                    enemyX_change.append(0.5)
                    enemyY_change.append(20)

                # bullet
                # ready - bullet can't see in the screen
                # fire - bullet is currently moving in the screen

                bulletImg = pygame.image.load("bullet.png")
                bulletX =0
                bulletY = 480
                bulletX_change = 0.2
                bulletY_change = 1
                bullet_state = 'ready'



                # score
                score_value = 0
                font = pygame.font.SysFont("freesansbolt.ttf", 32)
                textX = 10
                textY = 10

                # game over text
                over_font = pygame.font.SysFont("freesansbolt.ttf", 64)





                def show_score(x, y):
                    score = font.render("SCORE :" + str(score_value), True, (250, 100, 255))
                    screen.blit(score, (x, y))


                def game_over_text():
                    over_text = over_font.render("GAME OVER ", True, (250, 100, 255))
                    screen.blit(over_text, (250, 250))


                def player(x, y):
                    screen.blit(playerImg, (x, y))


                def enemy(x, y, i):
                    screen.blit(enemyImg[i], (x + 16, y +10))


                def fire_bullet(x, y):
                    global bullet_state
                    bullet_state = 'fire'
                    screen.blit(bulletImg, (x, y))


                def iscollision(enemyX, enemyY, bulletX, bulletY):
                    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
                    if distance < 27:
                        return True
                    else:
                        return False


                # game loop
                running = True
                while running:

                    # RBG=red,blue,green (the value from 0 to 255)
                    screen.fill((0, 0, 0))
                    # background
                    screen.blit(background, (0, 0))
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False

                        # if keystroke is pressed check whether its right or left
                        if event.type == pygame.KEYDOWN:
                            print("A keystroke is pressed")
                            if event.key == pygame.K_LEFT:
                                playerX_change = -0.7
                                print("left arrow is pressed")
                            if event.key == pygame.K_RIGHT:
                                playerX_change = 0.7
                                print("right arrow is pressed")
                            if event.key == pygame.K_SPACE:
                                if bullet_state == "ready":
                                    bullet_sound = mixer.Sound('laser.wav')
                                    bullet_sound.play()
                                    # get the current coorinate of the spaceship
                                    bulletX = playerX
                                    fire_bullet(bulletX, bulletY)

                        if event.type == pygame.KEYUP:

                            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                                playerX_change = 0

                    # Checking for boundries of spaceship so it doesin't go out of bound
                    playerX += playerX_change

                    if playerX <= 0:
                        playerX = 0
                    elif playerX >= 768:
                        playerX = 768

                    # enemy movement
                    for i in range(no_of_enemies):

                        # game over
                        if enemyY[i] > 400:
                            for j in range(no_of_enemies):
                                enemyY[j] = 2000
                            game_over_text()



                            break

                        enemyX[i] += enemyX_change[i]

                        if enemyX[i] <= 0:
                            enemyX_change[i] = 0.5
                            enemyY[i] += enemyY_change[i]
                        elif enemyX[i] >= 768:
                            enemyX_change[i] = -0.5
                            enemyY[i] += enemyY_change[i]

                        # collision
                        collision = iscollision(enemyX[i], enemyY[i], bulletX, bulletY)
                        if collision:
                            explosion_sound = mixer.Sound('explosion.wav')
                            explosion_sound.play()
                            bulletY = 480
                            bullet_state = 'ready'
                            score_value += 1
                            enemyX[i] = random.randint(0, 768)
                            enemyY[i] = random.randint(50, 150)
                        enemy(enemyX[i], enemyY[i], i)

                    # bullet movement
                    if bulletY <= 0:
                        bulletY = 480
                        bullet_state = "ready"

                    if bullet_state == 'fire':
                        fire_bullet(bulletX, bulletY)
                        bulletY -= bulletY_change

                    player(playerX, playerY)
                    show_score(textX, textY)
                    pygame.display.update()

    show_title(spaceX, spaceY)
    show_play(textX, textY)
    pygame.display.update()

