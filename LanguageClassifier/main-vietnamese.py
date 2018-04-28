import sys
import pickle
from readers.excel_reader import read_sentences_from_file_for_train
from readers.excel_reader import read_sentences_from_file_for_test

mode = sys.argv[1]

if mode == "train":
    classifier = read_sentences_from_file_for_train(sys.argv[2], "data/stopwords/vietnamese-stopwords.txt")

    with open(sys.argv[3], 'wb') as output:
        pickle.dump(classifier, output, pickle.HIGHEST_PROTOCOL)

if mode == "run":
    with open(sys.argv[2], 'rb') as input:
        classifier = pickle.load(input)

    print(classifier.classify(sys.argv[3]))

if mode == "test":
    with open(sys.argv[2], 'rb') as input:
        classifier = pickle.load(input)

    test_set = read_sentences_from_file_for_test(sys.argv[3])

    count = 0
    accurateCount = 0

    for sentence, category in test_set.items():
        count += 1
        resultCategory = classifier.classify(sentence)
        print(category, resultCategory)
        if category == resultCategory:
            accurateCount += 1

    print((float(accurateCount) / float(count)) * 100, "%", sep = '')



