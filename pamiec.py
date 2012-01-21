# -*- coding: utf-8 -*-
import os
import sys
import codecs
import random


__version__ = '0.5'
__author__ =  'tomislater@gmail.com'


class DictionaryMain(object):
    """Creates a dictionary in which stores are words."""

    def __init__(self):
        """Invoke loads the dictionary."""
        self.load_dictionary()

    def load_dictionary(self):
        """Loads the dictionary."""
        self.dictionary_ = {}
        try:
            for word in codecs.open(os.path.join(os.path.dirname(__file__), 'slowa.txt'),
                                     encoding='utf-8'):
                self.dictionary_[word[:-1]] = word[0]
        except IOError:
            print 'Program nie znalazł pliku słownika. Sprawdź nazwę słownika. '\
                            'Poprawna nazwa to "slowa.txt". Jeżeli go nie ma, to go stwórz.\n'
            help_()
            sys.exit(2)

    def adds(self, words):
        """Adds words from command line into python dictionary."""
        words = words.split(',')
        for word in words:
            if word != '' and len(word) > 1:
                self.dictionary_[codecs.decode(word, 'utf-8')] = word[0]
        self.save_dictionary()

    def save_dictionary(self):
        """Saves dictionary into a file."""
        dictionary_ = codecs.open(os.path.join(os.path.dirname(__file__), 'slowa.txt'),
                              'w', encoding='utf-8')
        for word in self.dictionary_:
            dictionary_.write('%s\n' % word)

    def alphabetical_bookmarks(self):
        """Displays a method 'Zakładki alfabetyczne'"""
        dictionary_ab = {}
        for tuple_word in self.dictionary_.items():
            if tuple_word[1] in dictionary_ab.keys():
                dictionary_ab[tuple_word[1]] += [tuple_word[0]]
            else:
                dictionary_ab[tuple_word[1]] = [tuple_word[0]]
        print '\n|', '-'*19, '|'
        for letter in u'abcćdefghijklłmnoóprsśtuwzźż':
            try:
                rand_word = random.choice(dictionary_ab[letter])
                print '| ' + letter.upper() + '. ' + rand_word
            except KeyError:
                print '| ' + letter.upper() + '. ' + '-' * 10
        print '|', '-'*19, '|'

    def _or(self, number_thewords):
        """
        Displays a methods:
          - zakładki obrazkowe
          - rymowanki liczbowe
        """
        dictionary_copy = self.create_dict_copy()
        print '\n|', '-'*19, '|'
        try:
            for nr_word in xrange(number_thewords):
                slowo = random.choice(dictionary_copy.keys())
                print '|'.ljust(1), str(nr_word+1).ljust(3), slowo
                del dictionary_copy[slowo]
        except IndexError:
            self.view_index_error()
        else:
            print '|', '-'*19, '|\n'

    def lms(self, number_thewords):
        """Displays the method 'Łańcuhowa metoda skojarzeń'."""
        dictionary_copy = self.create_dict_copy()
        print '\n|', '-'*19, '|'
        try:
            while number_thewords:
                word = random.choice(dictionary_copy.keys())
                print '|'.ljust(1), word
                del dictionary_copy[word]
                number_thewords -= 1
        except IndexError:
            self.view_index_error()
        else:
            print '|', '-'*19, '|\n'

    def create_dict_copy(self):
        """Creates copy of a dictionary."""
        import copy
        return copy.copy(self.dictionary_)

    def view_index_error(self):
        """Displays the error if user input more the number than number the words in file."""
        print '|', '-'*19, '|'
        print '\nSprawdź, plik. Najprawdopodobniej, nie ma w nim tyle słów.\nWyświetliłem ile dało radę.\n'


class ListNumbers(object):
    """Class creates and shows the random numbers."""
    numbers_ = []
    dict_ranges = {3: (100, 999), 4: (1000, 9999), 5: (10000, 99999), 6: (100000, 999999), 7: (1000000, 9999999),
                     8: (10000000, 99999999), 9: (100000000, 999999999),}

    def __init__(self, amount, lenght_):
        scope = self.ret_scope(lenght_)
        self.amount = amount
        self.creates_random(scope)
        self.show_()

    def ret_scope(self, lenght_):
        """Return a scope."""
        try:
            return self.dict_ranges[lenght_]
        except KeyError:
            print >>sys.stderr, 'Liczba długości musi mieścić się w przedziale <3;9>.\n'
            help_()
            sys.exit(2)

    def creates_random(self, scope):
        """Creates the random numbers and puts them into list."""
        while self.amount:
            r_number = random.randint(scope[0], scope[1])
            if r_number not in self.numbers_:
                self.numbers_.append(r_number)
            self.amount -= 1

    def show_(self):
        """Shows a numbers."""
        for nr in self.numbers_:
            print "\n    {0}".format(nr)
        print


def help_():
    """Shows the help."""
    
    print """Dostępne polecenia:
    python pamiec.py DODAJ 'slowo1,slowo2,slowo3' - dodaje podane słowa
    python pamiec.py LMS <liczba> - wyświetla określoną liczbę słów (Łańcuchowa metoda skojarzeń)
    python pamiec.py OR <liczba> - wyświetla określoną liczbę słów" (Metody: Zakładki obrazkowe oraz rymowanki liczbowe)
    python pamiec.py ZA - wyświetla słowa do zakładek alfabetycznych
    python pamiec.py LICZBY <liczbaIlosc> <liczbaDlugosc> - wyswietla randomowe liczby o zadanej dlugosci
    python pamiec.py POMOC - wyświetla help_
    python pamiec.py WERSJA - wyświetla aktualną wersję programu
  
    Przykłady:
    python pamiec.py DODAJ 'dupa,pleb,lumpenproletariat'
    python pamiec.py LMS 10
    python pamiec.py OR 20
    python pamiec.py LICZBY 10 7
    python pamiec.py ZA\n"""
  
  
if __name__ == '__main__':
    if len(sys.argv) == 4 and sys.argv[1] == 'LICZBY':
        try:
            ilosc = int(sys.argv[2])
            dlugosc = int(sys.argv[3])
        except ValueError:
            print >>sys.stderr, 'Argumentami muszą być liczby\n'
            help_()
            sys.exit(2)
        if ilosc == 0:
                print >>sys.stderr, 'Argument ilość powinien wynosić więcej niż 0...\n'
                help_()
                sys.exit(2)
        ListNumbers(ilosc, dlugosc)
    elif len(sys.argv) == 3:
        if sys.argv[1] == 'DODAJ':
            DictionaryMain().adds(sys.argv[2])
        elif sys.argv[1] == 'OR' and sys.argv[2] != '0':
            try:
                DictionaryMain()._or(int(sys.argv[2]))
            except ValueError:
                help_()
                print 'Argument musi być liczbą.\n'
        elif sys.argv[1] == 'LMS':
            try:
                DictionaryMain().lms(int(sys.argv[2]))
            except ValueError:
                help_()
                print 'Argument musi być liczbą.\n'
        else:
            help_()
    elif len(sys.argv) == 2:
        if sys.argv[1] == 'POMOC':
            help_()
        elif sys.argv[1] == 'WERSJA':
            print 'Wersja programu:', __version__, '\n'
        elif sys.argv[1] == 'ZA':
            DictionaryMain().alphabetical_bookmarks()
        else:
            help_()
    else:
        help_()