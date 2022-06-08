import nltk
#     Stwórz listę z poniższymi wyrazami:
#     programming, Python, prgrming, python, Programing, to program
#
#     Napisz wyrażenie regularne, które znajdzie różne warianty wyrazu "programming". Skorzystaj z re_show i pętli "for".
# https://python.hotexamples.com/examples/nltk/-/re_show/python-re_show-function-examples.html

words = ["programming", "Python", "prgrming", "python", "Programing", "to program"]

text = "The programming in Python is a very fun task. To program or not to program, that is a question?"

regex = "("

for w in words:
    regex = regex + w + "|"

regex = regex[:-1] + ")"

print(regex)

nltk.re_show(regex, text)