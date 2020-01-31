from Model import Model


def write_to_file(file_name, mode, data):
    f = open(file_name, mode)
    f.write(data)
    f.close()


class Train:
    def __init__(self, train_corpus):
        self.titles = []
        train_corpus_file_name = train_corpus + ".txt"
        f = open(train_corpus_file_name, mode="r", encoding='utf-8-sig')
        self.corpus = f.read()
        f.close()

    def group_titles(self):
        global file_name
        different_texts = self.corpus.split('\n')
        titles = []
        for text in different_texts:
            title, data = text.split("@@@@@@@@@@ ")
            file_name = title + ".txt"
            if title in titles:
                write_to_file(file_name, "a+", data)
            else:
                write_to_file(file_name, "w+", data)
                titles.append(title)
        self.titles = titles

    def model_per_class(self):
        models = {}
        for title in self.titles:
            model = Model(title)
            models[title] = model.model()
        return models
