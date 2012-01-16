Historia
--------

16-01-2012 - 0.4.8
++++++++++++++++++
Przyspieszyłem działanie algorytmu w metodzie "Zakładki alfabetyczne". Jest teraz naprawdę szybki.

15-01-2012 - 0.4.7
++++++++++++++++++
Naprawiłem błąd w metodzie "Zakładki alfabetyczne", który rzucał błąd, jeżeli nie znalazł jakiegoś wyrazu zaczynającego się od danej litery.

12-01-2012 - 0.4.6
++++++++++++++++++
Dostępna jest nowa metoda: Zakładki alfabetyczne.

10-01-2012 - 0.4.5
++++++++++++++++++
Kilka zmian w kodzie nie wpływających znacznie na działanie programu.

8-01-2012 - 0.4.4
+++++++++++++++++
Historia oraz opis programu są teraz w osobnych plikach. Powinny być teraz bardziej przejrzyste.

5-01-2012 - 0.4.3
+++++++++++++++++
Mała zmiana przy odczytywaniu oraz zapisywaniu pliku. Dodałem również kilka nowych słów.

2-01-2012 - 0.4.1
+++++++++++++++++
Wprowadziłem małą poprawkę. Metoda zwrocZakres klasy ListaLiczb nie zawiera teraz warunków if.
Zamiast tego tworzy w momencie wywołania klasy słownik z którego funkcja korzysta. Dzięki temu program wykonuje się szybciej.

1-01-2012 - 0.4
+++++++++++++++
Nowy rok i co? Nowa wersja oznaczona numerem 0.4! Leczyłem dzisiaj kaca po sylwestrze i nic mi się nie chciało robić.
Miałem się położyć wcześniej spać dzisiaj, ale postanowiłem, że dodam nową funkcjonalność do programu i oto jest.
Program od dzisiaj potrafi również generować randomowe liczby o zadanej przez użytkownika długośći. Więcej w pomocy. (python pamiec.py POMOC)

9-12-2011 - 0.3
+++++++++++++++
Całkowicie nowa wersja oznaczona numerem 0.3!
Jest jedna klasa "Slownik", która posiada 5 metod.
zaladuj_slownik - odpowiada za wczytanie pliku "slowa.txt" i przekazaniu słów do "słownika pythonowego" po wywołaniu klasy "Slownik".
dodaj - dodaje słowa do "pythonowego słownika".
zapisz_slownik - zapisuje "pythonowy słownik" do pliku "slowa.txt".
_or - wyświetla słowa do metod "Zakładki obrazkowe" lub "Rymowanki liczbowe". Zależy jak zinterpretuje to użytkownik.
lms - wyświetla słowa do metody "Łańcuchowa metoda skojarzeń".

14-11-2011 - 0.2.8
++++++++++++++++++
Lekka zmiana od strony technicznej.
Możesz teraz dodawać słowa oraz wyświetlić dodane słowa od razu.
Nie musisz ponownie odpalać skryptu.
Jest tylko jeden warunek. Aby wy świetlić dodane słowa, komenda dodawania musi poprzedzać komendę losowania.
Logiczne, ale wiadomo jak to czasami jest :)

Przykład: python pamiec.py -d 'wrona,sroka,dupa,biskup' -l 15
Dodamy do pliku te cztery słowa po czym wylosujemy 15 różnych słów z pliku (wraz z tymi, które dodaliśmy).
Wcześniej to nie przechodziło ponieważ ładowałem słownik przy odpalaniu skryptu.
Natomiast teraz ładuje się osobno przy dodawaniu i osobno przy losowaniu.

09-11-2011 0.2.5
++++++++++++++++
Przepraszam za małe niedopatrzenie. Był błąd podczas dodawania słów do pliku. W zasadzie to bardziej z przechwytywaniem komendy "-d".
Podczas gdy komenda "--dodaj" działała, "-d" nie działała z tego względu, iż przy ifie, zamiast szukać "-d", prze pomyłkę wpisałem "d" zamiast "-d".
Naprawione. Zauważyłem to gdy dodałem dośc sporą liczbę słów i nic się nie działo.
Myślałem, że coś, ze ścieżką do pliku się stało albo błąd w funkcji jest, a to taki mały psikus się okazał. Dodatkowo dorzucam garść nowych słów. Cześć!

07-11-2011 - 0.2.5
++++++++++++++++++
Mała, nieistotna zmiana.

30-10-2011 - 0.2.4
++++++++++++++++++
Zmieniłem sposób wyświetlania napisów. Jest teraz bardziej przyjemny.

26-10-2011 - 0.2.3
++++++++++++++++++
Zmieniłem sposób przechwytywania poleceń oraz rozbudowałem trochę helpa.

21-10-2011 - 0.2.1
++++++++++++++++++
Dodałem nowe słowa. Pojawiła się nowa instrukcja if. Jeżeli użytkownik poda za dużą ilość słów do losowania, zostanie o tym poinformowany i w zamian za to, zostanie wyświetlony cały słownik.

20-10-2011 - 0.2.0
++++++++++++++++++
Hehe. Teraz to nabroiłem! Wywaliłem w cholerę całe GUI. Wszystko jest obsługiwane z lini poleceń.
Trochę się napracowałem jeżeli chodzi o kodowanie znaków... Ale jest już to rozwiązane.

18-10-2011 - 0.1.5
++++++++++++++++++
Zmieniłem uruchamianie. Teraz program odpala się z QMainWindow, a nie jak wcześniej z QDialog. Dodałem również ikonki i menu :)
