import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *

class Window(QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://www.google.com'))
        self.setCentralWidget(self.browser)

        #-------------------full screen mode------------------
        self.showMaximized()

        #----------------------navbar-------------------------
        navbar = QToolBar()
        self.addToolBar(navbar)

        #-----------------buttons-----------------
        prevBtn = QAction('Prev',self)
        prevBtn.triggered.connect(self.browser.back)
        navbar.addAction(prevBtn)

        nextBtn = QAction('Next',self)
        nextBtn.triggered.connect(self.browser.forward)
        navbar.addAction(nextBtn)

        refreshBtn = QAction('Refresh',self)
        refreshBtn.triggered.connect(self.browser.reload)
        navbar.addAction(refreshBtn)

        homeBtn = QAction('Home',self)
        homeBtn.triggered.connect(self.home)
        navbar.addAction(homeBtn)

        #---------------------search bar---------------------------------
        self.searchBar = QLineEdit()
        self.searchBar.returnPressed.connect(self.loadUrl)
        navbar.addWidget(self.searchBar)
        self.browser.urlChanged.connect(self.updateUrl)

    def home(self):
        self.browser.setUrl(QUrl('https://www.google.com'))

    def loadUrl(self):
        url = "https://www." + self.searchBar.text()
        self.browser.setUrl(QUrl(url))

    def updateUrl(self, url):
        self.searchBar.setText(url.toString())


MyApp = QApplication(sys.argv)
QApplication.setApplicationName('My Web Browser')
window = Window()
MyApp.exec_()