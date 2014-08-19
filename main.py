import pygame
import tmx

class Platform:
    
    def __init__(self,screen):
        self.screen = screen
        self.tilemap = None
        self.sprites = None
    
    def start(self):

        #init the game clock
        clock = pygame.time.Clock()
        
        #load the tile map
        self.tilemap = tmx.load('map.tmx',self.screen.get_size())
        self.sprites = tmx.SpriteLayer()
        
        self.tilemap.layers.append(self.sprites)

        #set view port
        self.tilemap.set_focus(640,480)
        
        
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
            
            self.tilemap.update(delta_t/1000.,self)
            self.tilemap.draw(self.screen)
            pygame.display.flip()
            

if __name__ == '__main__':
    #init of pygame
    pygame.init()
    #set screen size
    screen = pygame.display.set_mode((640,480))
    Platform(screen).start()
