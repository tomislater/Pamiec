# -*- coding: utf-8 -*-

__author__ =  'tomislater@gmail.com'

import codecs, os, random, sys
__version__ = '0.4'

class Slownik(object):
  u"""Tworzy słownik w którym przechowywane są słowa."""
  def __init__(self):
    u"""Wywołuje ładowanie słownik do 'słownika pythonowego'"""
    self.zaladuj_slownik() 


  def zaladuj_slownik(self):
    u"""Ładuje słownik do 'słownika pythonowego'"""
    try:
      self.slownik = {}
      for slowo in codecs.open(os.path.abspath(__file__)[:os.path.abspath(__file__).rfind('/')+1] + 'slowa.txt', encoding='utf-8'):
        self.slownik[slowo[:-1]] = ''
    except IOError:
      print u'Prawdopodobnie nie robisz tego tak jak trzeba. Uruchom program z lini poleceń.'


  def dodaj(self, slowa):
    u"""Dodaje słowa przechwycone z lini poleceń do 'słonika pythonowego'"""
    slowa = slowa.split(',')
    for slowo in slowa:
      if slowo != '' and len(slowo) > 1:
        self.slownik[codecs.decode(slowo, 'utf-8')] = ''
    self.zapisz_slownik()

  
  def zapisz_slownik(self):
    u"""Zapisuje 'pythonowy słownik' do pliku"""
    slownik = codecs.open(os.path.abspath(__file__)[:os.path.abspath(__file__).rfind('/')+1] + 'slowa.txt', 'w', encoding='utf-8')
    for slowo in self.slownik:
      slownik.write('%s\n' % slowo)


  def _or(self, liczba_slow):
    u"""Odpowiada za wyświetlanie metod:
    - zakładki obrazkowe
    - rymowanki liczbowe"""
    import copy
    slownikKopia = copy.copy(self.slownik) 
    try:
      print '\n|', '-'*19, '|'
      for liczbaSlowa in xrange(liczba_slow):
        slowo = random.choice(slownikKopia.keys())
        print '|'.ljust(1), str(liczbaSlowa+1).ljust(3), slowo
        del slownikKopia[slowo]
      print '|', '-'*19, '|\n'
    except IndexError:
      print '|', '-'*19, '|'
      print '\nSprawdź, plik. Najprawdopodobniej, nie ma w nim tyle słów.\nWyświetliłem tyle ile było w pliku.\n'
  
  
  def lms(self, liczba_slow):
    u"""Odpowiada za wyświetlenie metody "Łańcuhowa metoda skojarzeń"""
    import copy
    slownikKopia = copy.copy(self.slownik) 
    try:
      print '\n|', '-'*19, '|'
      for liczba in xrange(liczba_slow):
        slowo = random.choice(slownikKopia.keys())
        print '|'.ljust(1), slowo
        del slownikKopia[slowo]
      print '|', '-'*19, '|\n'
    except IndexError:
      print '|', '-'*19, '|'
      print '\nSprawdź, plik. Najprawdopodobniej, nie ma w nim tyle słów.\nWyświetliłem ile dało radę.\n'



class ListaLiczb(object):
  _listaLiczb = []
  def __init__(self, ilosc, dlugosc):
    zakres = self.zwrocZakres(dlugosc)
    self.ilosc = ilosc
    self.stworzRandomy(zakres)
    self.wyswietl(dlugosc)

  def zwrocZakres(self, dlugosc):
    if dlugosc == 3:
      return (100, 999)
    elif dlugosc == 4:
      return (1000, 9999)
    elif dlugosc == 5:
      return (10000, 99999)
    elif dlugosc == 6:
      return (100000, 999999)
    elif dlugosc == 7:
      return (1000000, 9999999)
    elif dlugosc == 8:
      return (10000000, 99999999)
    elif dlugosc == 9:
      return (100000000, 999999999)
    else:
      print >>sys.stderr, 'Liczba długości musi mieścić się w przedziale <3;9>\n'
      pomoc()
      sys.exit(2)

  def stworzRandomy(self, zakres):
    while self.ilosc:
      rLiczba = random.randint(zakres[0], zakres[1])
      if rLiczba not in self._listaLiczb:
        self._listaLiczb.append(rLiczba)
      self.ilosc -= 1
    return

  def wyswietl(self, dlugosc):
    for liczba in self._listaLiczb:
      print "\n    {0}".format(liczba)
    print



def pomoc():
  u"""Wyświetla pomoc."""
  print u"""Dostępne polecenia:
  python pamiec.py DODAJ 'slowo1,slowo2,slowo3' - dodaje podane słowa
  python pamiec.py LMS <liczba> - wyświetla określoną liczbę słów (Łańcuchowa metoda skojarzeń)
  python pamiec.py OR <liczba> - wyświetla określoną liczbę słów" (Metody: Zakładki obrazkowe oraz rymowanki liczbowe)
  python pamiec.py LICZBY <liczbaIlosc> <liczbaDlugosc> - wyswietla randomowe liczby o zadanej dlugosci
  python pamiec.py POMOC - wyświetla pomoc
  python pamiec.py WERSJA - wyświetla aktualną wersję programu
  
  Przykłady:
  python pamiec.py DODAJ 'dupa,pleb,lumpenproletariat'
  python pamiec.py LMS 10
  python pamiec.py OR 20
  python pamiec.py LICZBY 10 7\n"""
  
  
  
if __name__ == '__main__':
  if len(sys.argv) == 4:
    try:
      ilosc = int(sys.argv[2])
      dlugosc = int(sys.argv[3])
    except ValueError:
      print >>sys.stderr, 'Argumentami muszą być liczby\n'
      pomoc()
      sys.exit(2)
    ListaLiczb(ilosc, dlugosc)
  elif len(sys.argv) == 3:
    if sys.argv[1] == 'DODAJ':
      Slownik().dodaj(sys.argv[2])
    elif sys.argv[1] == 'OR':
      try:
        Slownik()._or(int(sys.argv[2]))
      except ValueError:
        pomoc()
        print 'Argument musi być liczbą.\n'
    elif sys.argv[1] == 'LMS':
      try:
        Slownik().lms(int(sys.argv[2]))
      except ValueError:
        pomoc()
        print 'Argument musi być liczbą.\n'
    else:
      pomoc()
  elif len(sys.argv) == 2:
    if sys.argv[1] == 'POMOC':
      pomoc()
    elif sys.argv[1] == 'WERSJA':
      print 'Wersja programu:', __version__, '\n'
    else:
      pomoc()
  else:
    pomoc()