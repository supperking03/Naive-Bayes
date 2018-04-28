from core.category import Category


def get_words(sentence):
    return sentence.split()


class BayesianTextClassifier:
    def __init__(self):
        self._categories = {}
        self._stopWords = []
        self._alpha = 1
        self._sumLine = 1
        self._words = []

    def setSumLine(selfs, value):
        selfs._sumLine = value

    def setAlpha(self, value):
        _alpha = value

    def add_stop_words(self, stopWord):
        self._stopWords.append(stopWord)

    def preprocess_sentence(self, sentence):
        list = ["(", ",", ".", ")", "!", "\"", "[", "]", ";", ":","-","*","?","<",">", "&lt",
                "&gt", "&quot", "&", "/", "\n"]

        for str in list:
            sentence = sentence.replace(str, " ")

        sentence_words = sentence.split()

        result = [word for word in sentence_words if word.lower() not in self._stopWords]
        result = ' '.join(result)
        print("result :",result)
        return result.lower()

    def add_sentence(self, sentence, categoryName):
        sentence = self.preprocess_sentence(sentence)

        category = self._categories.get(categoryName)

        if category is None:
            category = Category(categoryName)
            for word in get_words(sentence):
                category.add_words(word)
                if word not in self._words:
                    self._words.append(word)
            self._categories[categoryName] = category
            category.setValueN(len(get_words(sentence)))
            category.setNumberOfSentence(1)
        else:
            for word in get_words(sentence):
                category.add_words(word)
                if word not in self._words:
                    self._words.append(word)
            category.setValueN(len(get_words(sentence)) + category.getValueN())
            category.setNumberOfSentence(category.getNumberOfSentence()+1)

    def classify(self, sentence):
        sentence = self.preprocess_sentence(sentence)
        max_p=0
        max_category = None

        for category_name, each_category in self._categories.items():
            P = 1
            for word in get_words(sentence):
                theta = 1
                keys = each_category.getWords().keys()
                if (word not in keys):
                    x=0
                else:
                    x = each_category.getWords()[word]
                N = each_category.getValueN()
                theta = (x + self._alpha) / float(N + self._alpha * len(self._words))
                P *= theta
            Pcate = each_category.getNumberOfSentence() / float(self._sumLine)
            P = P * Pcate
            if P > max_p:
                max_category = category_name
                max_p = P
        return max_category
