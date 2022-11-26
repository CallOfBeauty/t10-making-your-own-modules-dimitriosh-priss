######################################################################
# TODO: Change the author(s) and username(s) to yourself and your partner (if any).
# Author(s): Jan Pearce and Patrick Shepherd
# Username(s): pearcej shepherdp
#
# Assignment: T10: Making Your Own Modules
#
# Purpose: A test suite to test the t10_dots code
#
######################################################################
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import sys

# TODO: Import your module here so that you can access the functions in it.

from inspect import getframeinfo, stack

from t10_dots import *


def unittest(did_pass):
    """
    Print the result of a unit test.
    :param did_pass: a boolean representing the test
    :return: None
    """

    caller = getframeinfo(stack()[1][0])
    linenum = caller.lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def dotssuit():
    """
    The dotssuit() is designed to test the following:
    calculate_size(num_dots):
    is_valid_size(dot_width, dot_height, distance, screen_width, screen_height):
    draw_board(dot_distance, dottie, height, width):
    user_input(screen_height, screen_width):

    :return: None
    """

    print("Testing calculate_size()")
    unittest(user_input("why",5) =="2","5", "10")




# TODO: Define a test suite function, provide it with a docstring, and fill it with
# unit tests!  Be sure to add helpful comments to your tests.


def main():
    """
    The main() function runs the sequence_gene code, which calls all other parts of this code
    :return: None
    """
    dotssuit()


if __name__ == "__main__":
    main()          # call to main() function
