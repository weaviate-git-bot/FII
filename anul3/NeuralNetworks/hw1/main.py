#!/usr/bin/python3
import os
from sys import argv
from matplotlib.pyplot import isinteractive

from numpy import isin

from lib import Parser
from lib.solvers import VanillaSolver, NumpySolver
from lib.tests import TestSolver

def help() -> None:
    print("""Neural Network Homework 1 @ Bogdan Zavadovschi

Usage: ./main.py <fileName> <action>

List of actions: vanilla, numpy, test

If you need more help contact the owner :D""")

def start():
    if len(argv) != 3:
        return help()

    input_file = argv[1]
    script_to_run = argv[2]

    input_data = Parser(input_file).parse()

    try:
        result = {
            'vanilla': VanillaSolver,
            'numpy': NumpySolver,
            'test': TestSolver 
        }[script_to_run](input_data[0], input_data[1]).solve()

        if result and isinstance(result, list):
            print(f"X = {result[0]}, Y = {result[1]}, Z = {result[2]}")
            return

        if result and isinstance(result, bool):
            if result is True:
                print("Test passed")
            else:
                print("Test failed")
            return

        print('Unknown result type.')

    except KeyError:
        print('Failed to find the specified value! Allowed one are: vanilla, numpy, test')

if __name__ == '__main__':
    start()