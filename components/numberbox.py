#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Number Guessing
# Copyright (C) 2024 Vaibhav Sangwan
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Contact information:
# Vaibhav Sangwan    sangwanvaibhav02@gmail.com

import pygame

from utils import Utils
from components.particles import Particles

pygame.font.init()
font_m = pygame.font.Font("./fonts/m04b.ttf", 8)
far_color = (255, 0, 0)
med_color = (255, 255, 0)
close_color = (0, 150, 0)


class NumberBox:
    def __init__(self, text, coord, target):
        self.rect = pygame.Rect(0, 0, 34, 14)
        self.rect.center = coord

        self.hover_rect = pygame.Rect(0, 0, 42, 20)
        self.hover_rect.center = coord
        self.hover_color = "#145463"

        self.unfilled_text = font_m.render(text, False, "#145463")
        self.filled_text = font_m.render(text, False, "white")
        self.text_rect = self.filled_text.get_rect(center=(self.rect.center))

        self.filled = False
        self.val = (int)(text)
        self.set_fill_color(target)
        
        self.particles = None
        self.target = target
    
    def set_fill_color(self, target):
        curr_dist = abs(self.val - target)
        max_dist = max(target - 0, 99 - target)
        if curr_dist <= max_dist / 5:
            primary = close_color
            secondary = med_color
            init_pos = 0
            final_pos = max_dist / 5
        else:
            primary = med_color
            secondary = far_color
            init_pos = max_dist / 5
            final_pos = max_dist

        self.fill_color = [
            self.interpolate(init_pos, final_pos, primary[i], secondary[i], curr_dist) for i in range(3)
        ]
    
    def interpolate(self, x1, x2, y1, y2, x):
        m = (y2 - y1)/(x2 - x1)
        y = m*(x-x1) + y1
        return y

    def fill(self):
        self.filled = True
        self.particles = Particles(self.fill_color, self.rect.center)

    def check_press(self):
        if self.rect.collidepoint(Utils.norm_cursor_pos()):
            if not self.filled:
                self.fill()
            return True
        return False

    def draw(self, screen):
        if not self.filled:
            pygame.draw.rect(screen, "#145463", self.rect, 1, 2)
            if self.rect.collidepoint(Utils.norm_cursor_pos()):
                pygame.draw.rect(screen, self.hover_color, self.hover_rect, 2, 4)
            screen.blit(self.unfilled_text, self.text_rect)
        else:
            pygame.draw.rect(screen, self.fill_color, self.rect, 0, 2)
            screen.blit(self.filled_text, self.text_rect)
            if not self.particles.done_emitting():
                self.particles.emit(screen)
            if self.val == self.target:
                pygame.draw.rect(screen, "white", self.hover_rect, 2, 4)
