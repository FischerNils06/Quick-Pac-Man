import pygame
import sys
import random
from pacman import Pacman
from ghosts import Ghost
from dot import Dot
from scoreboard import Scoreboard
from wall import Wall
from bonusdot import Bonusdot


# Initialisierung von Pygame
pygame.init()

# Bildschirmgröße festlegen
screen_width = 800
screen_height = 650
screen = pygame.display.set_mode((screen_width, screen_height))

# Titel des Fensters setzen
pygame.display.set_caption("Quick-Pac-Man")

# Farbe definieren
black = (0, 0, 0)
white = (255, 255, 255)

# Spielfigur erstellen
pacman = Pacman(375, 435)
ghost = Ghost("Red", 345, 295)
ghost2 = Ghost("Pink", 405, 295)
ghost3 = Ghost("Orange", 345, 355)
ghost4 = Ghost("Turquoise", 405, 355)
dot = Dot()
bonusdot = Bonusdot()
wall = Wall(330, 410, 140, 10, screen)
wall2 = Wall(330, 295, 10, 115, screen)
wall3 = Wall(460, 295, 10, 115, screen)
wall4 = Wall(300, 200, 260, 10, screen)
wall5 = Wall(390, 130, 185, 10, screen)
wall6 = Wall(700, 105, 10, 215, screen)
wall7 = Wall(735, 375, 10, 150, screen)
wall8 = Wall(745, 375, 55, 10, screen)
wall9 = Wall(0, 250, 190, 10, screen)
wall10 = Wall(0, 320, 180, 10, screen)
wall11 = Wall(275, 495, 250, 10, screen)
wall12 = Wall(275, 505, 10, 90, screen)
wall13 = Wall(515, 505, 10, 90, screen)
wall14 = Wall(100, 515, 95, 10, screen)
wall15 = Wall(90, 120, 115, 10, screen)
wall_list = [wall, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10, wall11, wall12, wall13, wall14, wall15]



scoreboard = Scoreboard()





def reset_game():
    global pacman, ghost, ghost2, ghost3, ghost4, dot, scoreboard, bonusdot, running
    pacman = Pacman(375, 435)
    ghost = Ghost("Red", 345, 295)
    ghost2 = Ghost("Pink", 405, 295)
    ghost3 = Ghost("Orange", 345, 355)
    ghost4 = Ghost("Turquoise", 405, 355)
    dot = Dot()
    bonusdot = Bonusdot()
    scoreboard = Scoreboard()
    running = True





# Hauptprogrammschleife
running = True
ghost_keys_pressed_time = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

   

    # Änderungen auf dem Bildschirm anzeigen
    pygame.display.flip()

    # move characters
    ghost.update()
    ghost2.update()
    ghost3.update()
    ghost4.update()
    ghost_list = [ghost, ghost2, ghost3, ghost4]
    current_time = pygame.time.get_ticks()
    if current_time - ghost_keys_pressed_time >= 250:
        ghost.keys()
        ghost2.keys()
        ghost3.keys()
        ghost4.keys()
        ghost_keys_pressed_time = current_time
    pacman.keys()
    pacman.update()
    pacman.update_costume()
   

    # Clear the screen
    screen.fill((0, 0, 0), pygame.Rect(0, 50, 800, 600))


    # draw characters
    bonusdot.draw(screen)
    dot.draw(screen)
    pacman.draw(screen)
    ghost4.draw(screen)
    ghost3.draw(screen)
    ghost2.draw(screen)
    ghost.draw(screen)
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(0,0,800,50))
    for wall_obj in wall_list:
        wall_obj.draw(screen)
    scoreboard.draw(screen)
    


    # if Space is pressed game restarts
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        reset_game()

    # pacman eats dot
    if (dot.x + 25 >= pacman.x >= dot.x - 50) and (dot.y + 25 >= pacman.y >= dot.y - 50):
        dot = Dot()
        scoreboard.add_score(1)
        sbsc = scoreboard.get_score()
        if sbsc % 10 == 0 and sbsc != 0:
            bonusdot.change_costume()
        ghost.change_speed()
        ghost2.change_speed()
        ghost3.change_speed()
        ghost4.change_speed()

            
    
    # pacman eats bonusdot
    if (bonusdot.x + 15 >= pacman.x >= bonusdot.x - 50) and (bonusdot.y + 15 >= pacman.y >= bonusdot.y - 50):
        sbsc = scoreboard.get_score()
        if sbsc != 0 and bonusdot.dot == "White":
            ghost.weak_ghost()
            ghost2.weak_ghost()
            ghost3.weak_ghost()
            ghost4.weak_ghost()
            bonusdot = Bonusdot()
        else:
            pass

    # pacman collides with ghost
    
    for ghost_obj in ghost_list:
        if (ghost_obj.x + 50 >= pacman.x >= ghost_obj.x - 50) and (ghost_obj.y + 50 >= pacman.y >= ghost_obj.y - 50):
            if ghost_obj.weak == False:
                reset_game()
            else:
                ghost_obj.go_back()

    # pacman collides with walls
    for wall_obj in wall_list:
        if (wall_obj.x + wall_obj.width >= pacman.x >= wall_obj.x - 50) and (wall_obj.y + wall_obj.height >= pacman.y >= wall_obj.y - 50):
            pacman.change_direction()
            


    # ghosts collide with walls
    for wall_obj in wall_list:
        for ghost_obj in ghost_list:
            if (wall_obj.x + wall_obj.width >= ghost_obj.x >= wall_obj.x - 50) and (wall_obj.y + wall_obj.height >= ghost_obj.y >= wall_obj.y - 50):
                ghost_obj.change_direction()
   

   





                    

   
    

# Pygame beenden
pygame.quit()
sys.exit()

