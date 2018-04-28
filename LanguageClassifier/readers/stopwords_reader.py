def read_stop_words_from_file(file):
    stopword = []
    with open(file, encoding="utf8") as f:
        for line in f:
            stopword.append(line.strip())
    return stopword