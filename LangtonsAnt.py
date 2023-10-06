"""
Project 39, Langton's Ant: A cellular automata whose ants move according to simple rules.
Explore how simple rules create complex graphical patterns.

Langton's Ant is a cellular automata simulation on a two-dimensional grid, similar to
Project 13, "Conway's Game of Life." In the simulation, an "ant" begins on a square that
is one of two colors. If the space is the first color, the ant switches it to the second
color, turns 90 degrees to the right, and moves forward one space. If the space is the
second color, the ant switches it to the first color, turns 90 degrees to the left, and
moves forward one space.
Despite the very simple set of rules, the simulation displays complex emergent behavior.
Simulations can feature multiple ants in the same space, causing interesting interactions
when they cross paths with each other. Langton's Ant was invented by computer scientist
Chris Langton in 1986. More information about Langton's Ant can be found at
https://en.wikipedia.org/wiki/Langton%27s_ant
"""
