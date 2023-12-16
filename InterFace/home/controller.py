import os
from PyQt5.QtCore import QTime, QStandardPaths, QDate


class Controller:
    def __init__(self, model, view):
        self._model = model
        self._view = view

        self.currentModel = self._model.currentModel

        self._view.SettingCard.saveJsonSignal.connect(self.settingConfigSave)
        self._view.DeviceInfoCard.dialog.modelSelectedSignal.connect(self.updateDeviceInfo)
        # self._view.DeviceInfoCard.dialog.image_label.modelSelectionSignal.connect(self.handleButtonClick)
        # self.view.SettingCard.Button_Save.clicked.connect(self.settingConfigSave)
        # self._view.LogCard.LineEdit_Command.returnPressed.connect(self.executeCommand)

        self.settingConfigLoad()
        self.deviceNameupdate(self.currentModel)
    
    def deviceInfoUpdate(self,data):
        self._view.DeviceInfoCard.textEdit_DeviceInfo.setMarkdown(self._model.alignMultilineText(data))
        
    def deviceNameupdate(self,data):
        if data is None:
            data = "unknown"
        self._view.DeviceInfoCard.TitleLabel_Model.setText(data)
        self._view.DeviceInfoCard.ToolButton_Model.setIcon(self._model.root + f"./../../resource/images/{data}.jpg")
        
    def linkStateUpdate(self, target ,state):
        if state is None or state == 'unlink':
            self._view.DeviceInfoCard.InfoBadge_State.setText("DisConnected !")
            self._view.DeviceInfoCard.InfoBadge_State.setCustomBackgroundColor("#F08080", "#F08080")
        else:
            self._view.DeviceInfoCard.InfoBadge_State.setText("Connect {}".format(target))
            self._view.DeviceInfoCard.InfoBadge_State.setCustomBackgroundColor("#7FFFD4", "#7FFFD4")

    def executeCommand(self):
        print (f"Executing command:{self._view.LogCard.LineEdit_Command.text()}")

    def logMessageUpdate(self, message):
        currentTime = QTime.currentTime().toString('HH:mm:ss')
        message = f'[{currentTime}]-: {message}'
        self._view.LogCard.textEdit_LogOutPut.appendPlainText(message)
        self.saveLogToFile("\n".format(message))

    def saveLogToFile(self, message):
        documents_path = QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation)
        current_date = QDate.currentDate()
        logFolder_path = os.path.join(documents_path, "ProductTest", "Log")
        if not os.path.exists(logFolder_path):
            os.makedirs(logFolder_path)
        file_path = os.path.join(logFolder_path, f"{current_date.toString('yyyy-MM-dd')}.log")
        with open(file_path, 'a') as file:
            file.write(message)

    def settingConfigLoad(self):
        self._view.SettingCard.CheckBox_Mac.setCheckState(self._model.modelJsonConfig["mac"]["enabled"])
        self._view.SettingCard.Edit_Mac.setText(self._model.modelJsonConfig["mac"]["start"])
        self._view.SettingCard.CompactSpinBox_MacOffset.setValue(self._model.modelJsonConfig["mac"]["offset"])
        self._view.SettingCard.CheckBox_MacCheck.setCheckState(self._model.modelJsonConfig["mac"]["check"])
        self._view.SettingCard.Edit_MacCheck.setText(self._model.modelJsonConfig["mac"]["checkfields"])
        self._view.SettingCard.CheckBox_FirmUpdate.setCheckState(self._model.modelJsonConfig["upgrade"]["enabled"])
        self._view.SettingCard.Edit_FirmVersion.setText(self._model.modelJsonConfig["upgrade"]["version"])

    def settingConfigSave(self):
        data = self._model.loadJsonConfig()
        self._model.modelJsonConfig["mac"]["enabled"] = self._view.SettingCard.CheckBox_Mac.checkState()
        self._model.modelJsonConfig["mac"]["start"] = self._view.SettingCard.Edit_Mac.text()
        self._model.modelJsonConfig["mac"]["offset"] = self._view.SettingCard.CompactSpinBox_MacOffset.value()
        self._model.modelJsonConfig["mac"]["check"] = self._view.SettingCard.CheckBox_MacCheck.checkState()
        self._model.modelJsonConfig["mac"]["checkfields"] = self._view.SettingCard.Edit_MacCheck.text()
        self._model.modelJsonConfig["upgrade"]["enabled"] = self._view.SettingCard.CheckBox_FirmUpdate.checkState()
        self._model.modelJsonConfig["upgrade"]["version"] = self._view.SettingCard.Edit_FirmVersion.text()
        data["Models"][self._model.currentModel].update(self._model.modelJsonConfig)
        # data = self._model.mergeJsonConfig(data, overlay)
        self._model.saveJsonConfig(data)
        self.settingConfigLoad()
        
            
    def updateDeviceInfo(self, selectedModel):
        self._model.changeCurrentModel(selectedModel)
        self.deviceNameupdate(selectedModel)
        self.settingConfigLoad()