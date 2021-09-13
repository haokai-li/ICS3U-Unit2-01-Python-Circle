#!/usr/bin/env python3

# Created by: Haokai Li
# Created on: Sept 2021
# This is the "circle"Program, with proper style

import math


def main():
    # This function calculate area and perimeter of circle

    print("A radius with dimensions 15 mm.")
    print("Calculate the area and perimeter of circle.")
    print("")
    print("a = πr2 = {} mm²".format(math.pi * 15 ** 2))
    print("p = 2πr = {} mm".format(2 * math.pi * 15))
    print("")
    print("Done")


if __name__ == "__main__":
    main()
