# Day 5: Doesn't He Have Intern-Elves For This?

## Challenge Overview
Santa needs help figuring out which strings in his text file are naughty or nice. 

## Features

- **Vowel Count**: Checks if a line contains at least three vowels (aeiou).
- **No Naughty Pairs**: Ensures the absence of specific "naughty" pairs.
- **Repeated Pair**: Verifies if at least one letter appears twice in a row.
- **Two Pairs of Letters**: Checks for at least two pairs of letters.
- **Repeating Letter with Gap**: Detects two repeating letters with one letter in between.
- **Non-Overlapping Repeated Pairs**: Ensures that repeated pairs do not overlap.

## Functions

### Part One:

#### `read_file()`
Reads lines from a file and returns a list of lines. 
This function is responsible for reading a file named 'text.txt', cleaning the lines, and returning them as a list of strings.

#### `has_vowels(my_line)`
Checks if a line contains at least three vowels (aeiou). 
It counts the vowels in the given line and returns `True` if at least three vowels are present, indicating a "nice" string.

#### `has_no_naughty_strings(my_line)`
Ensures that the line doesn't contain "naughty" pairs (ab, cd, pq, xy). 
It checks the line for the presence of these disallowed substrings and returns `True` if none of them are found, indicating a "nice" string.

#### `has_pair(my_line)`
Checks for at least one letter that appears twice in a row. 
This function examines the line to find any repeating letters, and if it identifies at least one instance of a letter appearing twice in a row, it returns `True`, marking the string as "nice."

#### `count_nice_strings_part_one(my_list)`
Counts the number of "nice" strings based on part one criteria. 
It takes a list of lines as input, iterates through them, and checks if each line is "nice" according to the criteria. It returns the count of "nice" strings found in the list.

### Part Two:

#### `has_two_pairs(my_line)`
Checks for at least two pairs of letters. 
This function examines the line to identify repeated pairs of letters. If it finds at least two such pairs, it returns `True`, indicating that the line is "nice" as per the Part Two criteria.

#### `has_repeating_letter_with_gap(my_line)`
Checks for two repeating letters with one letter in between. 
It looks for repeating letter patterns with one letter in between, such as 'xyx'. If it finds any such pattern, it returns `True`, marking the string as "nice."

#### `has_no_overlap(my_line)`
Ensures that repeated pairs don't overlap. 
This function examines the line for non-overlapping repeated pairs (e.g., 'aaa' and 'aaxa'). It returns `True` if it does not find any overlapping repeated pairs, indicating a "nice" string.

#### `count_nice_strings_part_two(my_list)`
Counts the number of "nice" strings based on part two criteria. 
It takes a list of lines as input, iterates through them, and checks if each line meets the Part Two criteria. It returns the count of "nice" strings found in the list, following the expanded requirements.

