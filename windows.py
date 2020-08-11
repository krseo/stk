# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 09:46:49 2020

@author: krseo
"""
from PyQt5.QtCore import (QFile, QFileInfo, QPoint, QSettings, QSignalMapper,
        QSize, QTextStream, Qt)
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtWidgets import (QAction, QApplication, QFileDialog, QMainWindow,
        QMdiArea, QMessageBox, QTextEdit, QWidget, QDialog)
from PyQt5 import uic

class win001(QDialog):
    def __init__(self, parent=None):
        super(win001, self).__init__(parent)
        uic.loadUi("win001.ui", self)
        width = self.frameGeometry().width()
        height = self.frameGeometry().height()
        self.setFixedSize(width, height)
    sequenceNumber = 1
    
class win002(QDialog):
    def __init__(self, parent=None):
        super(win002, self).__init__(parent)
        uic.loadUi("win002.ui", self)
        #self.app = app
        self.parent = parent
        width = self.frameGeometry().width()
        height = self.frameGeometry().height()
        self.setFixedSize(width, height)
    sequenceNumber = 1