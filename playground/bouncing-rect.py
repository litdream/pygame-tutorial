import pygame
import pycolor

def main():
    pygame.init()
    size = [700, 500]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Bouncing Rectangle")
    clock = pygame.time.Clock()
    done = False
    rectX, rectY = 50,50
    rect_Xdelta, rect_Ydelta = 2,2

    while not done:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                done = True

        rectX += rect_Xdelta
        rectY += rect_Ydelta

        if rectY > 450 or rectY < 0:
            rect_Ydelta = -rect_Ydelta
        if rectX > 650 or rectX < 0:
            rect_Xdelta = -rect_Xdelta

        screen.fill(pycolor.black)
        pygame.draw.rect(screen, pycolor.white, [rectX, rectY, 50,50])
        pygame.draw.rect(screen, pycolor.red, [rectX+10, rectY+10, 30,30])

        clock.tick(60)
        pygame.display.flip()
    pygame.quit()
                
if __name__ == '__main__':
    main()
