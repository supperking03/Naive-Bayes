class Category:

    def __init__(self, categoryName):
        self._categoryName = categoryName
        # dictionary: key la word, value la so lan xuat hien
        self.N=0
        self._words = {}
        self._numberOfSentence=0

    def getNumberOfSentence(self):
        return self._numberOfSentence

    def setNumberOfSentence(self,value):
        self._numberOfSentence=value

    def getName(self):
        return  self._categoryName

    def setValueN(selfs,value):
        N=value

    def getWordsLen(self):
        return len(self._words)

    def getWords(self):
        return self._words

    def getValueN(self):
        return self.N

    def add_words(self, word):
        if (word in self._words.keys()):
            self._words.update({word: self._words[word] + 1})
        else:
            self._words.update({word:1})

