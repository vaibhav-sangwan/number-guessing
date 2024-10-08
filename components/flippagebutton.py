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
DARK_GREY = "#145463"


class FlipPageButton(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("./assets/page-flip-button.png")
        self.rect = self.image.get_rect(center=(x, y))

        self.hover_rect = pygame.Rect(0, 0, 36, 36)
        self.hover_rect.center = (x, y)

    def check_press(self):
        if self.rect.collidepoint(Utils.norm_cursor_pos()):
            return True
        return False

    def draw(self, screen):
        if self.rect.collidepoint(Utils.norm_cursor_pos()):
            pygame.draw.rect(screen, DARK_GREY, self.hover_rect, 2, 7)
        screen.blit(self.image, self.rect)
