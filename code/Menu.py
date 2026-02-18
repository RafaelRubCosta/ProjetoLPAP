import pygame.image

class Menu:
    def __init__(self, in_window):
        self.window = in_window
        self.surf = pygame.image.load('')
        self.rect = self.surf.get_rect(left=0, top=0)
    def run(self,):
        self.window.blit(source=self.surf, dest=self.rect)
        pygame.display.flip()
        pass