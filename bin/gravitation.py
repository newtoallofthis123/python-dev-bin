#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  gravitation.py

# MIT License

# Copyright (c) 2021 Noob Science

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# By the way, the formula of Gravitational force is
# F = GxM1xM2/R^2

length = len("Gravitational Force Calculator") # Don't mind this, this is just for line under the title
print("\nGravitational Force Calculator")
print("_"*length)
x = float(6.75)

# Geting User input
radius = float(input("Enter distance between two bodies(m): "))
m1 = float(input("Enter the mass of the first body(kg): "))
m2 = float(input("Enter the mass of the second body(kg): "))

# Defining Answer
distance = 1/radius
ans = str(x * m1 * m2 * distance)
ans_length = len("Gravitational Force(F) = " + ans + " x 10^-11 N-m^2 kg^-2")  # Don't mind this, this is just for the lines in between
print("_"*ans_length)
print("\nGravitational Force(F) = " + ans + " x 10^-11 N-m^2 kg^-2") # Printing the answer with a small description
print("_"*ans_length)
print("NoobScience 2021")

# Hope you enjoy using and Hope you find it usefull
