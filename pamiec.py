#!/usr/bin/env python -tt
# -*- coding: utf-8 -*-
'''
Wyświetla randomowo słowa pobrane z pliku. Do nauki pamięci.

Możesz podać ile słów ma wyświetlić. Domyślnie jest to liczba 20.

@author: swiety
'''
import codecs, os, random
__version__ = '0.2.0'

class Pamiec(object):
  
  def __init__(self, args):
    try:
      self.zaladuj_slownik()
    except IOError:
      print u'Prawdopodobnie nie robisz tego tak jak trzeba. Uruchom program z lini poleceń.'
    
    try:
      self.funkcja = args[0]
      
      if self.funkcja == 'losuj':
        try:
          self.wartosc = int(args[1])
        except IndexError:
          self.wartosc = 20
        self.losuj(self.wartosc)
        
      elif self.funkcja == 'dodaj':
        try:
          self.wartosc = args[1]
          self.dodaj(self.wartosc)
        except IndexError:
          print u'\nNie podałeś żadnych słów.'
          self.pomoc()
      
      elif self.funkcja == 'pomoc':
        self.pomoc()
      
      elif self.funkcja == 'wersja':
        print '\nWersja:', __version__, '\n'
          
      else:
        print u'\nNieznana komenda.'
        self.pomoc()
    except IndexError:
      print u'\nNie podałeś żadnej komendy'
      self.pomoc()
  
  
  def zaladuj_slownik(self):
    self.slownik = {}
    for slowo in codecs.open(os.path.dirname(__file__) + 'slowa.txt', encoding='utf-8'):
      self.slownik[slowo[:-1]] = ''
  
  
  def zapisz_slownik(self):
    slownik = codecs.open(os.path.dirname(__file__) + 'slowa.txt', 'w', encoding='utf-8')
    for slowo in self.slownik:
      slownik.write('%s\n' % slowo)
    slownik.close()
      
  
  def losuj(self, liczba_slow):
    try:
      print '\n|', '-'*23, '|'
      for x in xrange(liczba_slow):
        slowo = random.choice(self.slownik.keys())
        print str(x+1).ljust(3), slowo
        del self.slownik[slowo]
      print '|', '-'*23, '|\n'
    except IndexError:
      print '\nSprawdź, plik. Najprawdopodobniej, nie ma w nim tyle słów.\nWyświetliłem ile dało radę.\n'

  
  def dodaj(self, slowa):
    slowa = slowa.split(',')
    for slowo in slowa:
      if slowo != '' and len(slowo) > 1:
        self.slownik[codecs.decode(slowo, 'utf-8')] = ''
    self.zapisz_slownik()
  
  
  def pomoc(self):
    print u"""\nDostępne polecenia:
    1. losuj liczba
    2. dodaj "słowa,jakieś,tam"
    -----------------------
    -----------------------
    Przykład:
    python pamiec.py losuj 30 - losuje 30 słów. Jeżeli nie podasz liczby, domyślnie wyświetli 20 wyrazów.
    python pamiec.py dodaj "cześć,witam,rower,deskorolka,pompka" - dodaje słowa.
    
    Uwaga! Pamiętaj, aby rozdzielać słowa przecinkami.\n\n"""

if __name__ == '__main__':
  import sys
  Pamiec(sys.argv[1:])