import os

"""Write a program that takes string input representing a file path 
and recursively print out files in that directory and each subdirectory.
This is sometimes referred to as walking through a directory.

The program execution should look similar to the following:

% python problem_4.py home/

home/   
 file1.txt   
 file2.txt   
 photos/   
  photo1.jpg   
  photo2.jpg   
  favorites/   
   beach1.png   
   hawaii.png  
  
Note that folders are indicated with an / and files or folders within a folder are indented. Your solution should use recursive programming techniques and make use of the Python os module.

Note: There is a standard Python module that provides this exact functionality through one of its functions. Identify the Python module and function and make a note of it in a comment at the top of the file. Use this to test your work, but do not use the module for solving problem."""
DEFAULT_INDENT = "   "


def walk_through_directory(path, indent=""):
    if not os.path.exists(path):
        return
    if not os.path.isdir(path):
        return
    print(f"{indent}{path}/")
    items = sorted(os.listdir(path))
    indent += DEFAULT_INDENT
    subdirectories = []
    for item in items:
        fpath = os.path.join(path, item)
        if os.path.isdir(fpath):
            subdirectories.append(fpath)
        else:
            print(f"{indent}{item}")
    for subdir in subdirectories:
        walk_through_directory(subdir, indent)


paths = "/Users/georg/Documents/uchicago_concepts_of_programming/assignment_4/home"
walk_through_directory(paths)
