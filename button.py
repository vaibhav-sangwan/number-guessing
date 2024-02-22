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
        