#!/usr/bin/env python -tt
# -*- coding: utf-8 -*-
'''
Wyswietla randomowo 20 slow pobranych z pliku, elo. Do nauki pamieci jou.

@author: swiety
'''

import random, codecs, sys, os, platform
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import qrc_resources

__version__ = '0.1.5'

class MainWindow(QMainWindow):
  def __init__(self, parent=None):
    super(MainWindow, self).__init__(parent)
        
    self.stworz_slownik()

    # pole do wpisywania slow
    zakres = QRegExp(u"[a-zA-ZęóąśłżźćńĘÓĄŚŁŻŹĆŃ,]*")
    self.wprowadz = QLineEdit()
    self.wprowadz.setValidator(QRegExpValidator(zakres, self))
      
    # toolbar
    toolbar = self.addToolBar(u'Głowne opcje')
    toolbar.setObjectName('gora')
    toolbar.setMovable(False)
    toolbar.addWidget(self.wprowadz)
        
    # akcje
    dodajAction = self.createAction('Dodaj', self.dodaj, None, 'dodaj', u'Dodaj nowe słowa!')
    losujAction = self.createAction('Losuj', self.losuj, 'Ctrl+L', 'losuj', 'Losuj!')
    closeAction = self.createAction('Zamknij', self.close, 'Ctrl+Q', 'zamknij', 'Zamknij')
    helpAboutAction = self.createAction('O programie', self.about, None, 'about', 'O programie')
    self.addActions(toolbar, (dodajAction, None, losujAction, None, closeAction))
        
    # menu
    fileMenu = self.menuBar().addMenu('Plik')
    helpMenu = self.menuBar().addMenu('Pomoc')
    self.addActions(helpMenu, (helpAboutAction,))
    self.addActions(fileMenu, (dodajAction, losujAction, None, closeAction))
        
    # glowny tekst
    self.tekst = QLabel()
    self.tekst.setMinimumSize(400, 400)
    self.tekst.setAlignment(Qt.AlignJustify)
    self.setCentralWidget(self.tekst)
      
    # status bar
    status = self.statusBar()
    status.setSizeGripEnabled(False)
    status.showMessage(u'Gotów! Losuj albo dodaj nowe słowa.', 5000)
     
    self.setWindowTitle(u'Ćwiczenie pamięci')
     
    settings = QSettings()
    self.restoreGeometry(settings.value("MainWindow/Geometry").toByteArray())
        
        
  def createAction(self, text, slot=None, shortcut=None, icon=None, tip=None, checkable=False, signal="triggered()"):
    action = QAction(text, self)
    if icon is not None:
      action.setIcon(QIcon(":/{0}.png".format(icon)))
    if shortcut is not None:
      action.setShortcut(shortcut)
    if tip is not None:
      action.setToolTip(tip)
      action.setStatusTip(tip)
    if slot is not None:
      self.connect(action, SIGNAL(signal), slot)
    if checkable:
      action.setCheckable(True)
    return action
    
  def addActions(self, target, actions):
    for action in actions:
      if action is None:
        target.addSeparator()
      else:
        target.addAction(action)
    
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
    slownik_losuj = self.slownik.copy()
    tablica = []
    for x in xrange(20):
      slowo = random.choice(slownik_losuj.keys())
      tablica.append(slowo)
      del slownik_losuj[slowo]
    self.pokaz(tablica)
                
                
  def pokaz(self, tablica):
    wylosowane_slowa = '\n\n'
    for liczba, slowo in enumerate(tablica):
      if liczba < 9:
        wylosowane_slowa += ''.ljust(40) + str(liczba+1) + " ----- " + slowo + "\n"
      else:
        wylosowane_slowa += ''.ljust(40) + str(liczba+1) + " --- " + slowo + "\n"
    self.tekst.setText(wylosowane_slowa[:-1])
    
    
  def dodaj(self):
    pobrane_slowa = self.wprowadz.text().split(",")
    for slowo in pobrane_slowa:
      if slowo != '':
        self.slownik[slowo] = ''
                
    self.zapisz_plik()
    self.wprowadz.clear()
    self.wprowadz.setFocus()
    
  def closeEvent(self, event):
    settings = QSettings()
    settings.setValue("MainWindow/Geometry", self.saveGeometry())
    
  def about(self):
    QMessageBox.about(self, "O programie",
                      u"""<b>Program do ćwiczenia pamięci. <p>Wersja {0}</p></b>
                      <p>Python {1} - Qt {2} - PyQt {3} na systemie {4}""".format(__version__, platform.python_version(),
                                                                                  QT_VERSION_STR, PYQT_VERSION_STR, platform.system()))
        
if __name__ == "__main__":
  app = QApplication(sys.argv)
  app.setOrganizationName('swiety')
  app.setOrganizationDomain('swiety.tumblr.com')
  app.setApplicationName(u'Program do ćwiczenia pamięci')
  form = MainWindow()
  form.show()
  app.exec_()