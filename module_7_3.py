class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    #  создание словаря из  файлов: ключ - имя файла, значение - слова из файла,
    #  а также нижний регистр, пунктуация, разбиение строк на слова
    def get_all_words(self):
        all_words = {}
        punkt = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                value_dict = file.read().lower()
                for i in punkt:
                    value_dict = value_dict.replace(i, '')
                value_dict = value_dict.split()
                all_words[file_name] = value_dict
        return all_words

    # создание нового словаря на основе all_words
    # ключ - тот же, значение - номер места (позиция) искомого слова
    def find(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        all_words_2 = {}
        for key, value in all_words.items():
            if word in value:
                position = value.index(word)+1
                all_words_2[key] = position
        return all_words_2

    # создание нового словаря на основе all_words
    # ключ - тот же, значение - количество искомого слова в файле
    def count(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        all_words_3 = {}
        for key, value in all_words.items():
            count = value.count(word)
            if count > 0:
                all_words_3[key] = count
        return all_words_3


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего






