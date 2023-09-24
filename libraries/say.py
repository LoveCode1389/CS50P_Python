import cowsay
import sys

"""
    cowsay lib shapes:
    -beavis
    -cheese
    -daemon
    -cow
    -dragon
    -ghostbusters
    -kitty
    -meow
    -milk
    -stegosaurus
    -stimpy
    -turkey
    -turtle
    -tux
    -pig
    -trex
    -miki
    -fox
    octopus

try!
"""

if len(sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1])