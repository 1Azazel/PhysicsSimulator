import numpy as np
import turtle as t
import pygame

## draw scripts

## transform scripts

## display scripts


def main():
    scripts = []
    while True:
        select = input("Make Selection: ")
        for script in scripts:
            if script == select:
                script()
