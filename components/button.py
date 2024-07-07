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

pygame.font.init()
font_m = pygame.font.Font("./fonts/3Dventure.ttf", 16)

import random


class Button:
    def __init__(self, text, coord):
        self.rect = pygame.Rect(0, 0, 70, 30)
        self.rect.center = coord
        self.hover_rect = pygame.Rect(0, 0, 76, 36)
        self.hover_rect.center = coord
        self.hover_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        self.text = font_m.render(text, False, "#145463")
        self.text_rect = self.text.get_rect(center=(self.rect.center))

    def check_press(self):
        if self.rect.collidepoint(Utils.norm_cursor_pos()):
            return True
        return False

    def draw(self, screen):
        pygame.draw.rect(screen, "#145463", self.rect, 1, 5)
        if self.rect.collidepoint(Utils.norm_cursor_pos()):
            pygame.draw.rect(screen, self.hover_color, self.hover_rect, 2, 7)
        else:
            self.hover_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        screen.blit(self.text, self.text_rect)
