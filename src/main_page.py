
import sys
from PyQt4 import QtCore, QtGui, uic
first_page = uic.loadUiType("../ui/first_page.ui")[0]
class MyWindowClass(QtGui.QMainWindow, first_page):
    
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.push_supervised.clicked.connect(self.push_supervised_clicked)  # Bind the event handlers
        self.push_unsupervised.clicked.connect(self.push_unsupervised_clicked)  #   to the buttons

        self.menuHelp.addAction('&About', self.about)  # add About to Help
        self.statusBar().showMessage("Start Page", 10000)
        
    def about(self):
        QtGui.QMessageBox.about(self, "About",
"""                                                Minor Project

Copyright 2015 Arjun P.P. , Mandeep Singh

This is minor project for our undergraduate course in Information Technology. The project demonstrates some Machine Learning algorithms.


The project uses Qt framework along with PyQt 4 plugin to create the UI.
"""
)
    
    def push_supervised_clicked(self):
        self 
        
    def push_unsupervised_clicked(self):
        self 

        
        
    
    

app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.show()
app.exec_()
