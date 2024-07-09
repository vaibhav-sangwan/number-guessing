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

import random
import pygame
from components.button import Button
from components.homebutton import HomeButton
from gettext import gettext as _

font_s = pygame.font.Font("./fonts/m04b.ttf", 8)

class CompGuess:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.gameStateManager = game.gameStateManager

        self.bg = pygame.image.load("./assets/background.png")
        self.bg_rect = self.bg.get_rect(center = (self.screen.get_width()/2, self.screen.get_height()/2))

        self.buttons = []
        self.yes_button = Button(_("Yes"), (235, 320))
        self.no_button = Button(_("No"), (320, 320))
        self.reset_button = Button(_("Reset"), (405, 320))
        self.buttons = [self.yes_button, self.no_button, self.reset_button]

        self.start_button = Button(_("Start"), (320, 200))
        self.home_button = HomeButton(30, 330, self.gameStateManager)
        self.reset()
    
    def reset(self):
        self.reqBit = 0
        self.res = 0
        self.target = random.randint(0, 1)
        nums = self.getNumbers(self.reqBit, self.target)
        self.cells = self.getCells(nums)
        self.started = False

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
            res[num] = (num % 10, num // 10)
        return res

    def render(self):
        self.screen.blit(self.bg, self.bg_rect)
        self.home_button.draw(self.screen)

        if not self.started:
            start_text = font_s.render(_("Think of a number between 0 to 99"), False, "#145463")
            start_text_rect = start_text.get_rect(center = (320, 160))

            self.screen.blit(start_text, start_text_rect)
            self.start_button.draw(self.screen)
            return

        if self.reqBit >= 7:
            if self.res < 100 and self.res >= 0:
                res_text = font_s.render(
                    _("You thought of ") + (str)(self.res), False, "#145463"
                )
            else:
                res_text = font_s.render(
                    _("The number you thought of does not lie in range 0-99"), False, "#145463"
                )
            res_rect = res_text.get_rect(center=(self.screen.get_width()/2, self.screen.get_height()/2))
            self.screen.blit(res_text, res_rect)

        else:
            for num in self.cells.keys():
                text = font_s.render((str)(num), False, "#145463")
                text_rect = text.get_rect(
                    center=(self.cells[num][0] * 64 + 32, self.cells[num][1] * 26 + 13)
                )
                self.screen.blit(text, text_rect)

        text = font_s.render("Is the number you thought of present on screen?", False, "#145463")
        text_rect = text.get_rect(center = (320, 290))
        if self.reqBit < 7:
            self.screen.blit(text, text_rect)

        for button in self.buttons:
            button.draw(self.screen)

    def input_received(self, present):
        val = 1 ^ (present ^ self.target)
        self.res = self.res | (val << self.reqBit)
        self.reqBit += 1
        self.target = random.randint(0, 1)
        nums = self.getNumbers(self.reqBit, self.target)
        self.cells = self.getCells(nums)


    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.started:
                if self.reset_button.check_press():
                    self.reset()
                elif (self.yes_button.check_press() and self.reqBit < 7):
                    self.input_received(1)
                elif (self.no_button.check_press() and self.reqBit < 7):
                    self.input_received(0)
            else:
                if self.start_button.check_press():
                    self.started = True
            self.home_button.check_press()

    def run(self):
        self.render()
