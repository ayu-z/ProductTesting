# coding:utf-8
import sys
from pathlib import Path

from PyQt5.QtCore import Qt, QPoint, QSize, QUrl, QRect, QPropertyAnimation, QEventLoop, QTimer, QFileInfo
from PyQt5.QtGui import QIcon, QFont, QColor, QPainter
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGraphicsOpacityEffect, QFrame, QAbstractButton, QSpacerItem, QSizePolicy, QFileDialog

from qfluentwidgets import (CardWidget, setTheme, Theme, IconWidget, BodyLabel, CaptionLabel, PushButton,
                            TransparentToolButton, FluentIcon, RoundMenu, Action, ElevatedCardWidget,
                            ImageLabel, isDarkTheme, FlowLayout, MSFluentTitleBar, SimpleCardWidget,
                            HeaderCardWidget, InfoBarIcon, HyperlinkLabel, HorizontalFlipView,
                            PrimaryPushButton, TitleLabel, PillPushButton, setFont, SingleDirectionScrollArea,
                            VerticalSeparator, MSFluentWindow, NavigationItemPosition, SplashScreen, SubtitleLabel, CheckBox, LineEdit, CompactSpinBox)

from qfluentwidgets.components.widgets.acrylic_label import AcrylicBrush


class DeviceInfoCard(SimpleCardWidget):
    """ Device info card """

    def __init__(self, parent=None):
        super().__init__(parent)
        root = QFileInfo(__file__).absolutePath()
        self.iconLabel = ImageLabel(root + "./resource/images/M21L2S.jpg", self)
        self.iconLabel.setBorderRadius(8, 8, 8, 8)
        self.iconLabel.scaledToWidth(120)

        self.nameLabel = TitleLabel('M21L2S', self)
        self.testButton = PrimaryPushButton('测试', self)
        self.companyLabel = HyperlinkLabel(QUrl('https://www.iyunlink.com/'), 'IYUNLINK Inc.', self)
        self.testButton.setFixedWidth(160)
    
        self.descriptionLabel = BodyLabel('', self)
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


