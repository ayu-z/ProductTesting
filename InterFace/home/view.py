# coding:utf-8
import model
import sys
import os
import json

from PyQt5.QtCore import Qt, QSize, QEventLoop, QTimer, QFileInfo
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QFrame, QFileDialog, QDialog, QScrollArea, QGridLayout)

from qfluentwidgets import (setTheme,  BodyLabel, FluentIcon, SimpleCardWidget,
                            PrimaryPushButton, TitleLabel, setFont, SingleDirectionScrollArea,MSFluentWindow, SplashScreen, SubtitleLabel, 
                            CheckBox, LineEdit, CompactSpinBox, ToolButton, TextEdit, InfoBadge, StateToolTip)


class ImageLabel(ToolButton):
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

        self.clicked.connect(self.handleButtonClick)

    def handleButtonClick(self):
        print(f"Button clicked for image: {self.image_path} - Model: {self.model}")
        # if self.model.lower() == "auto":
            # self.searchModel()
        self.window().close()
        
    # def searchModel(self):
    #     with open("config.json", "r") as file:
    #         config_data = json.load(file)
    #     target_ip = config_data["target_ip"]
    #     ssh_username = config_data["ssh_username"]
    #     ssh_password = config_data["ssh_password"]
    #     ssh = ProductTest.SSHClient(target_ip, ssh_username, ssh_password)
    #     result = ssh.send_command("cat /tmp/sysinfo/model").strip()  
    #     print(f"Device Model:{result}")

class ModelSelectionDialog(QDialog):
    def __init__(self):
        super().__init__()

        root = QFileInfo(__file__).absolutePath()
        self.folder_path = (root + "./../../resource/images/")
        self.json_path = (root + "./../../resource/json/config.json")
        self.models = self.load_models()

        self.initUI()

    def load_models(self):
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
        for model, model_config in self.models.items():
            image_file = f"{model}.jpg"
            image_path = os.path.join(self.folder_path, image_file)

            if not os.path.exists(image_path):
                image_path = os.path.join(self.folder_path, "Null.jpg")

            image_label = ImageLabel(model, image_path, self)
            model_label = BodyLabel(model, self)

            if model.lower() == "auto":
                model_label.setText("自动选择")
                
            v_layout = QVBoxLayout()
            v_layout.setContentsMargins(20,20,20,20)
            v_layout.addWidget(image_label, 0, Qt.AlignCenter|Qt.AlignBottom)
            v_layout.addWidget(model_label, 0, Qt.AlignCenter|Qt.AlignTop)
            self.grid_layout.addLayout(v_layout, row, col)
            col += 1

            if col == 4:
                col = 0
                row += 1

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
        # self.leftBoxLayout = QVBoxLayout(self)
        self.vBoxLayout = QVBoxLayout()
        self.initLayout()

    def initLayout(self):
        self.vBoxLayout.addWidget(self.TitleLabel_Model)
        self.vBoxLayout.addWidget(self.InfoBadge_State, 0, Qt.AlignLeft )
        # self.hBoxLayout.setSpacing(0)
        self.hBoxLayout.setContentsMargins(10, 10, 10, 10)
        self.hBoxLayout.addWidget(self.ToolButton_Model, 0, Qt.AlignLeft)
        self.hBoxLayout.addLayout(self.vBoxLayout)
        # self.vBoxLayout.addLayout(self.leftBoxLayout)
        self.vBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.vBoxLayout.addWidget(self.textEdit_DeviceInfo, 0, Qt.AlignLeft)
        
        self.deviceInfoUpdate("Header1\tHeader2\nValue1\tValue2\nData1\tData2\nOK\nNG")
        
        self.linkStateUpdate("192.168.111.1", "unlink")
        
    def alignMultilineText(self, data):
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
    
    def deviceInfoUpdate(self,data):
        aligned_data = self.alignMultilineText(data)
        self.textEdit_DeviceInfo.setMarkdown(aligned_data)
        
    def deviceNameupdate(self,data):
        if data is None:
            data = "unknown"
        print (data)
        self.TitleLabel_Model.setText(data)
        self.ToolButton_Model.setIcon(self.root + f"./../../resource/images/{data}.jpg")
        
    def linkStateUpdate(self, target ,state):
        if state is None or state == 'unlink':
            self.InfoBadge_State.setText("DisConnected !")
            self.InfoBadge_State.setCustomBackgroundColor("#F08080", "#F08080")
        else:
            self.InfoBadge_State.setText("Connect {}".format(target))
            self.InfoBadge_State.setCustomBackgroundColor("#7FFFD4", "#7FFFD4")

    def selectionModel(self):
        dialog = ModelSelectionDialog()
        dialog.setWindowTitle("测试机型选择")
        dialog.exec_()


class LogCard(SimpleCardWidget):
    """ Log card """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.Lable_Log = BodyLabel(self)
        self.Lable_Log.setObjectName("BodyLabel")
        self.Lable_Log.setText("测试日志")
        
        self.textEdit_LogOutPut = TextEdit(self)
        self.textEdit_LogOutPut.setFixedSize(770, 100)
        self.textEdit_LogOutPut.setReadOnly(True)
        self.textEdit_LogOutPut.setFocusPolicy(Qt.NoFocus)
        self.textEdit_LogOutPut.setStyleSheet("TextEdit { border: 0px solid gray; border-radius: 0px; padding: 0px; }")

        self.LineEdit_Command = LineEdit(self)
        self.LineEdit_Command.setFixedWidth(770)
        self.LineEdit_Command.setStyleSheet("LineEdit { border: 0px solid gray; border-radius: 0px; padding: 0px; }")
        self.LineEdit_Command.returnPressed.connect(self.executeCommand)
        
        self.vBoxLayout = QVBoxLayout()
        self.initLayout()

    def initLayout(self):
        self.vBoxLayout.setContentsMargins(20, 10, 10, 10)
        self.vBoxLayout.addWidget(self.Lable_Log, 0, Qt.AlignLeft)
        self.vBoxLayout.addWidget(self.textEdit_LogOutPut, 0, Qt.AlignLeft)
        self.vBoxLayout.addWidget(self.LineEdit_Command, 0, Qt.AlignLeft)
        
        self.setLayout(self.vBoxLayout)

    def executeCommand(self):
        print (f"Executing command:{self.LineEdit_Command.text()}")


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


