import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        button1 = QPushButton('Button 1', self)
        button2 = QPushButton('Button 2', self)

        layout.addWidget(button1)
        layout.addWidget(button2)

        # 调整第一个按钮的最小和最大高度
        button1.setMinimumHeight(50)
        button1.setMaximumHeight(100)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec_())
