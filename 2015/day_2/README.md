# Day 2: Calculate warpping paper and ribbon 

## Challenge Overview
The challenge involves calculating the exact amount of wrapping paper and ribbon needed for a list of presents. Each present is a box (a perfect right rectangular prism) with given dimensions (length l, width w, and height h).

## Part One
The amount of wrapping paper for each box is determined by the surface area (2lw + 2wh + 2hl) plus the area of the smallest side. The aim is to determine the total square feet of wrapping paper needed for all presents.

## Part Two
The amount of ribbon required to wrap a present is determined by the shortest distance around its sides (the smallest perimeter of any one face), plus a bow made out of ribbon. The feet of ribbon required for the bow equals the cubic feet of volume of the present.

## Functionality 
The script is divided into five functions:

1. format_string(): 
This function opens a text file named "text.txt", reads its contents, and returns the content as a string. The text file is expected to contain the dimensions of the boxes, with each dimension separated by 'x' and each box on a new line.

2. 
format_ints(): This function takes the string of box dimensions returned by format_string(), and parses it to extract the individual dimensions as integers. The digits of each number are built up until an 'x' or a newline is encountered, at which point the built-up number is converted to an integer and added to the list. The function finally returns the list of integers.

3. get_slack_total(l, w, h): 
This function takes the dimensions of a box as input, removes the largest dimension, and then multiplies the remaining two smallest dimensions together to calculate the slack needed for the wrapping paper. The function returns this slack total.

4. get_ribbon_total(l, w, h): 
This function also takes the dimensions of a box as input. It calculates the volume of the box (for the bow) and removes the largest dimension from the list. It then multiplies the remaining two smallest dimensions by 2 and sums them to calculate the ribbon needed to wrap around the box. The function finally adds the ribbon and bow lengths together to get the total ribbon needed and returns this total.

5. box_dimensions(numbers): 
This function takes the list of integers returned by format_ints(), treats every three integers as the dimensions of a box, and calculates the total wrapping paper and ribbon needed for all boxes. It does this by calling get_slack_total() and get_ribbon_total() for each box to get the slack and ribbon needed, then adds these to running totals. The function finally returns the total wrapping paper and ribbon needed

The script then calls these functions and prints the total wrapping paper and ribbon needed.



