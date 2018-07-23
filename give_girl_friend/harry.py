import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont, QIcon
from PyQt5 import QtGui, QtCore
import random

import sys, os
def resource_path(relative_path):
       if hasattr(sys, '_MEIPASS'):
           return os.path.join(sys._MEIPASS, relative_path)
       return os.path.join(os.path.abspath("."), relative_path)


class MessageBox(QtWidgets.QWidget):
    CloseAllowed=0
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self)
        self.setGeometry(300,300,800,800) # 设置主窗口大小
        self.center()# 居中函数
        self.setFixedSize(self.width(), self.height()) #限制窗口的控件大小
        self.setWindowTitle(u'hello, i am harry')
        self.setWindowIcon(QIcon('1.png')) # ICON 的背景图片
        self.setToolTip(u'我该说点什么')
        QtWidgets.QToolTip.setFont(QFont('华文楷体', 40)) #设置字体
        self.label1 = QtWidgets.QLabel(u'<b>小姐姐，我观察你很久了!</b>',self)
        self.label1.move(150, 40) #label1的摆放位置
        self.label1.setFont(QFont("Timers", 40))
        self.label2 = QtWidgets.QLabel(u'<b>做我女朋友好不好?</b>', self)
        self.label2.move(150,100)
        self.label2.setFont(QFont("Timers",20))

        self.window_pale = QtGui.QPalette() #实例化该类
        self.window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("表白底图.jpg")))
        self.setPalette(self.window_pale)

        self.buttonOK = QtWidgets.QPushButton(u'同意',self)
        self.buttonOK.setFocusPolicy(QtCore.Qt.NoFocus) # 按钮无焦点
        self.buttonOK.move(50,700) # 摆放位置
        self.buttonOK.clicked.connect(self.showDialogOK)

        self.buttonE = QtWidgets.QPushButton(u'考虑考虑呗', self)
        self.buttonE.setFocusPolicy(QtCore.Qt.NoFocus)

        self.buttonE.move(330,700)
        self.buttonE.clicked.connect(self.showDialogEE)

        self.buttonNO = QtWidgets.QPushButton(u'拒绝',self)
        self.buttonNO.setFocusPolicy(QtCore.Qt.NoFocus)
        self.buttonNO.move(610, 700)
        self.buttonNO.clicked.connect(self.showDialogNO)

    def showDialogOK(self):
        QtWidgets.QMessageBox.information(self, "欧耶", "爱你 么么么么么么哒",QtWidgets.QMessageBox.Ok)
        self.CloseAllowed = 1
    def showDialogEE(self):
        QtWidgets.QMessageBox.information(self, "别纠结了", "你完了， 你爸妈让你嫁给我",QtWidgets.QMessageBox.Ok)
        QtWidgets.QMessageBox.information(self, "别纠结了", "你爸也是这么说的", QtWidgets.QMessageBox.Ok)
        QtWidgets.QMessageBox.information(self, "别纠结了", "你奶奶也让你嫁给我", QtWidgets.QMessageBox.Ok)
        QtWidgets.QMessageBox.information(self, "别纠结了", "你弟弟也同意", QtWidgets.QMessageBox.Ok)
        QtWidgets.QMessageBox.information(self, "别纠结了", "你全家都同意", QtWidgets.QMessageBox.Ok)
        QtWidgets.QMessageBox.information(self, "别纠结了", "接受现实吧，我会对你好的", QtWidgets.QMessageBox.Ok)
        QtWidgets.QMessageBox.information(self, "别纠结了", "你是我的人了", QtWidgets.QMessageBox.Ok)

    def showDialogNO(self):
        self.q = random.randint(0,650)
        self.w = random.randint(150,650)
        self.buttonNO.move(self.q, self.w)

    def closeEvent(self, event):
        if self.CloseAllowed == 1:
            event.accept()
        else:
            QtWidgets.QMessageBox.information(self, "未作回应", "小姐姐，请不要逃避", QtWidgets.QMessageBox.Ok)
            event.ignore()
    def center(self):
        screen = QtWidgets.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-screen.width())/2, (screen.height()-screen.height())/2)

app = QtWidgets.QApplication(sys.argv)
window = MessageBox()
window.show()
sys.exit(app.exec_())