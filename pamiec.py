# -*- coding: utf-8 -*-
'''
Wyswietla randomowo 20 slow pobranych z pliku, elo. Do nauki pamieci jou.

@author: swiety
'''

import random, time, codecs, sys, os
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        
        self.stworz_slownik()
               
        zakres = QRegExp(u"[a-zA-ZęóąśłżźćńĘÓĄŚŁŻŹĆŃ,]*")
        
        self.wprowadz = QLineEdit()
        self.wprowadz.setValidator(QRegExpValidator(zakres, self))
        
        guzikiLay = QHBoxLayout()
        for tekst, akcja in (("Dodaj", self.dodaj), ("&Losuj", self.losuj)):
            button = QPushButton(tekst)
            guzikiLay.addWidget(button)
            self.connect(button, SIGNAL("clicked()"), akcja)
            
        self.tekst = QLabel()
        self.tekst.setAlignment(Qt.AlignLeft)
        
        self.czas_wygenerowania = QLabel("Czas wygenerowania:")
        
        layout = QGridLayout()
        layout.addWidget(self.wprowadz, 0, 0)
        layout.addLayout(guzikiLay, 1, 0)
        layout.addWidget(self.tekst, 2, 0)
        layout.addWidget(self.czas_wygenerowania, 3, 0)
        self.setWindowTitle(u"Ćwiczymy pamięć")
        self.setLayout(layout)
        
        
    def stworz_slownik(self):
        self.slownik = {}
        self.slowa = codecs.open(os.path.dirname(__file__) + '/slowa.txt', encoding='utf-8').readlines()
        for slowo in self.slowa:
            self.slownik[slowo[:-1]] = ''
            
            
    def zapisz_plik(self):
        self.slowa = codecs.open(os.path.dirname(__file__) + '/slowa.txt', 'w', encoding='utf-8')
        for slowo in self.slownik:
            self.slowa.write('%s\n' % slowo)
            
            
    def losuj(self):
        czas = time.time()
        slownik_losuj = self.slownik.copy()
        tablica = []
        for x in xrange(20):
            slowo = random.choice(slownik_losuj.keys())
            tablica.append(slowo)
            del slownik_losuj[slowo]
        self.pokaz(tablica, czas)
                
                
    def pokaz(self, tablica, czas):
        wylosowane_slowa = ''
        for liczba, slowo in enumerate(tablica):
            if liczba < 9:
                wylosowane_slowa += str(liczba+1) + " ----- " + slowo + "\n"
            else:
                wylosowane_slowa += str(liczba+1) + " --- " + slowo + "\n"
        self.tekst.setText(wylosowane_slowa[:-1])
        self.czas_wygenerowania.setText("Czas wygenerowania: %0.5f" % (time.time() - czas))
    
    
    def dodaj(self):
        pobrane_slowa = self.wprowadz.text().split(",")
        for slowo in pobrane_slowa:
            if slowo != '':
                self.slownik[slowo] = ''
                
        self.zapisz_plik()
        self.wprowadz.clear()
        self.wprowadz.setFocus()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()