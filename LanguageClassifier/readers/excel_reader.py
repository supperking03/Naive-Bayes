from core.bayesian_classifier import BayesianTextClassifier
from readers.stopwords_reader import read_stop_words_from_file

import xlrd


def read_sentences_from_file_for_train(train_file, stopwords_file):
    classifier = BayesianTextClassifier()

    for stopword in read_stop_words_from_file(stopwords_file):
        classifier.add_stop_words(stopword)

    workbook = xlrd.open_workbook(train_file)
    sheet = workbook.sheet_by_index(0)

    i = 0
    for row in range(sheet.nrows):
        i+=1
        classifier.add_sentence(sheet.cell_value(row, 0), sheet.cell_value(row, 1))

    classifier.setSumLine(i)

    return classifier


def read_sentences_from_file_for_test(test_file):
    test_set = {}

    workbook = xlrd.open_workbook(test_file)
    sheet = workbook.sheet_by_index(0)

    for row in range(sheet.nrows):
        test_set.update({sheet.cell_value(row, 0): sheet.cell_value(row, 1)})

    return test_set
