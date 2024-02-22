import pygame

class Button:
    def __init__(self, text, coord):
        self.rect = pygame.Rect(0, 0, 50, 20)
        self.rect.center = coord

        self.font = pygame.font.Font(None, 18)
        self.text = self.font.render(text, False, "red")
        self.text_rect = self.text.get_rect(center = (self.rect.center))
    
    def check_clicked(self, pos):
        return self.rect.collidepoint(pos)
    
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 0), self.rect)
        screen.blit(self.text, self.text_rect)
        