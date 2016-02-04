from textblob.classifiers import NaiveBayesClassifier


SPANISH = 'spanish'
ENGLISH = 'english'
SAMPLE_TRAIN = [
    ("amor", SPANISH),
    ("perro", SPANISH),
    ("playa", SPANISH),
    ("sal", SPANISH),
    ("oceano", SPANISH),
    ("love", ENGLISH),
    ("dog", ENGLISH),
    ("beach", ENGLISH),
    ("salt", ENGLISH),
    ("ocean", ENGLISH)
]

SAMPLE_TEST = [
    ("ropa", SPANISH),
    ("comprar", SPANISH),
    ("camisa", SPANISH),
    ("agua", SPANISH),
    ("telefono", SPANISH),
    ("clothes", ENGLISH),
    ("buy", ENGLISH),
    ("shirt", ENGLISH),
    ("water", ENGLISH),
    ("telephone", ENGLISH)
]

class FeatureExtractors(object):
    
    def last_word_extractor(word):
        feats = {}
        last_letter = word[-1]
        feats["last_letter"] = last_letter
        return feats

class LanguageDetector(object):
    def __init__(self, train=SAMPLE_TRAIN, feature_extractor=FeatureExtractors.last_word_extractor()):
        self.train = train
        self.classifier = NaiveBayesClassifier(self.train, feature_extractor)
    
    def accuracy(self, test_set=SAMPLE_TEST):
        return self.classifier.accuracy(test_set)

    def show_features(self):
        return self.classifier.show_informative_features(5)

