# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
# Import der Spielkonstanten
from constants import *
# Clock object
clock = pygame.time.Clock()
# delta time variable
dt = 0

def main():
    pygame.init()
    # Bildschirmfläche wird festgelegt
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  
    #Game Loop beginnt hier
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # schwarzer Hintergrund    
        screen.fill((0,0,0), rect=None, special_flags=0)
        pygame.display.flip()
        # Warten für 1/60 Sekunde --> Limit auf 60FPS und Speichern der dt nach jedem Tick 
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()