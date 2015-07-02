import re
from collections import Counter
words = re.findall(r'\w+', open('sample.txt').read().lower())
print(Counter(words).most_common(20))
