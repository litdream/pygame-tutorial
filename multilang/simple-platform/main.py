import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
clock = pygame.time.Clock()

# Colors
BLACK = (0,0,0)
WHITE = (255,255,255)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Platformer")

spritesheet = pygame.image.load("simple-platform/char_paper.png").convert_alpha()
sheet_width = 128
sheet_height = 128
def get_sprite_surface(x,y, width=sheet_width, height=sheet_height):
    _surface = pygame.Surface( (width,height), pygame.SRCALPHA)
    _surface.blit(spritesheet, (0, 0), (x, y, width, height))
    return _surface
    

class Platform(pygame.sprite.Sprite):
    def __init__(self, width, height, x:int, y:int):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Mario(pygame.sprite.Sprite):
    def __init__(self, x:int, y:int, platforms):
        super().__init__()
        self.platform_list = platforms
        
        # Setup animation frames
        self.walking_frames_l = []
        self.walking_frames_r = []
        for i in range(8):
            image = get_sprite_surface(i * 128, 0)
            self.walking_frames_r.append(image)
            image = pygame.transform.flip(image, True, False)
            self.walking_frames_l.append(image)
        _surf = get_sprite_surface(0, 9*128)
        self.jump_frame_l = _surf
        self.jump_frame_r = pygame.transform.flip(_surf, True, False)
        
        # Initialize character
        self.image = self.walking_frames_r[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.delta_y = 0
        self.delta_x = 6

        self.walk_speed = 6
        self.direction = "L"
        self.cur_frame = 0
        self.last_update = pygame.time.get_ticks()

    def update(self):
        self.calc_grav()

        self.rect.x += self.delta_x
        block_hit_list = pygame.sprite.spritecollide(self, self.platform_list, False)
        for block in block_hit_list:
            if self.delta_x > 0:
                self.rect.right = block.rect.left
            elif self.delta_x < 0:
                self.rect.left = block.rect.right

        self.rect.y += self.delta_y
        block_hit_list = pygame.sprite.spritecollide(self, self.platform_list, False)
        for block in block_hit_list:
            if self.delta_y > 0:
                self.rect.bottom = block.rect.top
            elif self.delta_y < 0:
                self.rect.top = block.rect.bottom
            self.delta_y = 0

        # Screen wrap
        if self.rect.right < 0:
            self.rect.left = SCREEN_WIDTH
        if self.rect.left > SCREEN_WIDTH:
            self.rect.right = 0
        if self.rect.bottom < 0:
            self.rect.top = SCREEN_HEIGHT
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.bottom = 0

        now = pygame.time.get_ticks()
        if self.delta_y != 0:
            if self.direction == "R":
                self.image = self.jump_frame_r
            else:
                self.image = self.jump_frame_l
        else:
            if self.delta_x != 0:
                if now - self.last_update > 100:
                    self.last_update = now
                    self.cur_frame = (self.cur_frame + 1) % len(self.walking_frames_l)
                    if self.direction == "R":
                        self.image = self.walking_frames_r[self.cur_frame]
                    else:
                        self.image = self.walking_frames_l[self.cur_frame]
            else:
                # Idle
                if self.direction == "R":
                    self.image = self.walking_frames_r[0]
                else:
                    self.image = self.walking_frames_l[0]
        

    def go_left(self):
        self.delta_x = -self.walk_speed
        self.direction = "L"

    def go_right(self):
        self.delta_x = self.walk_speed
        self.direction = "R"

    def stop(self):
        self.delta_x = 0

    def jump(self):
        # check if on the ground
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.platform_list, False)
        self.rect.y -= 2

        if len(platform_hit_list) > 0:
            self.delta_y = -10
    
        
    def calc_grav(self):
        if self.delta_y == 0:
            self.delta_y = 1
        else:
            self.delta_y += .35
            if self.delta_y > 30:   # terminal velocity
                self.delta_y = 30


def main():
    all_sprites = pygame.sprite.Group()
    
    # Create the ground
    platform_list = pygame.sprite.Group()
    ground1 = Platform(300, 40, 0, 500)
    platform_list.add( ground1)
    ground2 = Platform(300, 40, 500, 500)
    platform_list.add( ground2)

    # Mario
    player = Mario(100, 200, platform_list)
    all_sprites.add(ground1)
    all_sprites.add(ground2)
    all_sprites.add(player)
    
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q and (event.mod & pygame.KMOD_CTRL):
                    running = False
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_SPACE:
                    player.jump()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.delta_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.delta_x > 0:
                    player.stop()

        # Update
        all_sprites.update()
        
        # Draw
        screen.fill(BLACK)
        all_sprites.draw(screen)
        
        pygame.display.flip()  # flip the buffer
        clock.tick(60)
    

if __name__ == '__main__':
    main()
