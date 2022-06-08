text = "What a tragedy! 2020 is a totally different year because of the viiiirus. Who could predict in 2019 that in 2020 students in many countries will take online tests because of pandemic of Covid-19?! The other name of this deadly Vairuuuuus is SARS-Cov-2. I hate this viiirs!"

import re
from nltk.stem import PorterStemmer
from nltk.tokenize import WordPunctTokenizer

regex = "[vV][ai]+ru*s"

found_words = re.findall(regex, text)

print("Znaleziono ", len(found_words) , " wirusów: ", found_words, ".")

t = WordPunctTokenizer()
s = PorterStemmer()

all_stems = [s.stem(x) for x in t.tokenize(text)]

print(len(all_stems))
print(len(set(all_stems)))

stem_set = set(all_stems)

print(sorted(stem_set))
print(sorted(stem_set, reverse=True))


# Kombinacja liter, cyfr i myślników
regex = "[a-zA-Z]+[\-0-9]+"


result = re.sub(regex,  'XXXX', text)
print(result)

