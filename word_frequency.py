#Your program should open sample.txt and read in the entirety of its text.
#You'll need to normalize the text so that words in different cases are,
#still the same word and so it's scrubbed of punctuation.
#Once you've done that, go through the text and find the number,
#of times each word is used.
#
#After that, find the top 20 words used and output them to the console,
#in reverse order, along with their frequency.

import re


#def word_frequency(word_freq):
#this needs to take the file from my with statement and find the top 20 words
def open_file():
    with open("sample.txt") as sample_text:
        words = re.sub(r'[^A-Za-z ]', " ", sample_text.read().lower())
        new_text = words.split()
        return (sorted(new_text))


def word_frequency(word_freq):
    words_counts = {}
    for words in word_freq:
        if words not in words_counts:
            words_counts[word] = 1
        else:
            words_counts[word] += 1

    return words_count_list



if __name__ == "__main__":

    open_file(word_frequency(word_freq))
