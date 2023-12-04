# coding:utf-8
import sys
from pathlib import Path

from PyQt5.QtCore import Qt, QPoint, QSize, QUrl, QRect, QPropertyAnimation, QEventLoop, QTimer, QFileInfo
from PyQt5.QtGui import QIcon, QFont, QColor, QPainter
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGraphicsOpacityEffect, QFrame

from qfluentwidgets import (CardWidget, setTheme, Theme, IconWidget, BodyLabel, CaptionLabel, PushButton,
                            TransparentToolButton, FluentIcon, RoundMenu, Action, ElevatedCardWidget,
                            ImageLabel, isDarkTheme, FlowLayout, MSFluentTitleBar, SimpleCardWidget,
                            HeaderCardWidget, InfoBarIcon, HyperlinkLabel, HorizontalFlipView,
                            PrimaryPushButton, TitleLabel, PillPushButton, setFont, SingleDirectionScrollArea,
                            VerticalSeparator, MSFluentWindow, NavigationItemPosition, SplashScreen, SubtitleLabel)

from qfluentwidgets.components.widgets.acrylic_label import AcrylicBrush


class DeviceInfoCard(SimpleCardWidget):
    """ App information card """

    def __init__(self, parent=None):
        super().__init__(parent)
        root = QFileInfo(__file__).absolutePath()
        self.iconLabel = ImageLabel(root + "./resource/M21L2S.jpg", self)
        self.iconLabel.setBorderRadius(8, 8, 8, 8)
        self.iconLabel.scaledToWidth(120)

        self.nameLabel = TitleLabel('M21L2S', self)
        self.testButton = PrimaryPushButton('测试', self)
        self.companyLabel = HyperlinkLabel(QUrl('https://www.iyunlink.com/'), 'IYUNLINK Inc.', self)
        self.testButton.setFixedWidth(160)



        self.descriptionLabel = BodyLabel(
            'PyQt-Fluent-Widgets 是一个基于 PyQt/PySide 的 Fluent Design 风格组件库，包含许多美观实用的组件，支持亮暗主题无缝切换和自定义主题色，帮助开发者快速实现美观优雅的现代化界面。', self)
        self.descriptionLabel.setWordWrap(True)

        self.settingButton = TransparentToolButton(FluentIcon.SETTING, self)
        self.settingButton.setFixedSize(32, 32)
        self.settingButton.setIconSize(QSize(14, 14))

        self.hBoxLayout = QHBoxLayout(self)
        self.vBoxLayout = QVBoxLayout()
        self.topLayout = QHBoxLayout()
        self.statisticsLayout = QHBoxLayout()
        self.buttonLayout = QHBoxLayout()

        self.initLayout()

    def initLayout(self):
        self.hBoxLayout.setSpacing(30)
        self.hBoxLayout.setContentsMargins(34, 24, 24, 24)
        self.hBoxLayout.addWidget(self.iconLabel)
        self.hBoxLayout.addLayout(self.vBoxLayout)

        self.vBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.vBoxLayout.setSpacing(0)

        # name label and install button
        self.vBoxLayout.addLayout(self.topLayout)
        self.topLayout.setContentsMargins(0, 0, 0, 0)
        self.topLayout.addWidget(self.nameLabel)
        self.topLayout.addWidget(self.testButton, 0, Qt.AlignRight)
        # self.vBoxLayout.addWidget(self.untestButton, 0, Qt.AlignRight)

        # company label
        self.vBoxLayout.addSpacing(3)
        self.vBoxLayout.addWidget(self.companyLabel, 0, Qt.AlignTop)

        # statistics widgets
        self.vBoxLayout.addSpacing(20)
        self.vBoxLayout.addLayout(self.statisticsLayout)
        self.statisticsLayout.setContentsMargins(0, 0, 0, 0)
        self.statisticsLayout.setSpacing(10)

        self.statisticsLayout.setAlignment(Qt.AlignLeft)

        # description label
        self.vBoxLayout.addSpacing(20)
        self.vBoxLayout.addWidget(self.descriptionLabel)

        # button
        self.vBoxLayout.addSpacing(12)
        self.buttonLayout.setContentsMargins(0, 0, 0, 0)
        self.vBoxLayout.addLayout(self.buttonLayout)
        # self.buttonLayout.addWidget(self.tagButton, 0, Qt.AlignRight)
        self.buttonLayout.addWidget(self.settingButton, 0, Qt.AlignRight)


class LogCard(HeaderCardWidget):
    """ Log card """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTitle('测试日志')


class HomeInterFace(SingleDirectionScrollArea):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.view = QWidget(self)

        self.vBoxLayout = QVBoxLayout(self.view)
        self.appCard = DeviceInfoCard(self)
        
        self.descriptionCard = LogCard(self)

        self.setWidget(self.view)
        self.setWidgetResizable(True)
        self.setObjectName("appInterface")

        self.vBoxLayout.setSpacing(10)
        self.vBoxLayout.setContentsMargins(0, 0, 10, 30)
        self.vBoxLayout.addWidget(self.appCard, 0, Qt.AlignTop)
        self.vBoxLayout.addWidget(self.descriptionCard, 0, Qt.AlignTop)

        
        self.setStyleSheet("QScrollArea {border: none; background:transparent}")
        self.view.setStyleSheet('QWidget {background:transparent}')

class Widget(QFrame):

    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.label = SubtitleLabel(text, self)
        self.hBoxLayout = QHBoxLayout(self)
        setFont(self.label, 24)
        self.label.setAlignment(Qt.AlignCenter)
        self.hBoxLayout.addWidget(self.label, 1, Qt.AlignCenter)
        self.setObjectName(text.replace(' ', '-'))

class Window(MSFluentWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.root = QFileInfo(__file__).absolutePath()
        self.setFixedSize(880, 600)
        self.setWindowTitle('IYUNLINK Product Test Tool')
        self.setWindowIcon(QIcon(self.root + './resource/iyl_logo.png'))
        self.titleBar.raise_()
        self.initSplashScreen()
        
        self.initNavigation()
        
        
    def initSplashScreen(self):
        self.splashScreen = SplashScreen(QIcon(self.root + './resource/ylx_logo.png'), self)
        self.splashScreen.setIconSize(QSize(102, 102))
        self.show()
        loop = QEventLoop()
        QTimer.singleShot(1000, loop.quit)
        loop.exec()
        self.splashScreen.finish()
    
    def initNavigation(self):
        self.homeInterface = HomeInterFace(self)
        self.appInterface = Widget('开发中...')

        self.addSubInterface(self.homeInterface, FluentIcon.HOME, "主页", FluentIcon.HOME_FILL, isTransparent=True)
        self.addSubInterface(self.appInterface, FluentIcon.APPLICATION, '应用')


if __name__ == '__main__':

    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    setTheme(Theme.DARK)

    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec_()
