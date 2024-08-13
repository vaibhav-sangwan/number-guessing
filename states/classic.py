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
from components.button import Button
from components.homebutton import HomeButton
from gettext import gettext as _

font_m = pygame.font.Font("./fonts/3Dventure.ttf", 16)
DARK_GREY = "#145463"


class Classic:
    def __init__(self, game):
        self.screen = game.screen
        self.gameStateManager = game.gameStateManager
        self.game = game

        self.bg = pygame.image.load("./assets/background.png")
        self.bg_rect = self.bg.get_rect(center=(
            self.screen.get_width() / 2, self.screen.get_height() / 2
        ))

        self.home_button = HomeButton(30, 330, self.gameStateManager)

        self.reset_button = Button(_("Reset"), (320, 330))
        self.reset()

    def reset(self):
        self.target = random.randint(0, 99)
        self.generate_numbers()
        self.layer = 4
        self.last_burst = pygame.time.get_ticks()
        self.incorrect = 0

    def generate_numbers(self):
        self.num_boxes = []
        for num in range(100):
            row = num // 10
            col = num % 10
            x = col * 64 + 32
            y = 40 + (row * 26) + 13
            num_box = NumberBox(str(num), (x, y), self.target)
            self.num_boxes.append(num_box)
            if num == self.target:
                self.target_box = num_box

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for box in self.num_boxes:
                if all([
                    not box.filled,
                    box.check_press(),
                    box.val != self.target
                ]):
                    self.incorrect += 1
            if self.reset_button.check_press():
                self.reset()
            self.home_button.check_press()

    def render(self):
        self.screen.blit(self.bg, self.bg_rect)
        for box in self.num_boxes:
            box.draw(self.screen)
        self.reset_button.draw(self.screen)
        self.home_button.draw(self.screen)

        inc_text = font_m.render(
            _("INCORRECT: ") + (str)(self.incorrect), False, DARK_GREY
        )
        inc_text_rect = inc_text.get_rect(center=(320, 20))
        self.screen.blit(inc_text, inc_text_rect)

    def run(self):
        if self.target_box.filled and self.layer >= 0:
            curr_tick = pygame.time.get_ticks()
            if curr_tick - self.last_burst >= 200:
                self.last_burst = curr_tick

                for i in range(100):
                    row = i // 10
                    col = i % 10
                    if any([
                        row == self.layer,
                        row == 9 - self.layer,
                        col == self.layer,
                        col == 9 - self.layer
                    ]):
                        self.num_boxes[i].fill()
                self.layer -= 1

        self.render()
