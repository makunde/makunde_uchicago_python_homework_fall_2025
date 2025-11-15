"""Write a function that draws a triangle out of asterix similar to that below. The function should take an integer argument that
represents the height of the triangle. Do not use a recursive function.

def pyramid(height):
 pass
Example of invoking the function with an argument of 5:

pyramid(height:5)


*
**
***
****"""


def triangle(height):
    triangle = ""
    for i in range(height):
        asterisk_count = i + 1
        while asterisk_count > 0:
            triangle += "*"
            asterisk_count -= 1
        if i + 1 != height:
            triangle += "\n"

    return triangle


print(triangle(7))
