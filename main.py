import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from sugar3.graphics.style import GRID_CELL_SIZE

import pygame
import random

pygame.init()
GAME_FONT = pygame.font.Font(None, 18)
WIN_FONT = pygame.font.Font(None, 42)

class NumberGuessing:
    def __init__(self):
        pygame.display.init()
        pygame.display.set_caption('Number Guessing')
        self.clock = pygame.time.Clock()
        self.reqBit = 0
        self.res = 0
    
    def getNumbers(self, n, target):
        res = []
        for i in range(1, 100):
            bit = (i >> n) & 1
            if bit == target:
                res.append(i)
        return res

    def getCells(self, nums):
        res = {}
        for num in nums:
            res[num] = (num%10, num//10)
        return res

    def draw(self):
        self.screen.fill("white")
        
        if self.reqBit >= 7:
            res_text = WIN_FONT.render("Your guess was " + (str)(self.res), False, "black")
            res_rect = res_text.get_rect(center = (250, 250))
            self.screen.blit(res_text, res_rect)

        else:
            self.target = random.randint(0, 1)
            nums = self.getNumbers(self.reqBit, self.target)
            cells = self.getCells(nums)
            for num in cells.keys():
                text = GAME_FONT.render((str)(num), False, "black")
                text_rect = text.get_rect(center = (cells[num][0] * 50  + 25, cells[num][1] * 50 + 25))
                self.screen.blit(text, text_rect)

    def input_received(self, present):
        val = 1 ^ (present ^ self.target)
        self.res = self.res | (val << self.reqBit)
        self.reqBit += 1
        self.draw()

    def run(self):
        self.screen = pygame.display.get_surface()
        self.is_running = True
        self.draw()
        pygame.display.update()

        while self.is_running:
            while Gtk.events_pending():
               Gtk.main_iteration()

            self.py_events = pygame.event.get()
            for event in self.py_events:
                if event.type == pygame.QUIT:
                    self.is_running = False
                elif event.type == pygame.VIDEORESIZE:
                    self.screen = pygame.display.set_mode((event.size[0], event.size[1]),pygame.RESIZABLE)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.reqBit = 0
                        self.res = 0
                        self.draw()
                    elif event.key == pygame.K_y and self.reqBit < 7:
                        self.input_received(1)
                    elif event.key == pygame.K_n and self.reqBit < 7:
                        self.input_received(0)
            
            pygame.display.update()
            self.clock.tick(30)


if __name__ == "__main__":
    g = NumberGuessing()
    GAME_SIZE = (500, 500)
    g.screen = pygame.display.set_mode(GAME_SIZE, pygame.RESIZABLE)
    g.run()