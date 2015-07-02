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

def word_frequency(word_freq):
    """This function creates our dict and counts our words."""

    words_counts = {} #This is our dict

    #count number of times a word appears
    for words in word_freq:
        if words not in words_counts:
            words_counts[words] = 1
        else:
            words_counts[words] += 1

    return words_counts



if __name__ == "__main__":

    with open("sample.txt") as sample_text:
        #Open my file

        words = re.sub(r'[^A-Za-z ]', " ", sample_text.read().lower())
        #Read everything in the file, stirp it and lowercase it all

        new_text = words.split()
        #split each word into a list

        print(sorted(word_frequency(new_text)))
