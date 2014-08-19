import pygame



class Platform:
    def __init__(self,screen):
        self.screen = screen
    def start(self):

        #init the game clock
        clock = pygame.time.Clock()
        
        #main event loop of the game
        while True:
            
            #setting fps to 30 calls per second.
            delta_t = clock.tick(30)

            #loop thru the events and pick the right one.
            for event in pygame.event.get():
                #close button
                if event.type == pygame.QUIT:
                    return
                #esc key
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
