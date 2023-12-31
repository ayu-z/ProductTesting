# coding:utf-8
# import model
# import sys
import os
import json

from PyQt5.QtCore import Qt, QSize, QEventLoop, QTimer, QFileInfo, QTime, QStandardPaths, QDate, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QFrame, QFileDialog, QDialog, QScrollArea, QGridLayout, QPlainTextEdit)

from qfluentwidgets import (setTheme,  BodyLabel, FluentIcon, SimpleCardWidget,
                            PrimaryPushButton, TitleLabel, setFont, SingleDirectionScrollArea,MSFluentWindow, SplashScreen, SubtitleLabel, 
                            CheckBox, LineEdit, CompactSpinBox, ToolButton, TextEdit, InfoBadge, StateToolTip, PlainTextEdit)


class ImageLabel(ToolButton):
    modelSelectSignal = pyqtSignal(str)
    def __init__(self, model, image_path, parent=None):
        super().__init__(parent)

        self.model = model
        self.image_path = image_path
        self.initUI()

    def initUI(self):
        self.setFixedSize(150, 150)
        pixmap = QPixmap(self.image_path)
        if not pixmap.isNull():
            icon = QIcon(pixmap)
            self.setIcon(icon)
            self.setIconSize(QSize(150, 150))
            self.setStyleSheet("background-color: rgba(0, 0, 0, 0);")

        self.clicked.connect(self.modelSelectButtonClick)

    def modelSelectButtonClick(self):
        print(f"Button clicked for image: {self.image_path} - Model: {self.model}")
        self.modelSelectSignal.emit(self.model)
        self.window().close()


class modelSelectionDialog(QDialog):

    modelSelectedSignal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        root = QFileInfo(__file__).absolutePath()
        self.folder_path = (root + "./../../resource/images/")
        self.json_path = (root + "./../../resource/json/config.json")
        self.models = self.loadJsonConfig()
        self.initUI()

    def loadJsonConfig(self):
        try:
            with open(self.json_path, 'r') as json_file:
                data = json.load(json_file)
                return data.get("Models", {})
        except Exception as e:
            print(f"Error loading JSON file: {e}")
            return {}

    def initUI(self):
        self.setObjectName("ModelSelectionFrame")
        layout = QVBoxLayout(self)
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setFrameStyle(QScrollArea.NoFrame) 

        self.grid_layout = QGridLayout()

        grid_widget = QWidget(self)
        grid_widget.setLayout(self.grid_layout)
        scroll_area.setWidget(grid_widget)
        layout.addWidget(scroll_area)
        self.setLayout(layout)
        self.load_images()
        self.setFixedSize(880, 600)

    def load_images(self):
        for i in reversed(range(self.grid_layout.count())):
            self.grid_layout.itemAt(i).widget().setParent(None)

        row, col = 0, 0
        for model,model_config in self.models.items():
            image_file = f"{model}.jpg"
            image_path = os.path.join(self.folder_path, image_file)

            if not os.path.exists(image_path):
                image_path = os.path.join(self.folder_path, "Null.jpg")

            self.image_label = ImageLabel(model, image_path)
            model_label = BodyLabel(model)

            if model.lower() == "auto":
                model_label.setText("自动选择")
                
            v_layout = QVBoxLayout()
            v_layout.setContentsMargins(20,20,20,20)
            v_layout.addWidget(self.image_label, 0, Qt.AlignCenter|Qt.AlignBottom)
            v_layout.addWidget(model_label, 0, Qt.AlignCenter|Qt.AlignTop)
            self.grid_layout.addLayout(v_layout, row, col)
            col += 1

            if col == 4:
                col = 0
                row += 1
            self.image_label.modelSelectSignal.connect(self.handleModelClicked)

    def handleModelClicked(self, model):
        print(f"Received Model Clicked Signal: {model}")
        self.modelSelectedSignal.emit(model)

