# -*- coding: utf-8 -*-
"""
Created on Sun 12 Jan 2020

@author: dohma / Alexandra Dohm
"""

import Dominion
import testUtility

# Get player names
player_names = ["*Annie", "*Ben", "*Carla"]

# number of curses and victory cards
nV = testUtility.get_victory_cards(len(player_names))
nC = testUtility.get_curses_cards(len(player_names))

# Define box
box = testUtility.get_boxes(nV)

# Define supply order
supply_order = testUtility.get_supply_order()

# Pick 10 cards from box to be in the supply.
supply = testUtility.pick_random_cards(box)

# The supply always has these cards
# testUtility.populate_supply(supply, player_names, nV, nC)

# initialize the trash
trash = []

# Construct the Player objects
players = testUtility.construct_player_objects(player_names)

# Play the game
testUtility.play_game(supply, supply_order, players, trash)

# Final score
testUtility.print_final_score(players)
