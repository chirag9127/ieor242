import nltk
train_set = [
    ('I love this sandwich.', 'pos'),
    ('This is an amazing place!', 'pos'),
    ('I feel very good about these beers.', 'pos'),
    ('This is my best work.', 'pos'),
    ("What an awesome view", 'pos'),
    ('I do not like this restaurant', 'neg'),
    ('I am tired of this stuff.', 'neg'),
    ("I can't deal with this", 'neg'),
    ('He is my sworn enemy!', 'neg'),
    ('My boss is horrible.', 'neg')
]
test_set = [
    ('The beer was good.', 'pos'),
    ('I do not enjoy my job', 'neg'),
    ("I ain't feeling dandy today.", 'neg'),
    ("I feel amazing!", 'pos'),
    ('Gary is a friend of mine.', 'pos'),
    ("I can't believe I'm doing this.", 'neg')
]

train_set_words = []
for item in train_set:
    words = nltk.word_tokenize(item[0])
    for word in words:
        train_set_words.append(word)

all_words = nltk.FreqDist(w.lower() for w in train_set_words)

def tweet_features(tweet):
    tweet_words = tweet.split()
    features = {}
    for word in all_words:
        features['contains({})'.format(word)] = (word in tweet_words)
    return features

 
feature_train_set = [(tweet_features(tweet), c) for (tweet, c) in train_set]
classifier = nltk.NaiveBayesClassifier.train(feature_train_set)
feature_test_set = [(tweet_features(tweet), c) for (tweet, c) in test_set]
print(nltk.classify.accuracy(classifier, feature_test_set))
classifier.show_most_informative_features(5)

