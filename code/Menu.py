import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import COLOR_WHITE, WIN_WIDTH


class Menu:
    def __init__(self, in_window):
        self.window = in_window
        self.surf = pygame.image.load('./asset/Background-menu.png')
        self.rect = self.surf.get_rect(left=0, top=0)
    def run(self,):
        pygame.mixer_music.load('./asset/menu_music.mp3')
        pygame.mixer_music.play(-1) # (-1) para tocar em loop
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50,'Project', COLOR_WHITE,((WIN_WIDTH/2),70))
            self.menu_text(50,'Blaze and Freeze', COLOR_WHITE,((WIN_WIDTH/2),120))
            pygame.display.flip()
            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # end pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont('Arial',size=text_size)
        text_surf: Surface = text_font.render(text, True,text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)