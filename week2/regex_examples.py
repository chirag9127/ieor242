from week1.parse_filing import ParseFiling
import re
import nltk


STR = "Match either serialise or serialize"
JUST_SUFFIX = '^.*(ing|ly|ed|ious|ies|ive|es|s|ment)$'
FULL_WORD = '^.*(?:ing|ly|ed|ious|ies|ive|es|s|ment)$'
DEFAULT = '^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)?$'

BASIC_TOKENIZER = ' ' # counter examples very\nwell
ONLY_WORDS = '\W+' # counter example first and last are empty strings
WITH_PUNCTUATION = '\w+|\S\w*' # hot-tempered gets split
FINAL_EXPRESSION = '\w+(?:[-']\w+)*|'|[-.(]+|\S\w*'


class RegexExamples():
    def __init__(self):
        self.pf = ParseFiling()
        self.text = self.pf.find_div_with_text()
        print "Finished fetching Google SEC document" 
        self.tokens = nltk.word_tokenize(self.text)
        print "Tokenizing using NLTK"
        self.wordlist = [w for w in self.tokens if w.islower()]
        print "Fetched all lowercase words"   

    def first_example(self):
        match = re.findall(r'seriali[sz]e', STR, re.M|re.I)
        if match:
            print "Matches are: ", match

    def find_words_ending_with(self, pattern):
        pattern = pattern + '$'
        words_ending_with_pattern = [w for w in self.wordlist if re.search(pattern, w)]
        return words_ending_with_pattern

    def find_words_with_pattern(self, pattern):
        words_with_pattern = [w for w in self.wordlist if re.search(pattern, w)]
        return words_with_pattern

    def compress(self, pattern, word):
        pieces = re.findall(pattern, word)
        return ''.join(pieces)

    def lossy_compression(self):
        pattern = '^[AEIOUaeiou]+|[AEIOUaeiou]+$|[^AEIOUaeiou]'
        print nltk.tokenwrap(self.compress(pattern, w) for w in self.wordlist)

    def stem(self, word, pattern=DEFAULT):
        stem, suffix = re.findall(pattern, word)[0]
        return stem

    def stemmer(self):
        return [self.stem(w) for w in self.tokens]

