import unittest
class Anagram(object):

    def __init__(self, line_string):
        self.line_string = line_string

    def list_word(self):
        self.list_words = self.line_string.split()
        self.list_result = self.list_result_anagram(self.list_words)
        self.line_result = self.line_result_anagram(self.list_result)
        self.get_result()
        return self.line_result

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

class MyListTests(unittest.TestCase):

    def setUp(self):
        self.obj_1 = Anagram('a1bcd efg!h')
        self.obj_2 = Anagram('a')
        self.obj_3 = Anagram('qwerty abcd zxcvb')
        self.obj_4 = Anagram('!abcd! we wtyu45%$ rwp3@#$% 95a9b54')
        self.obj_5 = Anagram('{a}+[b]+[a2!56rte] ___A___#___2qwerty 5rfv`><hgtrd')

    def test_normal(self):
        self.assertEqual(Anagram.list_word(self.obj_1), 'd1cba hgf!e')

    def test_single(self):
        self.assertEqual(Anagram.list_word(self.obj_2), 'a')

    def test_words(self):
        self.assertEqual(Anagram.list_word(self.obj_3), 'ytrewq dcba bvcxz')

    def test_multi(self):
        self.assertEqual(Anagram.list_word(self.obj_4), '!dcba! ew uytw45%$ pwr3@#$% 95b9a54')

    def test_symbol(self):
        self.assertEqual(Anagram.list_word(self.obj_5), '{e}+[t]+[r2!56aba] ___y___#___2trewqA 5drt`><ghvfr')


if __name__ == '__main__':
    unittest.main()