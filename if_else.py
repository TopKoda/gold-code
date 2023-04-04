"""
If Else and elif example

Johnny Mac - 04 Apr 2023
"""
#!/bin/python3

import math
import os
import random
import re
import sys

def main():
    n = int(input("Please enter a number: ").strip())
    
    if n % 2 == 0:
        if n > 20:
            print("Not Weird")
        elif 2 <= n <= 5:
            print("Not Weird")
        elif 6 <= n <= 20:
            print("Not Weird")
        else:
            print("Number out of bounds")    
    else:
        print("Weird")
    
if __name__ == '__main__':
    main()