class SettingCard(SimpleCardWidget):
    """ Setting card """
    def __init__(self, parent=None):
        super().__init__(parent)

        self.CheckBox_Mac = CheckBox(self)
        self.CheckBox_Mac.setObjectName("CheckBox_Mac")
        self.CheckBox_Mac.setText("MAC写入")

        self.Edit_Mac = LineEdit(self)
        self.Edit_Mac.setText("")
        self.Edit_Mac.setAlignment(Qt.AlignCenter)
        self.Edit_Mac.setObjectName("Edit_Mac")
        self.Edit_Mac.setPlaceholderText("起始MAC地址")

        self.Lable_Offset = BodyLabel(self)
        self.Lable_Offset.setObjectName("BodyLabel")
        self.Lable_Offset.setText("增量")
        
        self.CompactSpinBox_MacOffset = CompactSpinBox(self)
        self.CompactSpinBox_MacOffset.setObjectName("CompactSpinBox_MacOffset")
        
        self.CheckBox_MacCheck = CheckBox(self)
        self.CheckBox_MacCheck.setObjectName("CheckBox_MacCheck")
        self.CheckBox_MacCheck.setText("MAC检测")
        self.Edit_MacCheck = LineEdit(self)
        self.Edit_MacCheck.setText("")
        self.Edit_MacCheck.setAlignment(Qt.AlignCenter)
        self.Edit_MacCheck.setObjectName("Edit_MacCheck")
        self.Edit_MacCheck.setPlaceholderText("检测字段")

        self.CheckBox_FirmUpdate = CheckBox(self)
        self.CheckBox_FirmUpdate.setObjectName("CheckBox_FirmUpdate")
        self.CheckBox_FirmUpdate.setText("固件升级")

        self.Edit_FirmVersion = LineEdit(self)
        self.Edit_FirmVersion.setText("")
        self.Edit_FirmVersion.setAlignment(Qt.AlignCenter)
        self.Edit_FirmVersion.setReadOnly(True)
        self.Edit_FirmVersion.setObjectName("Edit_FirmVersion")
        self.Edit_FirmVersion.setPlaceholderText("固件路径")
        self.Edit_FirmVersion.setFocusPolicy(Qt.NoFocus)

        self.Button_FileSel = PrimaryPushButton(self)
        self.Button_FileSel.setObjectName("Button_FileSel")
        self.Button_FileSel.setText("选择")
        self.Button_FileSel.clicked.connect(self.show_file_dialog)
        
        self.Button_Save = PrimaryPushButton(self)
        self.Button_Save.setObjectName("Button_Save")
        self.Button_Save.setText("保存")
        
        self.testButton = PrimaryPushButton('测试', self)
        self.testButton.setFixedSize(90, 60)
        
        
        self.hBoxLayout_Mac = QHBoxLayout()
        self.hBoxLayout_Firm = QHBoxLayout()
        
        self.hBoxLayout = QHBoxLayout()
        self.vBoxLayout = QVBoxLayout()

        self.initLayout()

    def initLayout(self):
        
        self.hBoxLayout_Mac.setContentsMargins(0, 0, 0, 0)
        self.hBoxLayout_Mac.addSpacing(20)
        self.hBoxLayout_Mac.addWidget(self.CheckBox_Mac)
        self.hBoxLayout_Mac.addWidget(self.Edit_Mac)
        self.hBoxLayout_Mac.addWidget(self.Lable_Offset)
        self.hBoxLayout_Mac.addWidget(self.CompactSpinBox_MacOffset)
        self.hBoxLayout_Mac.addWidget(self.CheckBox_MacCheck)
        self.hBoxLayout_Mac.addWidget(self.Edit_MacCheck)
        
        self.hBoxLayout_Firm.setContentsMargins(0, 0, 0, 0)
        self.hBoxLayout_Firm.addSpacing(20)
        self.hBoxLayout_Firm.addWidget(self.CheckBox_FirmUpdate)
        self.hBoxLayout_Firm.addWidget(self.Edit_FirmVersion)
        self.hBoxLayout_Firm.addWidget(self.Button_FileSel)
        self.hBoxLayout_Firm.addWidget(self.Button_Save)

        self.vBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.vBoxLayout.addLayout(self.hBoxLayout_Mac)
        self.vBoxLayout.addLayout(self.hBoxLayout_Firm)
        
        # self.hBoxLayout.setContentsMargins(0, 0, 20, 0)
        self.hBoxLayout.setSpacing(10)
        self.hBoxLayout.addLayout(self.vBoxLayout)
        self.hBoxLayout.addWidget(self.testButton)
        self.hBoxLayout.addSpacing(10)
        self.setLayout(self.hBoxLayout)
        
    def show_file_dialog(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "选择文件", "", "All Files (*);;Text Files (*.txt)")
        if file_name:
            self.Edit_FirmVersion.setText(file_name)
            self.Edit_FirmVersion.setToolTip(file_name)



        
class HomeInterFace(SingleDirectionScrollArea):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.view = QWidget(self)

        self.vBoxLayout = QVBoxLayout(self.view)
        self.DeviceInfoCard = DeviceInfoCard(self)
        self.LogCard = LogCard(self)
        self.SettingCard = SettingCard(self)

        self.setWidget(self.view)
        self.setWidgetResizable(True)
        self.setObjectName("appInterface")

        self.vBoxLayout.setSpacing(10)
        self.vBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.vBoxLayout.addWidget(self.DeviceInfoCard, 0, Qt.AlignTop)
        self.vBoxLayout.addWidget(self.LogCard, 0, Qt.AlignTop)
        self.vBoxLayout.addWidget(self.SettingCard, 0, Qt.AlignBottom)
        self.vBoxLayout.addSpacing(20) 

        
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
        self.setWindowTitle('Product Test Tool')
        self.setWindowIcon(QIcon(self.root + './resource/images/iyl_logo.png'))
        self.titleBar.raise_()
        self.initSplashScreen()
        
        self.initNavigation()
        
        
    def initSplashScreen(self):
        self.splashScreen = SplashScreen(QIcon(self.root + './resource/images/ylx_logo.png'), self)
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

    # setTheme(Theme.DARK)

    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec_()
