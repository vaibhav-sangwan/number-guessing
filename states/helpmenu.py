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
from components.homebutton import HomeButton
from components.flippagebutton import FlipPageButton

font_s = pygame.font.Font("./fonts/m04b.ttf", 8)
classic_text = """\
----------------- Classic Mode ------------------

The computer has thought of a target number that you \
have to guess in minimum guesses possible. \
You can click on any number to see its distance from the target. \
The color of the number box signifies how close your guess \
is to the target number. \


Color Scheme
Red - Far away
Yellow - Getting closer
Green - In close proximity

Page 1 of 2
"""

rev_text = """\
------------------- Rev Mode -------------------

You have to think of a number lying between 0 and 99.\
Then the computer will show you a collection of numbers and \
you need to press on Yes or No depending on \
whether the number you thought of is present on the screen or not.

You will be shown 7 such collections and after providing appropriate \
answers each time, the number you thought of will be correctly guessed \
by the computer.

Page 2 of 2
"""

pages = [classic_text, rev_text]
DARK_GREY = "#145463"

class HelpMenu:
    def __init__(self, game):
        self.screen = game.screen
        self.gameStateManager = game.gameStateManager
        self.game = game

        self.bg = pygame.image.load("./assets/background.png")
        self.bg_rect = self.bg.get_rect(center=(
            self.screen.get_width() / 2, self.screen.get_height() / 2
        ))

        self.help_bg = pygame.image.load("./assets/help-menu-bg.png")
        self.help_bg = pygame.transform.scale_by(self.help_bg, 8)

        self.title = pygame.image.load("./assets/help-menu-title.png")
        self.title_rect = self.title.get_rect(center=(320, 80))

        self.home_button = HomeButton(510, 280, self.gameStateManager)
        self.flip_button = FlipPageButton(470, 280)

        self.reset()

    def reset(self):
        self.page = 0
        self.refresh_page()

    def refresh_page(self):
        self.curr_page = self.help_bg.copy()
        Utils.render_multiple_lines(
            pages[self.page], self.curr_page, 60, (60, 75), DARK_GREY, font_s
        )
        self.curr_page_rect = self.curr_page.get_rect(center=(
            self.screen.get_width() / 2, self.screen.get_height() / 2
        ))

    def render(self):
        self.screen.blit(self.bg, self.bg_rect)
        self.screen.blit(self.curr_page, self.curr_page_rect)
        self.screen.blit(self.title, self.title_rect)
        self.home_button.draw(self.screen)
        self.flip_button.draw(self.screen)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.home_button.check_press()
            if self.flip_button.check_press():
                self.page += 1
                if self.page >= len(pages):
                    self.page = 0
                self.refresh_page()

    def run(self):
        self.home_button.update()
        self.flip_button.update()
        self.render()
