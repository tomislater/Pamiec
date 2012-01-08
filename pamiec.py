# -*- coding: utf-8 -*-
__author__ =  'tomislater@gmail.com'
import codecs, os, random, sys
__version__ = '0.4.4'



class Slownik(object):
  """
  Tworzy słownik w którym przechowywane są słowa.
  """

  def __init__(self):
    """
    Wywołuje ładowanie słownik do 'słownika pythonowego'.
    """
    self.zaladuj_slownik()

  def zaladuj_slownik(self):
    """
    Ładuje słownik do 'słownika pythonowego'.
    """
    self.slownik = {}
    try:
      for slowo in codecs.open(os.path.join(os.path.dirname(__file__), 'slowa.txt'), encoding='utf-8'):
        self.slownik[slowo[:-1]] = ''
    except IOError:
      print u'Program nie znalazł pliku słownika. Sprawdź nazwę słownika. Poprawna nazwa to "slowa.txt". Jeżeli go nie ma, to go stwórz.\n'
      pomoc()
      sys.exit(2)

  def dodaj(self, slowa):
    """
    Dodaje słowa przechwycone z lini poleceń do 'słownika pythonowego.'
    """
    slowa = slowa.split(',')
    for slowo in slowa:
      if slowo != '' and len(slowo) > 1:
        self.slownik[codecs.decode(slowo, 'utf-8')] = ''
    self.zapisz_slownik()

  def zapisz_slownik(self):
    """
    Zapisuje 'pythonowy słownik' do pliku
    """
    slownik = codecs.open(os.path.join(os.path.dirname(__file__), 'slowa.txt'), 'w', encoding='utf-8')
    for slowo in self.slownik:
      slownik.write('%s\n' % slowo)

  def _or(self, liczba_slow):
    """
    Odpowiada za wyświetlanie metod:
      - zakładki obrazkowe
      - rymowanki liczbowe
    """
    slownikKopia = self.stworzKopieSlownika()
    try:
      print '\n|', '-'*19, '|'
      for liczbaSlowa in xrange(liczba_slow):
        slowo = random.choice(slownikKopia.keys())
        print '|'.ljust(1), str(liczbaSlowa+1).ljust(3), slowo
        del slownikKopia[slowo]
      print '|', '-'*19, '|\n'
    except IndexError:
      self.wyswietlBladIndexError()

  def lms(self, liczba_slow):
    """
    Odpowiada za wyświetlenie metody 'Łańcuhowa metoda skojarzeń'.
    """
    slownikKopia = self.stworzKopieSlownika()
    try:
      print '\n|', '-'*19, '|'
      for liczba in xrange(liczba_slow):
        slowo = random.choice(slownikKopia.keys())
        print '|'.ljust(1), slowo
        del slownikKopia[slowo]
      print '|', '-'*19, '|\n'
    except IndexError:
      self.wyswietlBladIndexError()

  def stworzKopieSlownika(self):
    """
    Tworzy kopię słownika.
    """
    import copy
    slownikKopia = copy.copy(self.slownik)
    return slownikKopia

  def wyswietlBladIndexError(self):
    """
    Wyświetla błąd związany z podaniem zbyt dużego zakresu co do ilości słów do wyświetlenia.
    """
    print '|', '-'*19, '|'
    print '\nSprawdź, plik. Najprawdopodobniej, nie ma w nim tyle słów.\nWyświetliłem ile dało radę.\n'



class ListaLiczb(object):
  """
  Klasa odpowiadająca utworzenie i wyświetlenie listy liczb.
  """
  _listaLiczb = []
  slownikDlugosci = {3: (100, 999), 4: (1000, 9999), 5: (10000, 99999), 6: (100000, 999999), 7: (1000000, 9999999),
                     8: (10000000, 99999999), 9: (100000000, 999999999),}

  def __init__(self, ilosc, dlugosc):
    zakres = self.zwrocZakres(dlugosc)
    self.ilosc = ilosc
    self.stworzRandomy(zakres)
    self.wyswietl()

  def zwrocZakres(self, dlugosc):
    """
    Zwraca zakres liczb jakie mają być brane pod uwagę. Zamiast pisania ifów dane są umieszczone w słowniku.
    Dostęp do danych odbywa się po kluczu, który podał użytkownik.
    """
    try:
      return self.slownikDlugosci[dlugosc]
    except KeyError:
      print >>sys.stderr, 'Liczba długości musi mieścić się w przedziale <3;9>.\n'
      pomoc()
      sys.exit(2)

  def stworzRandomy(self, zakres):
    """
    Tworzy randomowe liczby i umieszcza je w liście.
    """
    while self.ilosc:
      rLiczba = random.randint(zakres[0], zakres[1])
      if rLiczba not in self._listaLiczb:
        self._listaLiczb.append(rLiczba)
      self.ilosc -= 1

  def wyswietl(self):
    """
    Wyświetla liczby.
    """
    for liczba in self._listaLiczb:
      print "\n    {0}".format(liczba)
    print



def pomoc():
  """
  Wyświetla pomoc.
  """
  print """Dostępne polecenia:
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
  if len(sys.argv) == 4 and sys.argv[1] == 'LICZBY':
    try:
      ilosc = int(sys.argv[2])
      dlugosc = int(sys.argv[3])
      if ilosc == 0:
        print >>sys.stderr, 'Argument ilość powinien wynosić więcej niż 0...\n'
        pomoc()
        sys.exit(2)
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