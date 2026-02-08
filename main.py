import pygame
# Aula Prática 01
print('Setup start')
pygame.init()
window = pygame.display.set_mode(size=(800, 600))
print('Setup end')

print('Loop start')
while True:
    # Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # Close Window
            quit() #end pygame