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
import random

from components.numberbox import NumberBox

class Classic:
    def __init__(self, game):
        self.screen = game.screen
        self.gameStateManager = game.gameStateManager
        self.game = game

        self.bg = pygame.image.load("./assets/background.png")
        self.bg_rect = self.bg.get_rect(center = (self.screen.get_width()/2, self.screen.get_height()/2))
        
        self.target = random.randint(0, 99)
        print(self.target)
        self.generate_numbers()
    
    def generate_numbers(self):
        self.num_boxes = []
        for num in range(100):
            row = num // 10
            col = num % 10
            x = col * 64 + 32
            y = row * 26 + 13
            num_box = NumberBox(str(num), (x, y), self.target)
            self.num_boxes.append(num_box)
            if num == self.target:
                self.target_box = num_box
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for box in self.num_boxes:
                box.check_press()
    
    def render(self):
        self.screen.blit(self.bg, self.bg_rect)
        for box in self.num_boxes:
            box.draw(self.screen)
    
    def run(self):
        if self.target_box.filled:
            pass

        self.render()
        
