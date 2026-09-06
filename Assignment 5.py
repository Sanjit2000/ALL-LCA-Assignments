# Problem Statement: PAN Number Validation Using Regular Expression
# Write a Python program that accepts a PAN number from the user and validates it using a
# regular expression. The program must ensure that the input contains only the permitted
# characters—uppercase letters (A–Z) and digits (0–9)—and follows the standard 10-character
# PAN format:
# AAAAA9999A
# where the first five characters are uppercase letters, the next four are digits, and the last
# character is an uppercase letter.
# Display "Valid PAN Number" if the input matches the required pattern; otherwise, display
# "Invalid PAN Number".
# Examples:
# ABCDE1234F → Valid PAN Number
# ABCD@1234F → Invalid PAN Number
# ABCDE12345 → Invalid PAN Number

import re

pan = input("Enter PAN Number: ")

if re.match(r'^[A-Z]{5}[0-9]{4}[A-Z]$', pan):
    print("Valid PAN Number")
else:
    print("Invalid PAN Number")

