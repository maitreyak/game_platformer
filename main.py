import pygame

class Platform:
    def __init__(self,screen):
        self.screen = screen

    def start(self):

        #main event loop of the game
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN\
                   and event.key == pygame.K_ESCAPE:
                    return

if __name__ == '__main__':
    #init of pygame
    pygame.init()
    #set screen size
    screen = pygame.display.set_mode((640,480))
    platform = Platform(screen)
    platform.start()
