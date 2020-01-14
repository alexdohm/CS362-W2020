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
if len(player_names) > 2:
    nV = 12
else:
    nV = 8
nC = -10 + 10 * len(player_names)

# Define box & supply order
box = testUtility.get_boxes(nV)
supply_order = testUtility.get_supply_order()

# Pick 10 cards from box to be in the supply.
supply = testUtility.pick_random_cards(box)

# The supply always has these cards
testUtility.populate_supply(supply, player_names, nV, nC)

# initialize the trash
trash = []

# Construct the Player objects
players = testUtility.construct_player_objects(player_names)

# Play the game
turn = 0
while not Dominion.gameover(supply):
    turn += 1
    print("\r")
    for value in supply_order:
        print(value)
        for stack in supply_order[value]:
            if stack in supply:
                print(stack, len(supply[stack]))
    print("\r")
    for player in players:
        print(player.name, player.calcpoints())
    print("\rStart of turn " + str(turn))
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players, supply, trash)

# Final score
dcs = Dominion.cardsummaries(players)
vp = dcs.loc['VICTORY POINTS']
vpmax = vp.max()
winners = []
for i in vp.index:
    if vp.loc[i] == vpmax:
        winners.append(i)
if len(winners) > 1:
    winstring = ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0], 'wins!'])

print("\nGAME OVER!!!\n" + winstring + "\n")
print(dcs)
