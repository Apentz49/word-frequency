import re
from collections import Counter

#open the txt file, read all, lowercase it, stirp it and find all the words in it.
words = re.findall(r'\w+', open('sample.txt').read().lower())

#Print out the 20 most common words in the file
print(Counter(words).most_common(20))
