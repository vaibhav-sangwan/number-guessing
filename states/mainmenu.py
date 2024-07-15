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

from components.menubutton import MenuButton


class MainMenu:
    def __init__(self, game):
        self.screen = game.screen
        self.gameStateManager = game.gameStateManager
        self.game = game

        self.bg = pygame.image.load("./assets/background.png")
        self.bg_rect = self.bg.get_rect(center=(
            self.screen.get_width() / 2, self.screen.get_height() / 2
        ))

        self.logo = pygame.image.load("./assets/logo.png")
        self.logo_rect = self.logo.get_rect(center=(320, 80))

        self.buttons = pygame.sprite.Group()
        self.buttons.add(MenuButton(320, 170, "CLASSIC", "classic"))
        self.buttons.add(MenuButton(320, 230, "REV MODE", "comp-guess"))
        self.buttons.add(MenuButton(320, 290, "HELP", "help-menu"))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.buttons:
                if button.check_press():
                    self.gameStateManager.set_state(button.targetState)
                    self.game.states[button.targetState].reset()

    def render(self):
        self.screen.blit(self.bg, self.bg_rect)
        self.screen.blit(self.logo, self.logo_rect)
        self.buttons.draw(self.screen)

    def run(self):
        self.buttons.update()
        self.render()
