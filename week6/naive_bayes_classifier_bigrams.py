from nltk.metrics import *
from nltk.classify import NaiveBayesClassifier
from nltk import word_tokenize, FreqDist, classify
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
import collections
import itertools


train_set = [
    ('I love this sandwich', 'pos'),
    ('This is an amazing place', 'pos'),
    ('I feel very good about these beers', 'pos'),
    ('This is my best work', 'pos'),
    ('What an awesome view', 'pos'),
    ('I do not like this restaurant', 'neg'),
    ('I am tired of this stuff', 'neg'),
    ('I cannot deal with this', 'neg'),
    ('He is my sworn enemy', 'neg'),
    ('My boss is horrible', 'neg'),
    ('I love this car', 'pos'),
    ('This view is amazing', 'pos'),
    ('I feel great this morning', 'pos'),
    ('I am so excited about the concert', 'pos'),
    ('He is my best friend', 'pos'),
    ('I do not like this car', 'neg'),
    ('This view is horrible', 'neg'),
    ('I feel tired this morning', 'neg'),
    ('I am not looking forward to the concert', 'neg'),
    ('He is my enemy', 'neg'),
    ('You are very intelligent', 'pos'), 
    ('He does not have a car', 'neg'), 
    ('I am not going to pay my bills', 'neg'),
    ('You appear tired', 'neg'),
    ('I like reading', 'pos'),
    ('I hate my life', 'neg'),
    ('I do not like him', 'neg'),
    ('I like lying', 'neg'),
]
test_set = [
    ('The beer was good.', 'pos'),
    ('I do not enjoy my job', 'neg'),
    ('I am not feeling dandy today', 'neg'),
    ('I feel amazing', 'pos'),
    ('Gary is a friend of mine', 'pos'),
    ('I cannot believe I am doing this', 'neg'),
    ('I feel happy this morning', 'pos'),
    ('Larry is my friend', 'pos'),
    ('I do not like that man', 'neg'),
    ('My house is not great', 'neg'),
    ('Your song is annoying', 'neg'),
    ('Today was a great day', 'pos'),
    ('That is so not cool', 'neg'),
    ('You are very stupid', 'neg'),
    ('He is not that smart', 'neg'),
    ('There is no hope for them', 'neg')
]

train_set_words = []
for item in train_set:
    words = word_tokenize(item[0])
    for word in words:
        train_set_words.append(word)

all_words = FreqDist(w.lower() for w in train_set_words).keys()

def tweet_features(tweet):
    tweet_words = word_tokenize(tweet)
    bigram_finder = BigramCollocationFinder.from_words(tweet_words)
    score_fn=BigramAssocMeasures.chi_sq
    bigrams = bigram_finder.nbest(score_fn, 200)
    print bigrams
    return dict([(ngram, True) for ngram in itertools.chain(words, bigrams)])

 
feature_train_set = [(tweet_features(tweet), c) for (tweet, c) in train_set]
classifier = NaiveBayesClassifier.train(feature_train_set)
feature_test_set = [(tweet_features(tweet), c) for (tweet, c) in test_set]
print "Accuracy: {}".format(classify.accuracy(classifier, feature_test_set))
classifier.show_most_informative_features(5)

refsets = collections.defaultdict(set)
testsets = collections.defaultdict(set)

for i, item in enumerate(test_set):
    tweet = item[0]
    label = item[1]
    refsets[label].add(i)
    observed = classifier.classify(tweet_features(tweet))
    testsets[observed].add(i)


print refsets
print testsets
print 'pos precision:', precision(refsets['pos'], testsets['pos'])
print 'pos recall:', recall(refsets['pos'], testsets['pos'])
print 'pos F-measure:', f_measure(refsets['pos'], testsets['pos'])
print 'neg precision:', precision(refsets['neg'], testsets['neg'])
print 'neg recall:', recall(refsets['neg'], testsets['neg'])
print 'neg F-measure:', f_measure(refsets['neg'], testsets['neg'])
