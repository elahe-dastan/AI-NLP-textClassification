import re
from Model import Model


class Train:
    def __init__(self, train_corpus):
        self.titles = []
        self.train_corpus_file_name = train_corpus + ".txt"
        f = open(self.train_corpus_file_name, "r")
        self.corpus = f.read()
        f.close()

    def group_titles(self):
        global file_name
        titles_with_bug = set(re.findall(r'\b(\w+رررررررررر)\b', self.corpus))
        # there will be a bug with title adab va honar
        # fix the bug in an ugly way just for now
        titles = []
        for t in titles_with_bug:
            if t == "هنررررررررررر":
                t = "ادب و هنررررررررررر"
            titles.append(t)

        for title in titles:
            file_name = title + ".txt"
            f = open(file_name, "w+")
            f.close()

        f = open(self.train_corpus_file_name, "r")
        for line in f:
            #honar has a bug
            for title in titles:
                if line.startswith(title):
                    file_name = title + ".txt"
            g = open(file_name, "a+")
            g.write(line)
            g.close()
        f.close()
        self.titles = titles

    def model_per_class(self):
        models = {}
        for title in self.titles:
            model = Model(title)
            models[title] = model.model()
        return models
