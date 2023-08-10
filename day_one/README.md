# Day 1: Santa's Journey

## Challenge Overview
This script determines Santa's final floor and the position that first brings Santa to the basement (-1 floor) in a building, based on a series of instructions. The instructions are read from a text file ("text.txt"), where each character represents an instruction: "(" means go up one floor, and ")" means go down one floor.

### Part One:
In this challenge, Santa is trying to deliver presents in a large apartment building, but he's having trouble finding the right floor due to confusing directions. He starts on the ground floor (floor 0) and follows the instructions one character at a time. An opening parenthesis "(" means he should go up one floor, and a closing parenthesis ")" means he should go down one floor.

The challenge is to determine the floor that Santa ends up on after following all the instructions. For example, "(())" and "()()" both result in floor 0, "(((" and "(()(()(" both result in floor 3, etc.

### Part Two:
Using the same set of instructions, the next task is to find the position of the first character that causes Santa to enter the basement (floor -1). The position of the characters starts from 1, so for example, ")" causes him to enter the basement at character position 1, "()())" causes him to enter the basement at character position 5.

The goal is to find the position of the character that causes Santa to first enter the basement.

## Functionality 
The script has the following main functions:

1. `convert_to_string()`: This function reads the instructions from a text file, converting the content into a string.

2. `convert(my_string)`: This function takes the string of instructions and breaks it into a list of characters (instructions). It ignores any spaces in the input string.

3. `floor_count(my_chars)`: This function takes the list of instructions and processes them to determine Santa's final floor and the position that first brings him to the basement. It uses a while loop to iterate through the list of instructions, incrementing a 'floor' counter for "(" instructions and decrementing it for ")" instructions. It also keeps track of the 'position' within the instructions. The first time Santa reaches the basement (floor -1), it records that position.

## Sample Output

Santans Floor: 232
Basement position: 1783