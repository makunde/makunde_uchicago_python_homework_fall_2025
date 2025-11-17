"""
By the date of the midterm exam, you will have already received hundreds of pages of pdfs.
Trying to review all those notes, might be a bit daunting. To help you prepare for the exam,
create an index of all the class lecture slides by converting the pdf files to text. After
all, we might as well use our new skills to help us study.

Using conda, download and install the PyPDF2 package. This package provides modules to
extract the text from pdf files. For more information Extracting Text from Pdf Files
Using PythonLinks to an external site..

How you decide to organize your index is up to you. Two possible approaches could be:

A single .txt file that your can regex in VSCode with file and page numbers
One file per lecture with keywords sorted by frequency
Provide the program with detailed documentation and an example of how to use it. Provide
a sample pdf files (eg. one set of lecture slides) in your repository so that we can easily
run the script with the supplied commands. The entire program should be able to be run by
simply cutting and pasting the command you provide in your repository directory.

Add your index file(s) to the repository and clearly label them
(eg. index.txt, index_lecture_2.txt, etc.) so we can see what the output looks like.
"""

import sys
import study

COMMON_WORDS_FLAG = "--common_words_filter="


# See Instructions in README
def main():
    args = sys.argv[1:]
    common_words_filter = False
    if COMMON_WORDS_FLAG in args[0]:
        common_words_filter = True
        common_words_filename = args[0][len(COMMON_WORDS_FLAG) :]
        del args[0]
    if not common_words_filter:
        sys.stderr.write(
            "Use the --common_words_filter flag to filter out common words. This flag is required\n"
        )
        print("usage: [--common_words_filter=file.txt] file [file ...]\n")
        sys.exit(1)
    print(common_words_filename)
    for filename in args:
        key_words_dict = study.extract_key_words(filename, common_words_filename)
        sorted_keyword_list = study.sort_keywords_by_frequency(key_words_dict)
        study.write_keywords_to_index(sorted_keyword_list, filename)


if __name__ == "__main__":
    main()
