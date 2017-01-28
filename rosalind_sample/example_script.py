# -*- coding: utf-8 -*-
import sys

def min_skew_indeces(genome_string):
    """
    Full code goes, that solves all the instances, and not just the sample dataset, goes HERE!
    """
    return [53, 97]

if __name__ == "__main__":
    input_file_path = sys.argv[1]
    with open(input_file_path, "rt") as source:
        data_line = source.readline()                               # reading the first string in the input.txt file
                                                                    # if more string need to be read, adjust this string accordingly
        genome = data_line.strip()                                  # removing the empty characters at the end of the string
        min_skew_indeces = min_skew_indeces(genome_string=genome)   # invoke the function, that does all the work and returns a list of indexes with minimal skews
        print(" ".join(map(str, min_skew_indeces)))                 # printing a list of integers as string, separated by spaces
