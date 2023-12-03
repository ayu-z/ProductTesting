# coding:utf-8
from PyQt5.QtCore import Qt, QSize, QEventLoop, QTimer
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QFrame, QHBoxLayout
from qfluentwidgets import IconWidget, TextWrap, FlowLayout, CardWidget
from qfluentwidgets import (setTheme, setFont, Theme, MSFluentWindow, SubtitleLabel, SplashScreen, SimpleCardWidget, ToggleToolButton, IconWidget, StrongBodyLabel, BodyLabel, TextEdit)
from qfluentwidgets import FluentIcon as FIF

from PyQt5.QtCore import Qt, pyqtSignal, QUrl, QEvent
from PyQt5.QtGui import QDesktopServices, QPainter, QPen, QColor
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QFrame


class displayHomeInterface(QFrame):

    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.setObjectName(text.replace(' ', '-'))
        
        # self.toggleToolButton = ToggleToolButton(FIF.SETTING, self)
        # self.toggleToolButton.toggled.connect(lambda: print('Toggled'))
        # self.toggleToolButton.clicked.connect(lambda: print('clicked'))
        
        textEdit = TextEdit(self)
        textEdit.setMarkdown(
            "## Steel Ball Run \n * Johnny Joestar 🦄 \n * Gyro Zeppeli 🐴 ")
        w, h = QApplication.desktop().availableGeometry().width(), QApplication.desktop().availableGeometry().height()
        textEdit.setFixedSize(self.width(), self.height())


    


    
