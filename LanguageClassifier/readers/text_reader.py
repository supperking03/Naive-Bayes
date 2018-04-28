from core.bayesian_classifier import BayesianTextClassifier
from readers.stopwords_reader import read_stop_words_from_file


def read_sentences_from_file_for_train(train_file, stopwords_file):
    classifier = BayesianTextClassifier()

    for stopword in read_stop_words_from_file(stopwords_file):
        classifier.add_stop_words(stopword)

    i = 0
    with open(train_file) as f:
        for line in f:
            i += 1
            line = line.strip()

            classifier.add_sentence(line[:len(line) - 3],line[len(line)-1])

    classifier.setSumLine(i)

    return classifier


def read_sentences_from_file_for_test(test_file):
    test_set = {}

    with open(test_file) as f:
        for line in f:
            line = line.strip()
            test_set.update({line[:len(line) - 3]: line[len(line) - 1]})

    return test_set
