import json
from PyQt5.QtCore import QFileInfo


class Model:
    def __init__(self):
        self.root = QFileInfo(__file__).absolutePath()
        self.folder_path = (self.root + "./../../resource/images/")
        self.json_path = (self.root + "./../../resource/json/config.json")


        self.modelJsonConfig = self.loadModelJsonConfig()
        
        
    
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
            aligned_line = aligned_line.replace("OK", T_OK)
            aligned_line = aligned_line.replace("NG", T_NG)
            aligned_lines.append(aligned_line)
        aligned_text = '\n'.join(aligned_lines)
        return aligned_text

    def loadJsonConfig(self):
        try:
            with open(self.json_path, 'r') as json_file:
                _json = json.load(json_file)
                return _json
        except Exception as e:
            print(f"Error loading JSON file: {e}")
            return {}
        
    def saveJsonConfig(self, data):
        try:
            with open(self.json_path, 'w') as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            print(f"Error loading JSON file: {e}")
            return {}
        
    def loadModelJsonConfig(self):
        jC = self.loadJsonConfig()
        self.currentModel = jC["Current"]["model"]
        globalJC = jC["Global"]
        overlayJC = jC["Models"][self.currentModel]
        return self.mergeJsonConfig(globalJC, overlayJC)
    
    def mergeJsonConfig(self, base, overlay):
        result = base.copy()
        for key, value in overlay.items():
            if key in result and isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = self.mergeJsonConfig(result[key], value)
            else:
                result[key] = value
        return result

    def changeCurrentModel(self,model):
        data = self.loadJsonConfig()
        data["Current"]["model"] = model
        self.saveJsonConfig(data)
        self.loadModelJsonConfig()
        