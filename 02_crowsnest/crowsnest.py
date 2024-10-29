#!/usr/bin/env python3
"""
Author: frayjadour <frayjadour@gmail.com>
Purpose: Alert the captain using the correct article for an object.
"""

import argparse


def get_args():
    parser = argparse.ArgumentParser(description = 
                                     "Crow's nest -- choose the correct article")
    parser.add_argument('word', help = 'A word')
    return parser.parse_args()


def choose_article(word):
    first_letter = word[0].lower()
    article = 'an' if first_letter in 'aeiou' else 'a'
    
#    vowels = ['a', 'e', 'i', 'o', 'u']
#    if first_letter not in vowels:
#        article = 'a'
#    else:
#        article = 'an'
    return article


def main():
    args = get_args()
    word = args.word
    article = choose_article(word)
    phrase = f'Ahoy, Captain, {article} {word} off the larboard bow!'
    print(phrase)


if __name__ == '__main__':
    main()
