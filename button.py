import pygame

pygame.font.init()
BUTTON_FONT = pygame.font.SysFont('ubuntumono', 18, bold=True)

class Button:
    def __init__(self, text, coord):
        self.rect = pygame.Rect(0, 0, 70, 30)
        self.rect.center = coord

        self.font = pygame.font.Font(None, 18)
        self.text = self.font.render(text, False, "red")
        self.text_rect = self.text.get_rect(center = (self.rect.center))
    
    def check_clicked(self, pos, screen):
        sw = screen.get_width()
        sh = screen.get_height()
        resized_rect = pygame.Rect(self.rect.left/800 * sw, self.rect.top/600 * sh, 70/800 * sw, 30/600 * sh)
        return resized_rect.collidepoint(pos)
    
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 0), self.rect)
        screen.blit(self.text, self.text_rect)
        