#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    with open(filename) as f:
        file_string = f.read()
    year_pattern = re.compile(r"Popularity\sin\s([0-9]{4})")
    name_ranking_pattern = re.compile(
        r"<tr\salign=\"right\"><td>([0-9]+)</td><td>([a-zA-Z]+)</td><td>([a-zA-Z]+)</td>"
    )
    year = year_pattern.findall(file_string)
    name_ranks = {}
    for name_data in name_ranking_pattern.findall(file_string):
        (rank, boy_name, girl_name) = name_data
        if boy_name not in name_ranks:
            name_ranks[boy_name] = rank
        if girl_name not in name_ranks:
            name_ranks[girl_name] = rank

    names_sorted = sorted(name_ranks.keys())
    names = [year[0]]

    for name in names_sorted:
        names.append(f"{name} {name_ranks[name]}")

    return names


def main():
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]

    if not args:
        print("usage: [--summaryfile] file [file ...]")
        sys.exit(1)

    # Notice the summary flag and remove it from args if it is present.
    summary = False
    if args[0] == "--summaryfile":
        summary = True
        del args[0]
    for filename in args:
        names = extract_names(filename)
        text = "\n".join(names) + "\n"
        print(text)

        if summary:
            with open(filename + ".summary", "w", encoding="utf-8") as f:
                f.write(text + "\n")
                f.close()
        else:
            print(text)


if __name__ == "__main__":
    main()
