"""A palindrome is a word, phrase, or sequence that reads the same backward as forward. For example, mom , racecar ,
"never odd or even", and "do geese see god" are all palindromes.

Write a program that prompts a user to enter a word or phrase and test if it is a palindrome. Ignore any spaces when evaulating the strings.

Example:

> Enter a word or phrase: dad
This is a palindrome.
> Enter a word or phrase: dog
This is not a palindrome."""


def palindrome():
    word = input("Enter a word or phrase: ")
    if word == word[::-1]:
        print("This is a palindrome")
    else:
        print("This is not a palindrome")


palindrome()
