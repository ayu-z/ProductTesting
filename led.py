# import sys
from PyQt5.QtGui import QPainter, QPainter, QColor, QPen, QRadialGradient, QBrush
from PyQt5.QtCore import QPointF
from PyQt5.QtWidgets import QAbstractButton

class MyLed(QAbstractButton):
    def __init__(self, parent=None):
        super(MyLed, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setMinimumSize(24, 24)
        self.setCheckable(True)
        self.scaledSize = 1000.0    #为方便计算，将窗口短边值映射为1000
        self.setLedDefaultOption()

    def setLedDefaultOption(self):
        allAttributes = ['colorOnBegin', 'colorOnEnd', 'colorOffBegin', 'colorOffEnd', 'colorBorderIn', 'colorBorderOut']
        allDefaultVal = [QColor(0, 180, 0), QColor(0, 150, 0), QColor(220, 0, 0), QColor(180, 0, 0), QColor(140, 140, 140), QColor(100, 100, 100)]
        for attr, val in zip(allAttributes, allDefaultVal):
            setattr(self, attr, val)
        self.update()

    def setLedOption(self, opt='colorOnBegin', val=QColor(0,240,0)):
        if hasattr(self, opt):
            setattr(self, opt, val)
            self.update()

    def resizeEvent(self, evt):
        self.update()

    def paintEvent(self, evt):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setPen(QPen(Qt.black, 1))

        realSize = min(self.width(), self.height())                         #窗口的短边
        painter.translate(self.width()/2.0, self.height()/2.0)              #原点平移到窗口中心
        painter.scale(realSize/self.scaledSize, realSize/self.scaledSize)   #缩放，窗口的短边值映射为self.scaledSize
        gradient = QRadialGradient(QPointF(0, 0), self.scaledSize/2.0, QPointF(0, 0))   #辐射渐变

        #画边框外圈和内圈
        for color, radius in [(self.colorBorderOut, self.radiusBorderOut),  #边框外圈
                               (self.colorBorderIn, self.radiusBorderIn)]:   #边框内圈
            gradient.setColorAt(1, color)
            painter.setBrush(QBrush(gradient))
            painter.drawEllipse(QPointF(0, 0), radius, radius)

        # 画内圆
        gradient.setColorAt(0, self.colorOnBegin if self.isChecked() else self.colorOffBegin)
        gradient.setColorAt(1, self.colorOnEnd if self.isChecked() else self.colorOffEnd)
        painter.setBrush(QBrush(gradient))
        painter.drawEllipse(QPointF(0, 0), self.radiusCircle, self.radiusCircle)