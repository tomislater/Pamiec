Pamięć: Program do ćwiczenia pamięci.
=====================================

**Pamięć** jest programem przeznaczonym do ćwiczenia pamięci długotrwałej jak i zarówno krótkotrwałej.
Program został stworzony z potrzeby samodoskonalenia się.


Pamięć długotrwała:
-------------------
- ŁMS (Łańcuchowa metoda skojarzeń)
- Zakładki obrazkowe
- Rymowanki liczbowe


ŁMS wywołuje się osobno, natomiast 2 i 3 metodę wywołuje się razem.
Tak postanowiłem ponieważ w 2 i 3 metodzie korzysta się z liczb, a bezsensu je wywoływać osobnymi poleceniami.


Pamięć krótkotrwała:
--------------------
- Wyświetlanie losowych liczb


Przykłady:
----------

Korzystanie z ŁMS (Łańcuchowa metoda skojarzeń). ::

    python pamiec.py LMS <liczba>
    python pamiec.py LMS 10
    
    | ------------------- |
    | płatki
    | głos
    | muchomor
    | mina
    | matematyka
    | ogródek
    | forex
    | cyklop
    | wschód
    | piłka
    | ------------------- |

Korzystanie z zakładek obrazkowych oraz rymowanek liczbowych. ::

    python pamiec.py OR <liczba>
    python pamiec.py OR 5
    
    | ------------------- |
    | 1   atlas
    | 2   papier
    | 3   horyzont
    | 4   artykuł
    | 5   gałąź
    | ------------------- |

Wyświetlanie losowych liczb (pamięć krótkotrwała). ::

    python pamiec.py LICZBY <liczbaIlosc> <liczbaDlugosc>
    python pamiec.py LICZBY 5 9
    
    555764831
    
    830254494
    
    862802343
    
    545794040
    
    576921441
    
Dodawanie słów. ::

    python pamiec.py DODAJ <slowa>
    python pamiec.py DODAJ 'wierzba,okoń,dłoń,most'

Pomoc. ::

    python pamiec.py POMOC


Wymagania:
----------
- Python 2.6

Historia:
---------
Historia zmian (wraz z datą i numerem wersji) dostępna jest tutaj_.
.. _tutaj: https://github.com/tomislater/Pamiec/blob/master/HISTORY.rst