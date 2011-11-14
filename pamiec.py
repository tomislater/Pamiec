#!/usr/bin/env python -tt
# -*- coding: utf-8 -*-
'''
@author: tomislater@gmail.com
'''
import codecs, os, random, getopt
__version__ = '0.2.8'

class Pamiec(object):
  def __init__(self, argv): 
    try:
      opts, args = getopt.getopt(argv, 'pl:d:w', ['pomoc', 'losuj=', 'dodaj=', 'wersja'])
    except getopt.GetoptError:
      self.pomoc()
      sys.exit()

    for opt, arg in opts:
      if opt in ('-p', '--pomoc'):
        self.pomoc()
      elif opt in ('-d', '--dodaj'):
        self.zaladuj_slownik()
        self.dodaj(arg)
      elif opt in ('-l', '--losuj'):
        try:
          self.zaladuj_slownik()
          self.losuj(int(arg))
        except ValueError:
          print '\nMusisz podać liczbę!\n'
      elif opt in ('--wersja', '-w'):
        print 'Wersja programu:'.rjust(23), __version__, '\n'
  
  
  def zaladuj_slownik(self):
    try:
      self.slownik = {}
      for slowo in codecs.open(os.path.abspath(__file__)[:os.path.abspath(__file__).rfind('/')+1] + 'slowa.txt', encoding='utf-8'):
        self.slownik[slowo[:-1]] = ''
    except IOError:
      print u'Prawdopodobnie nie robisz tego tak jak trzeba. Uruchom program z lini poleceń.'
      
  
  def zapisz_slownik(self):
    slownik = codecs.open(os.path.abspath(__file__)[:os.path.abspath(__file__).rfind('/')+1] + 'slowa.txt', 'w', encoding='utf-8')
    for slowo in self.slownik:
      slownik.write('%s\n' % slowo)
    slownik.close()
      
  
  def losuj(self, liczba_slow):
    import copy
    slownikKopia = copy.copy(self.slownik) 
    try:
      print '\n|', '-'*23, '|'
      for liczbaSlowa in xrange(liczba_slow):
        slowo = random.choice(slownikKopia.keys())
        print '|'.ljust(1), str(liczbaSlowa+1).ljust(3), slowo
        del slownikKopia[slowo]
      print '|', '-'*23, '|\n'
    except IndexError:
      print '|', '-'*23, '|'
      print '\nSprawdź, plik. Najprawdopodobniej, nie ma w nim tyle słów.\nWyświetliłem ile dało radę.\n'

  
  def dodaj(self, slowa):
    slowa = slowa.split(',')
    for slowo in slowa:
      if slowo != '' and len(slowo) > 1:
        self.slownik[codecs.decode(slowo, 'utf-8')] = ''
    self.zapisz_slownik()
  
  
  def pomoc(self):
    print u"""\nDostępne polecenia:
    -l lub --losuj
              losuje podaną liczbę słów
              -l 30 ----- losuje 30 liczb
              --losuj 20 ----- losuje 20 liczb
    -d lub --dodaj
              dodaje podane słowa
              -d 'mistyfikacja,dupa,biskup' ----- dodaje podane słowa
              --dodaj 'płyta,ptaszek,bazylia' ----- również dodaje podane słowa
                        Uwaga! Pamiętaj, aby rozdzielać słowa przecinkami.
    -p lub --pomoc
              pomoc :)
    -w lub --wersja
              wyświetla numer aktualnej wersji\n"""
              
              

if __name__ == '__main__':
  import sys
  Pamiec(sys.argv[1:])
