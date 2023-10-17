# Day 4: helping santa mine Adventcoins. 

## Challenge Overview
Santa is looking for help mining AdventCoins, which are similar to bitcoins. He wants to find MD5 hashes with at least five leading zeros in hexadecimal. To achieve this, you need to combine a secret key with a decimal number, and your goal is to discover the lowest positive number (without leading zeros) that generates such a hash.

## Features

- **Customizable Difficulty**: You can specify the number of leading zeros required in the hash by setting the `_difficulty` parameter.
- **MD5 Hashing**: The script utilizes the MD5 hashing algorithm to compute hashes based on the input text and nonce.

## Functions and Classes

### `check_hash(_hash_hex, _difficulty)`

This function checks if the generated hash `_hash_hex` has the required number of leading zeros specified by the `_difficulty` parameter. It iterates through the hash characters and returns `True` if the first `_difficulty` characters are '0', indicating a valid hash. If any non-'0' character is encountered, it returns `False`.

### `generate_hash(_text, _nonce)`

The `generate_hash` function generates a hash by concatenating the `_text` and `_nonce` as a string and then using the MD5 hash algorithm. It returns the hexadecimal representation of the hash.

### `pow(_text, _difficulty)`

The `pow` function implements the proof-of-work (PoW) algorithm. It takes the input `_text` and `_difficulty`, initializes a nonce to 0, and continues to increment it until a hash is found that meets the condition specified by `check_hash()`. It returns both the resulting hash and the nonce when a valid hash is found.

## Usage

You can run the script by setting the desired `text` and `difficulty` values in the "Main Program" section. The script will find a nonce that results in a hash with the specified number of leading zeros.
