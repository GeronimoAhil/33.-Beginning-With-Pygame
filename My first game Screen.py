import pygame

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = (500, 400)

display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(('Adding image and background image.'))


background_image = pygame.transform.scale(pygame.image.load('bg.jpeg').convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
sprite_image = pygame.transform.scale(pygame.image.load('Satoru Gojo.jpeg').convert(), (200, 200))
def game_loop():
    clock = pygame.time.Clock()
    running = True
    sprite_x = 150
    sprite_y = 100

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        
        display_surface.blit(background_image, (0, 0))
        
        display_surface.blit(sprite_image, (sprite_x, sprite_y))

        pygame.display.flip() 

if __name__ == '__main__':
    game_loop()

    pygame.quit()