class DeviceInfoCard(SimpleCardWidget):
    """ Device info card """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.root = QFileInfo(__file__).absolutePath()
        self.ToolButton_Model = ToolButton(self.root + f"./../../resource/images/Null.jpg")
        self.ToolButton_Model.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.ToolButton_Model.setIconSize(QSize(150, 150))
        self.ToolButton_Model.resize(150, 150)
        self.ToolButton_Model.clicked.connect(self.selectionModel)
        self.TitleLabel_Model = TitleLabel("unknown")
        self.TitleLabel_Model.setFixedWidth(150)
        self.textEdit_DeviceInfo = TextEdit(self)
        self.textEdit_DeviceInfo.setFixedSize(600, 150)
        self.textEdit_DeviceInfo.setReadOnly(True)
        self.textEdit_DeviceInfo.setFocusPolicy(Qt.NoFocus)
        self.textEdit_DeviceInfo.setStyleSheet("TextEdit { border: 0px solid gray; border-radius: 0px; padding: 0px; }")
        self.InfoBadge_State = InfoBadge.custom('DisConnected !', '#F08080', '#60cdff')
        self.hBoxLayout = QHBoxLayout(self)
        self.vBoxLayout = QVBoxLayout()
        self.vBoxLayout.addWidget(self.TitleLabel_Model)
        self.vBoxLayout.addWidget(self.InfoBadge_State, 0, Qt.AlignLeft )
        self.hBoxLayout.setContentsMargins(10, 10, 10, 10)
        self.hBoxLayout.addWidget(self.ToolButton_Model, 0, Qt.AlignLeft)
        self.hBoxLayout.addLayout(self.vBoxLayout)
        self.vBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.vBoxLayout.addWidget(self.textEdit_DeviceInfo, 0, Qt.AlignLeft)
        
        # self.deviceInfoUpdate("Header1\tHeader2\nValue1\tValue2\nData1\tData2\nOK\nNG")
        # self.linkStateUpdate("192.168.111.1", "unlink")
        self.dialog = modelSelectionDialog()
        self.dialog.setWindowTitle("测试机型选择")
        

    def selectionModel(self):
        self.dialog.exec_()
        


class LogCard(SimpleCardWidget):
    """ Log card """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.Lable_Log = BodyLabel(self)
        self.Lable_Log.setObjectName("BodyLabel")
        self.Lable_Log.setText("测试日志")
        
        self.textEdit_LogOutPut = PlainTextEdit(self)
        self.textEdit_LogOutPut.setFixedSize(770, 165)
        self.textEdit_LogOutPut.setReadOnly(True)
        self.textEdit_LogOutPut.setFocusPolicy(Qt.NoFocus)
        self.textEdit_LogOutPut.setMaximumBlockCount(50)
        self.textEdit_LogOutPut.setStyleSheet("PlainTextEdit { border: 0px solid gray; border-radius: 0px; padding: 0px; }")

        self.LineEdit_Command = LineEdit(self)
        self.LineEdit_Command.setFixedWidth(770)
        self.LineEdit_Command.setStyleSheet("LineEdit { border: 0px solid gray; border-radius: 0px; padding: 0px; }")
        

        # self.logMessageUpdate('ygvyhbjknmdl;')
        self.vBoxLayout = QVBoxLayout()
        self.vBoxLayout.setContentsMargins(20, 5, 10, 5)
        self.vBoxLayout.addWidget(self.Lable_Log, 0, Qt.AlignLeft)
        self.vBoxLayout.addWidget(self.textEdit_LogOutPut, 0, Qt.AlignLeft)
        self.vBoxLayout.setSpacing(5)
        self.vBoxLayout.addWidget(self.LineEdit_Command, 0, Qt.AlignLeft)
        self.setLayout(self.vBoxLayout)

    




class SettingCard(SimpleCardWidget):
    """ Setting card """
    saveJsonSignal = pyqtSignal()
    
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
        self.Button_FileSel.clicked.connect(self.showFileDialog)
        
        self.Button_Save = PrimaryPushButton(self)
        self.Button_Save.setObjectName("Button_Save")
        self.Button_Save.setText("保存")
        self.Button_Save.clicked.connect(self.saveJsonSignal)
        
        
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

    def showFileDialog(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "选择文件", "", "All Files (*);;Text Files (*.txt)")
        if file_name:
            self.Edit_FirmVersion.setText(file_name)
            self.Edit_FirmVersion.setToolTip(file_name)

    


        
class View(SingleDirectionScrollArea):

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
        self.vBoxLayout.addWidget(self.SettingCard, 0, Qt.AlignTop)
        self.vBoxLayout.addSpacing(10) 
        
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






