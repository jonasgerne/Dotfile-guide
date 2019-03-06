#!/usr/bin/env python
import argparse


def filter(filename, filterstring, outputfilename):
    with open(filename, "r") as f:
        inlines = f.readlines()

    with open(outputfilename, "w") as f:
        [f.write(l) for l in inlines if filterstring not in l]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Hide states from your Smach Viewer.')
    parser.add_argument('inputfile', type=str, help='the inputfile to process')
    parser.add_argument('outputfile', type=str, help='the filename for the output')
    parser.add_argument('filterstring', type=str, help='the State you want to hide/remove from the dotfile. Enter like "/StateMachine/error"')
    args = parser.parse_args()

    filter(args.inputfile, args.filterstring, args.outputfile)
