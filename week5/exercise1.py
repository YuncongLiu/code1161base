# -*- coding: UTF-8 -*-
"""Refactoring.

This excercise is very similar to week 2, exercise 2. It contains a complete
and working example, but it's very poorly written.

Your job is to go through it and make it as good as you can.

That means making it self-documenting wherever possible, adding comments where
it isn't. Take repeated code and make it into a function. Also use functions
to encapsulate concepts. If something is done many times, maybe a map or a loop
is called for. Etc.

The resulting file should feel as close to english as possible.
It must also pass the linter.

This is the first file that will be run against the pydocstyle checker. If
you've run the week5_system_prep.sh file you should be getting blue linter dots
that show you where lintere errors are. If they aren't working, you should be
getting the errors in the test output.

Some functions will have directions as external comments, once you think you
are on top of it, take these comments out. Others won't have comments and
you'll need to figure out for yourself what to do.
"""

from __future__ import division
from __future__ import print_function
import math


# This is a terrible function. The rest of the functions in this file do a
# much better job of what it's trying to do. Once you've has a little look,
# move on, and eventually delete this function. (And this comment!)
def do_bunch_of_bad_things():
    """Docstring."""
    print(countdown("Getting ready to start in ", 9, 0, "Let's go!"))

    triangle = {"base": 3, "height": 4}
    triangle["hypotenuse"] = triangle["base"]**2 + triangle["height"]**2
    print("area = " + str((triangle["base"] * triangle["height"])/2))
    print("side lengths are:")
    print("base: {}".format(triangle["base"]))
    print("height: {}".format(triangle["height"]))
    print("hypotenuse: {}".format(triangle["hypotenuse"]))

    another_hyp = 5**2 + 6**2
    print(another_hyp)

    yet_another_hyp = 40**2 + 30**2
    print(yet_another_hyp)


# return a lit of countdown messages, much like in the bad function above.
# It should say something different in the last message.
def countdown(message, start, stop, completion_message):
    """Start the game off with a countdown message."""
    countMessage = []
    if start > stop:
        step = -1
    elif start < stop:
        step = +1
    for i in range(start, stop, step):
        loopMessage = message + str(i)
        countMessage.append(loopMessage)
    countMessage.append(completion_message)
    return countMessage
    pass


# TRIANGLES

# This should be a series of functions that are ultimatly used by
# triangle_master
# It should eventually return a dictionary of triangle facts. It should
# optionally print information as a nicely formatted string. Make printing
# turned off by default but turned on with an optional argument.
# The stub functions are made for you, and each one is tested, so this should
# hand hold quite nicely.
def calculate_hypotenuse(base, height):
    """Calculate the hypotheneus of a triangle."""
    hypotheneus = math.sqrt(base ** 2 + height ** 2)
    return hypotheneus


def calculate_area(base, height):
    """Calculate the area of a triangle."""
    area = (1 / 2) * base * height
    return area


def calculate_perimeter(base, height):
    """Calculate the perimeter of a triangle."""
    perimeter = base + height + calculate_hypotenuse(base, height)
    return perimeter


def calculate_aspect(base, height):
    """Determine the aspect of a triangle."""
    if height > base:
        return "tall"
    elif height == base:
        return "equal"
    else:
        return "wide"


# Make sure you reuse the functions you've already got
# Don't reinvent the wheel
def get_triangle_facts(base, height, units="mm"):
    """Gatter information of the triangle."""
    return {"area": calculate_area(base, height),
            "perimeter": calculate_perimeter(base, height),
            "height": height,
            "base": base,
            "hypotenuse": calculate_hypotenuse(base, height),
            "aspect": calculate_aspect(base, height),
            "units": units}


# this should return a multi line string that looks a bit like this:
#
# 15
# |
# |     |\
# |____>| \  17.0
#       |  \
#       |   \
#       ------
#       8
# This triangle is 60.0mm²
# It has a perimeter of 40.0mm
# This is a tall triangle.
#
# but with the values and shape that relate to the specific
# triangle we care about.
def tell_me_about_this_right_triangle(facts_dictionary):
    """Send information about this triangle."""
    tall = """
            {height}
            |
            |     |\\
            |____>| \\  {hypotenuse}
                  |  \\
                  |   \\
                  ------
                  {base}"""
    wide = """
            {hypotenuse}
             ↓         ∕ |
                   ∕     | <-{height}
               ∕         |
            ∕------------|
              {base}"""
    equal = """
            {height}
            |
            |     |⋱
            |____>|  ⋱ <-{hypotenuse}
                  |____⋱
                  {base}"""

    pattern = ("This triangle is {area}{units}²\n"
               "It has a perimeter of {perimeter}{units}\n"
               "This is a {aspect} triangle.\n")

    facts = pattern.format(**facts_dictionary)

    height = facts_dictionary["height"]
    base = facts_dictionary["base"]

    if height > base:
        ret = tall.format(**facts_dictionary)
    elif height == base:
        ret = equal.format(**facts_dictionary)
    else:
        ret = wide.format(**facts_dictionary)

    ret = ret + "\n" + facts
    return ret


def triangle_master(base,
                    height,
                    return_diagram=False,
                    return_dictionary=False):
    """Return a diagram or dictionary."""
    dictionary = get_triangle_facts(base, height)
    diagram = tell_me_about_this_right_triangle(dictionary)
    if return_diagram and return_dictionary:
        return {'diagram': diagram, 'facts': dictionary}
    elif return_diagram:
        return diagram
    elif return_dictionary:
        return {'facts': dictionary}
    else:
        print("You're an odd one, you don't want anything!")


def wordy_pyramid():
    """Return a word pyramid."""
    pyramid_list = list_of_words_with_lengths(range(3, 21, 2))
    pyramid_list += list_of_words_with_lengths(range(20, 3, -2))
    return pyramid_list
    # import requests
    # baseURL = "http://www.setgetgo.com/randomword/get.php?len="
    # pyramid_list = []
    # for i in range(3, 21, 2):
    #     url = baseURL + str(i)
    #     r = requests.get(url)
    #     message = r.text
    #     pyramid_list.append(message)
    # for i in range(20, 3, -2):
    #     url = baseURL + str(i)
    #     r = requests.get(url)
    #     message = r.text
    #     pyramid_list.append(message)
    # return pyramid_list


def get_a_word_of_length_n(length):
    """Get a word of length through URL request."""
    import requests
    baseURL = "http://www.setgetgo.com/randomword/get.php?len="
    try:
        length = int(length)
        if length >= 3:
            url = baseURL + str(length)
            r = requests.get(url)
            message = r.text
            return message
    except ValueError:
        message = None


def list_of_words_with_lengths(list_of_lengths):
    """Use the word length in list to find a word of equal length."""
    wordsRet = []
    for i in list_of_lengths:
        wordsRet.append(get_a_word_of_length_n(i))
    return wordsRet


if __name__ == "__main__":
    do_bunch_of_bad_things()
