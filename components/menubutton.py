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

font_m = pygame.font.Font("./fonts/3Dventure.ttf", 16)

class MenuButton(pygame.sprite.Sprite):
    def __init__(self, x, y, text, targetState):
        super().__init__()
        self.targetState = targetState
        self.image = pygame.image.load("./assets/button-bg.png")
        self.rect = self.image.get_rect(center = (x, y))
        img_txt = font_m.render(text, False, "#145463")
        img_txt_rect = img_txt.get_rect(center = (self.rect.width/2, self.rect.height/2))
        self.image.blit(img_txt, img_txt_rect)
        self.collide_rect = self.rect.copy()
    
    def check_press(self):
        if self.collide_rect.collidepoint(Utils.norm_cursor_pos()):
            return True
        return False
    
    def update(self):
        if self.collide_rect.collidepoint(Utils.norm_cursor_pos()):
            self.rect.centery = self.collide_rect.centery - 5
        else:
            self.rect.centery = self.collide_rect.centery
