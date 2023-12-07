# coding:utf-8
import sys
from pathlib import Path

from PyQt5.QtCore import Qt, QPoint, QSize, QUrl, QRect, QPropertyAnimation, QEventLoop, QTimer, QFileInfo
from PyQt5.QtGui import QIcon, QFont, QColor, QPainter, QPixmap
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGraphicsOpacityEffect, QFrame, 
                            QAbstractButton, QSpacerItem, QSizePolicy, QFileDialog, QPushButton, QTableWidget, QTableWidgetItem)

from qfluentwidgets import (CardWidget, setTheme, Theme, IconWidget, BodyLabel, CaptionLabel, PushButton,
                            TransparentToolButton, FluentIcon, RoundMenu, Action, ElevatedCardWidget,
                            ImageLabel, isDarkTheme, FlowLayout, MSFluentTitleBar, SimpleCardWidget,
                            HeaderCardWidget, InfoBarIcon, HyperlinkLabel, HorizontalFlipView,
                            PrimaryPushButton, TitleLabel, PillPushButton, setFont, SingleDirectionScrollArea,
                            VerticalSeparator, MSFluentWindow, NavigationItemPosition, SplashScreen, SubtitleLabel, 
                            CheckBox, LineEdit, CompactSpinBox, ToolButton, TextEdit)

from qfluentwidgets.components.widgets.acrylic_label import AcrylicBrush



class DeviceInfoCard(SimpleCardWidget):
    """ Device info card """

    def __init__(self, parent=None):
        super().__init__(parent)
        root = QFileInfo(__file__).absolutePath()
        self.ToolButton_Model = ToolButton(root + "./resource/images/M21L2S.jpg")
        self.ToolButton_Model.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.ToolButton_Model.setIconSize(QSize(150, 150))
        self.ToolButton_Model.resize(150, 150)
        self.ToolButton_Model.clicked.connect(self.selection_model)
        
        self.TitleLabel_Model = TitleLabel('M21L2S', self)
        self.textEdit_DeviceInfo = TextEdit(self)
        data = "Header1\tHeader2\nValue1\tValue2\nData1\tData2\nOK\nNG"
        aligned_data = self.align_multiline_text(data)
        self.textEdit_DeviceInfo.setMarkdown(aligned_data)
        self.textEdit_DeviceInfo.setFixedSize(600, 150)
        self.textEdit_DeviceInfo.setReadOnly(True)
        self.textEdit_DeviceInfo.setFocusPolicy(Qt.NoFocus)
        self.textEdit_DeviceInfo.setStyleSheet("TextEdit { border: 0px solid gray; border-radius: 0px; padding: 0px; }")

        self.hBoxLayout = QHBoxLayout(self)
        self.vBoxLayout = QVBoxLayout()
        self.initLayout()

    def initLayout(self):
        self.hBoxLayout.setSpacing(0)
        self.hBoxLayout.setContentsMargins(10, 10, 10, 10)
        self.hBoxLayout.addWidget(self.ToolButton_Model, 0, Qt.AlignLeft)
        self.hBoxLayout.addLayout(self.vBoxLayout)

        self.vBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.vBoxLayout.addWidget(self.TitleLabel_Model, 0, Qt.AlignLeft)
        self.vBoxLayout.addWidget(self.textEdit_DeviceInfo, 0, Qt.AlignLeft)
        
    def align_multiline_text(self, data):
        T_OK = '<span style="background-color: #4CAF50; color: #ffffff; padding: 5px; display: inline-block;"> OK </span>'
        T_NG = '<span style="background-color: #FF0000; color: #ffffff; padding: 5px; display: inline-block;"> NG </span>'
        lines = data.split('\n')
        max_widths = [max(len(field) for field in line.split('\t')) for line in lines]
        aligned_lines = []
        for line in lines:
            fields = line.split('\t')
            aligned_fields = ["{:<{}}".format(field, max_width) for field, max_width in zip(fields, max_widths)]
            aligned_line = '#### '+'\t\t\t'.join(aligned_fields)

            # Replace "OK" with the corresponding HTML span
            aligned_line = aligned_line.replace("OK", T_OK)

            # Replace "NG" with the corresponding HTML span
            aligned_line = aligned_line.replace("NG", T_NG)

            aligned_lines.append(aligned_line)

        aligned_text = '\n'.join(aligned_lines)
        return aligned_text

    def selection_model(self):
        print('Button Clicked!')


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

    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    

    # setTheme(Theme.DARK)

    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec_()
