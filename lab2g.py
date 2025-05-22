#!/usr/bin/env python3
# Author - Ansh Domadiax
# Author ID: addomadia@myseneca.ca
# Date Created: 2025/05/22

import sys

# Set default timer value
if len(sys.argv) > 1:
    timer = int(sys.argv[1])
else:
    timer = 3

# Countdown loop
while timer > 0:
    print(timer)
    timer -= 1

print("blast off!")

