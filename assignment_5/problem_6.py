"""Digital cameras manufactures have yet to agree on a standard name and date format
for naming image files. Write a function that reformats filenames from the MM-DD-YYYY
(month-day-year) date format to the DD-MM-YYYY (day-month-year).

The file extension should be preserved. Use regular expression to match the date format.
"""

import re


def updateDateFormat(original):
    date_pattern = re.compile(r"^([0-9]{2})-([0-9]{2})-([0-9]{4})(\.[a-zA-z]+)$")
    return date_pattern.sub(r"\2-\1-\3\4", original)


print(updateDateFormat("10-31-2019.jpg"))
print(updateDateFormat("10-31-2019.jpg"))
