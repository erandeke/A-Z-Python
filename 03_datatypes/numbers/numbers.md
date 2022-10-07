## Python DECIMAL

We generally use Decimal in the following cases.

When we are making financial applications that need exact decimal representation.
When we want to control the level of precision required.
When we want to implement the notion of significant decimal places.

For example when we do calculate 1.1 + 2.2 ideally ans should
be 3.3 but floating point numbers are stored in computer in fractions and which
are approximate .

so if we do 1.1+2.2 it turns out to be
3.3000000000000003

instead use decimal to represent the exact value

from decimal import Decimal as D
print(D('1.1')+D('2.2')) = 3.3

## Python Fractions

Again fractions are stored in infinite long binary representation on the system . hence
in python there is a module Fractions that helps to give exact fractional figure

from fractions import Fraction as F;
print(F('1/3')+F('1/3')) = 2/3

## Python Math

Math functions in python are dedicated to use in performing mathematical, stats and algebra calculations
some of the functions

Math.pi
Math.cos
Math.sinh
Math.Fraction

More can be explored based upon usecase

## Python random

In Python random is use for generation of randon numbers , selecting the random
from your choice , shuffling the array etc 

some of the examples 

random.choice();
random.shuffle();