class Anagram(object):

    def __init__(self, line_string):
        self.line_string = line_string

    def list_word(self):
        self.list_words = self.line_string.split()
        self.list_result = self.list_result_anagram(self.list_words)
        self.line_result = self.line_result_anagram(self.list_result)
        self.get_result()

    def list_result_anagram(self,list_words):
        list_result_anagram = []
        # йдемо по всіх словах списку
        for i in range(len(list_words)):
            anagram_of_words = ''
            only_letters = []

            # Вибираємо тільки букви і вставляємо в список
            for j in range(len(list_words[i])):
                if (ord(list_words[i][j]) > 32 and ord(list_words[i][j]) <= 64) or (
                                ord(list_words[i][j]) >= 91 and ord(list_words[i][j]) <= 96) or (
                                ord(list_words[i][j]) >= 123 and ord(list_words[i][j]) <= 126):
                    continue
                else:
                    only_letters.append(list_words[i][j])

            # робимо реверс створеного списку
            only_letters.reverse()

            # добавляємо спец символи в список
            for k in range(len(list_words[i])):
                if (ord(list_words[i][k]) > 32 and ord(list_words[i][k]) <= 64) or (
                                ord(list_words[i][k]) >= 91 and ord(list_words[i][k]) <= 96) or (
                                ord(list_words[i][k]) >= 123 and ord(list_words[i][k]) <= 126):
                    only_letters.insert(k, list_words[i][k])

            # формуємо слово із елементів реверсованого списку
            for g in range(len(only_letters)):
                anagram_of_words += only_letters[g]

            # добавляємо це слово у список готових слів анаграм
            list_result_anagram.append(anagram_of_words)
        return list_result_anagram

    def line_result_anagram(self,list_result):
        self.result_line = ' '.join(list_result)
        return self.result_line

    def get_result(self):
        print(self.line_result)

