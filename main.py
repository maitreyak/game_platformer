import pygame
import tmx
class Player(pygame.sprite.Sprite):
    def __init__(self, location, *groups):
        super(Player, self).__init__(*groups)
        self.image = pygame.image.load('images/redblock.png')
        self.rect = pygame.rect.Rect(location, self.image.get_size())
        self.resting = False
        self.dy = 0

    def update(self, dt, game):
        last = self.rect.copy()

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x -= 300 * dt
        if key[pygame.K_RIGHT]:
            self.rect.x += 300 * dt

        if self.resting and key[pygame.K_SPACE]:
            self.dy = -500
        self.dy = min(400, self.dy + 40)

        self.rect.y += self.dy * dt

        new = self.rect
        self.resting = False
        for cell in game.tilemap.layers['triggers'].collide(new, 'floor'):
            if last.right <= cell.left and new.right > cell.left:
                new.right = cell.left
            if last.left >= cell.right and new.left < cell.right:
                new.left = cell.right
            if last.bottom <= cell.top and new.bottom > cell.top:
                self.resting = True
                new.bottom = cell.top
                self.dy = 0
            if last.top >= cell.bottom and new.top < cell.bottom:
                new.top = cell.bottom
                self.dy = 0

        game.tilemap.set_focus(new.x, new.y)




##class Player(pygame.sprite.Sprite):
#    def __init__(self,location,*groups):
#        super(Player,self).__init__(*groups)
#        self.image = pygame.image.load('images/redblock.png')
#        self.rect = pygame.rect.Rect(location,self.image.get_size())
#        
#        self.resting = False
#        self.dy = 0
#
#        def update(self,dt,game):
#            last = self.rect.copy()
#            
#            key = pygame.key.get_pressed()
#            
#            if key[pygame.K_LEFT]:
#                self.rect.x +=300 *dt
#            if key[pygame.K_RIGHT]:
#                self.rect.x -=300 *dt
#            
#            if self.resting and key[K_SPACE]:
#                self.dy = -500
#
#            self.rect.y +=self.dy * dt
#
#            new = self.rect
#            self.resting = False
#
#            for cell in game.tilemap.layers['triggers'].collide(new,'floor'):
#
#                if last.right <= cell.left and new.right > cell.left:
#                    new.right = cell.left
#                if last.left >= cell.right and new.left < cell.right:
#                    new.left = cell.right
#                if last.bottom <= cell.top and new.bottom > cell.top:
#                    self.resting = True
#                    new.bottom = cell.top
#                    self.dy = 0
#                if last.top >= cell.bottom and new.top < cell.bottom:
#                    new.top = cell.bottom
#                    self.dy = 0
#
#            game.tilemap.set_focus(new.x, new.y)


class Platform(object):
    
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
        
        start_cell = self.tilemap.layers['triggers'].find('player')[0]
        self.player = Player((start_cell.px, start_cell.py), self.sprites)
        
        #set view port
        self.tilemap.set_focus(640,480)
        
        background = pygame.Surface(screen.get_size())
        background.fill((255, 255, 255))
        
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
             
            screen.blit(background,(0,0))
            self.tilemap.update(delta_t/1000.,self)
            self.tilemap.draw(self.screen)
            pygame.display.flip()
            

if __name__ == '__main__':
    #init of pygame
    pygame.init()
    #set screen size
    screen = pygame.display.set_mode((640,480))
    Platform(screen).start()
