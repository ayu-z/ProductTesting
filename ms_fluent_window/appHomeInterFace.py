# coding:utf-8
from PyQt5.QtCore import Qt, QSize, QEventLoop, QTimer
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QFrame, QHBoxLayout
from qfluentwidgets import IconWidget, TextWrap, FlowLayout, CardWidget
from qfluentwidgets import (setTheme, setFont, Theme, MSFluentWindow, SubtitleLabel, SplashScreen, SimpleCardWidget, ToggleToolButton, IconWidget, StrongBodyLabel, BodyLabel, TextEdit, TabCloseButtonDisplayMode)
from qfluentwidgets import FluentIcon as FIF
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from qfluentwidgets import CheckBox, ComboBox, LineEdit, PrimaryPushButton, SpinBox, SubtitleLabel, TableWidget, TextEdit


class Ui_HomeInterFace(object):
    def setupUi(self, HomeInterFace):
        HomeInterFace.setObjectName("HomeInterFace")
        HomeInterFace.resize(830, 650)

        # 开始按钮
        self.btnStart = PrimaryPushButton(HomeInterFace)
        self.btnStart.setGeometry(QtCore.QRect(650, 590, 153, 41))
        self.btnStart.setObjectName("btnStart")


        # 布局
        self.verticalLayoutWidget = QtWidgets.QWidget(HomeInterFace)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(640, 10, 171, 285))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        # 设备型号选择
        self.SelctDeviceModel = SubtitleLabel(self.verticalLayoutWidget)
        self.SelctDeviceModel.setObjectName("SelctDeviceModel")
        self.verticalLayout.addWidget(self.SelctDeviceModel)
        self.ComboBox = ComboBox(self.verticalLayoutWidget)
        self.ComboBox.setObjectName("ComboBox")
        self.verticalLayout.addWidget(self.ComboBox)

        # 垫片
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)


        # MAC 写入使能
        self.cbEnableMacWrite = CheckBox(self.verticalLayoutWidget)
        self.cbEnableMacWrite.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbEnableMacWrite.sizePolicy().hasHeightForWidth())
        self.cbEnableMacWrite.setSizePolicy(sizePolicy)
        self.cbEnableMacWrite.setMinimumSize(QtCore.QSize(29, 22))
        self.cbEnableMacWrite.setCheckable(True)
        self.cbEnableMacWrite.setObjectName("cbEnableMacWrite")
        self.verticalLayout.addWidget(self.cbEnableMacWrite)

        # MAC起始地址
        self.stlMacStart = SubtitleLabel(self.verticalLayoutWidget)
        self.stlMacStart.setObjectName("stlMacStart")
        self.verticalLayout.addWidget(self.stlMacStart)
        self.leMacInput = LineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(False)
        self.leMacInput.setFont(font)
        self.leMacInput.setText("")
        self.leMacInput.setObjectName("leMacInput")
        self.verticalLayout.addWidget(self.leMacInput)

        # MAC 累加 
        self.stMacAdd = SubtitleLabel(self.verticalLayoutWidget)
        self.stMacAdd.setObjectName("stMacAdd")
        self.verticalLayout.addWidget(self.stMacAdd)
        self.SpinBox = SpinBox(self.verticalLayoutWidget)
        self.SpinBox.setObjectName("SpinBox")
        self.verticalLayout.addWidget(self.SpinBox)


        self.verticalLayoutWidget_2 = QtWidgets.QWidget(HomeInterFace)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 601, 631))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.SubtitleLabel_2 = SubtitleLabel(self.verticalLayoutWidget_2)
        self.SubtitleLabel_2.setObjectName("SubtitleLabel_2")
        self.verticalLayout_2.addWidget(self.SubtitleLabel_2)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.StrongBodyLabel_6 = StrongBodyLabel(self.verticalLayoutWidget_2)
        self.StrongBodyLabel_6.setObjectName("StrongBodyLabel_6")
        self.gridLayout_2.addWidget(self.StrongBodyLabel_6, 0, 0, 1, 1)
        self.StrongBodyLabel_7 = StrongBodyLabel(self.verticalLayoutWidget_2)
        self.StrongBodyLabel_7.setObjectName("StrongBodyLabel_7")
        self.gridLayout_2.addWidget(self.StrongBodyLabel_7, 0, 2, 1, 1)
        self.BodyLabel_6 = BodyLabel(self.verticalLayoutWidget_2)
        self.BodyLabel_6.setObjectName("BodyLabel_6")
        self.gridLayout_2.addWidget(self.BodyLabel_6, 0, 1, 1, 1)
        self.StrongBodyLabel_8 = StrongBodyLabel(self.verticalLayoutWidget_2)
        self.StrongBodyLabel_8.setObjectName("StrongBodyLabel_8")
        self.gridLayout_2.addWidget(self.StrongBodyLabel_8, 1, 0, 1, 1)
        self.BodyLabel_8 = BodyLabel(self.verticalLayoutWidget_2)
        self.BodyLabel_8.setObjectName("BodyLabel_8")
        self.gridLayout_2.addWidget(self.BodyLabel_8, 1, 1, 1, 1)
        self.StrongBodyLabel_9 = StrongBodyLabel(self.verticalLayoutWidget_2)
        self.StrongBodyLabel_9.setObjectName("StrongBodyLabel_9")
        self.gridLayout_2.addWidget(self.StrongBodyLabel_9, 1, 2, 1, 1)
        self.StrongBodyLabel_10 = StrongBodyLabel(self.verticalLayoutWidget_2)
        self.StrongBodyLabel_10.setObjectName("StrongBodyLabel_10")
        self.gridLayout_2.addWidget(self.StrongBodyLabel_10, 2, 0, 1, 1)
        self.BodyLabel_10 = BodyLabel(self.verticalLayoutWidget_2)
        self.BodyLabel_10.setObjectName("BodyLabel_10")
        self.gridLayout_2.addWidget(self.BodyLabel_10, 2, 1, 1, 1)
        self.StrongBodyLabel_11 = StrongBodyLabel(self.verticalLayoutWidget_2)
        self.StrongBodyLabel_11.setObjectName("StrongBodyLabel_11")
        self.gridLayout_2.addWidget(self.StrongBodyLabel_11, 2, 2, 1, 1)
        self.BodyLabel_11 = BodyLabel(self.verticalLayoutWidget_2)
        self.BodyLabel_11.setObjectName("BodyLabel_11")
        self.gridLayout_2.addWidget(self.BodyLabel_11, 2, 3, 1, 1)
        self.BodyLabel_9 = BodyLabel(self.verticalLayoutWidget_2)
        self.BodyLabel_9.setObjectName("BodyLabel_9")
        self.gridLayout_2.addWidget(self.BodyLabel_9, 0, 3, 1, 1)
        self.BodyLabel_12 = BodyLabel(self.verticalLayoutWidget_2)
        self.BodyLabel_12.setObjectName("BodyLabel_12")
        self.gridLayout_2.addWidget(self.BodyLabel_12, 1, 3, 1, 1)
        self.StrongBodyLabel_13 = StrongBodyLabel(self.verticalLayoutWidget_2)
        self.StrongBodyLabel_13.setObjectName("StrongBodyLabel_13")
        self.gridLayout_2.addWidget(self.StrongBodyLabel_13, 3, 0, 1, 1)
        self.BodyLabel_13 = BodyLabel(self.verticalLayoutWidget_2)
        self.BodyLabel_13.setObjectName("BodyLabel_13")
        self.gridLayout_2.addWidget(self.BodyLabel_13, 3, 1, 1, 1)
        self.StrongBodyLabel_12 = StrongBodyLabel(self.verticalLayoutWidget_2)
        self.StrongBodyLabel_12.setObjectName("StrongBodyLabel_12")
        self.gridLayout_2.addWidget(self.StrongBodyLabel_12, 3, 2, 1, 1)
        self.BodyLabel_14 = BodyLabel(self.verticalLayoutWidget_2)
        self.BodyLabel_14.setObjectName("BodyLabel_14")
        self.gridLayout_2.addWidget(self.BodyLabel_14, 3, 3, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem1)
        self.SubtitleLabel_5 = SubtitleLabel(self.verticalLayoutWidget_2)
        self.SubtitleLabel_5.setObjectName("SubtitleLabel_5")
        self.verticalLayout_2.addWidget(self.SubtitleLabel_5)
        self.TextEdit = TextEdit(self.verticalLayoutWidget_2)
        self.TextEdit.setObjectName("TextEdit")
        self.verticalLayout_2.addWidget(self.TextEdit)

        self.retranslateUi(HomeInterFace)
        QtCore.QMetaObject.connectSlotsByName(HomeInterFace)

    def retranslateUi(self, HomeInterFace):
        _translate = QtCore.QCoreApplication.translate
        HomeInterFace.setWindowTitle(_translate("HomeInterFace", "HomeInterFace"))
        self.btnStart.setText(_translate("HomeInterFace", "开始测试"))
        self.SelctDeviceModel.setText(_translate("HomeInterFace", "型号"))
        self.cbEnableMacWrite.setText(_translate("HomeInterFace", "启用 MAC 写入"))
        self.stlMacStart.setText(_translate("HomeInterFace", "MAC起始地址"))
        self.stMacAdd.setText(_translate("HomeInterFace", "累加"))
        self.SubtitleLabel_2.setText(_translate("HomeInterFace", "设备信息"))
        self.StrongBodyLabel_6.setText(_translate("HomeInterFace", "Strong body label"))
        self.StrongBodyLabel_7.setText(_translate("HomeInterFace", "Strong body label"))
        self.BodyLabel_6.setText(_translate("HomeInterFace", "Body label"))
        self.StrongBodyLabel_8.setText(_translate("HomeInterFace", "Strong body label"))
        self.BodyLabel_8.setText(_translate("HomeInterFace", "Body label"))
        self.StrongBodyLabel_9.setText(_translate("HomeInterFace", "Strong body label"))
        self.StrongBodyLabel_10.setText(_translate("HomeInterFace", "Strong body label"))
        self.BodyLabel_10.setText(_translate("HomeInterFace", "Body label"))
        self.StrongBodyLabel_11.setText(_translate("HomeInterFace", "Strong body label"))
        self.BodyLabel_11.setText(_translate("HomeInterFace", "Body label"))
        self.BodyLabel_9.setText(_translate("HomeInterFace", "Body label"))
        self.BodyLabel_12.setText(_translate("HomeInterFace", "Body label"))
        self.StrongBodyLabel_13.setText(_translate("HomeInterFace", "Strong body label"))
        self.BodyLabel_13.setText(_translate("HomeInterFace", "Body label"))
        self.StrongBodyLabel_12.setText(_translate("HomeInterFace", "Strong body label"))
        self.BodyLabel_14.setText(_translate("HomeInterFace", "Body label"))
        self.SubtitleLabel_5.setText(_translate("HomeInterFace", "测试Log"))




class displayHomeInterface(Ui_HomeInterFace, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)


        






    
