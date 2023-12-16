# coding:utf-8

import sys

from PyQt5.QtCore import Qt, QSize, QEventLoop, QTimer, QFileInfo
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QApplication)

from qfluentwidgets import (setTheme,FluentIcon,MSFluentWindow, SplashScreen)

import ui.home.model as ui_MHome
import ui.home.view as ui_VHome
import ui.home.controller as ui_CHome



class Window(MSFluentWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.root = QFileInfo(__file__).absolutePath()
        self.setFixedSize(880, 650)
        self.setWindowTitle('Product Test Tool')
        self.setWindowIcon(QIcon(self.root + './resource/images/iyl_logo.png'))
        self.titleBar.raise_()
        self.initSplashScreen()
        self.initNavigation()

        # self.homeInterface.DeviceInfoCard.TitleLabel_Model.setText("link")
        
    def initSplashScreen(self):
        self.splashScreen = SplashScreen(QIcon(self.root + './resource/images/ylx_logo.png'), self)
        self.splashScreen.setIconSize(QSize(200, 200))
        self.show()
        loop = QEventLoop()
        QTimer.singleShot(1000, loop.quit)
        loop.exec()
        self.splashScreen.finish()
    
    def initNavigation(self):
        self.homeInterface = ui_VHome.View(self)
        self.appInterface = ui_VHome.Widget('开发中...')
        self.addSubInterface(self.homeInterface, FluentIcon.HOME, "主页", FluentIcon.HOME_FILL, isTransparent=True)
        self.addSubInterface(self.appInterface, FluentIcon.APPLICATION, '应用')
        
        self.controller = ui_CHome.Controller(ui_MHome.Model(), self.homeInterface)

if __name__ == '__main__':

    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    

    # setTheme(Theme.DARK)

    app = QApplication(sys.argv)
    w = Window()
    w.show() 
    
    app.exec_()