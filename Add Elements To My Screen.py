import pygame

pygame.init()

#SCREEN_WIDTH, SCREEN_HEIGHT = (500, 500)

display_surface = pygame.display.set_mode((500, 500))
White = (255, 255, 255)
Blue = (0, 0, 255)

rectangle_size = pygame.Rect(50, 100, 200, 150)
running = True
while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:                                                                                                                    
                running = False
        display_surface.fill(White)
        pygame.draw.rect(display_surface, Blue, pygame.Rect(50, 100, 200, 150))
        pygame.display.update()
pygame.quit()