# Santa's Delivery Route Optimizer

## Overview

**Santa's Delivery Route Optimizer** is a Python script designed to help Santa Claus efficiently deliver presents to houses in a grid. It calculates the number of houses visited based on a set of directions provided in an input file. The script takes into account both Santa and Robo-Santa's movements to prevent double deliveries.

## Features

- **Grid Navigation**: The script reads a set of directions from a text file and simulates the movement of Santa and Robo-Santa on a grid to deliver presents.
- **Efficient Present Delivery**: By avoiding duplicate visits to the same house, the script ensures efficient present delivery during the holiday season.
- **Customizable Input**: You can easily provide your own set of directions in a text file to calculate deliveries for any given scenario.

## Functions and Classes

### `get_directions()`

This function reads the directions from a text file named "text.txt" and returns them as a string, allowing you to customize the delivery route.

### `deliver_presents_with_robot(directions, robot=True)`

This function takes a set of directions and a boolean parameter, `robot`, to determine whether both Santa and Robo-Santa should be used for deliveries. It simulates their movements based on the provided directions, tracks visited houses, and ensures that no house is visited more than once. The function returns the count of visited houses, indicating the total number of presents delivered.

## Usage

To use the script, you can provide your own set of directions by creating a "text.txt" file with the directions. Then, run the script, and it will calculate and display the number of houses visited by Santa and, if enabled, Robo-Santa.