from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from instr import *

age7_8 = [6.5, 12, 17, 21]
age9_10 = [5, 10.5, 15.5, 19.5]
age11_12 = [3.5, 9, 14, 18]
age13_14 = [2, 7.5, 12.5, 16.5]
age15_99 = [0.5, 6, 11, 15]

class FinalWin(QWidget):
    def __init__(self, exp):
        super().__init__()
        self.set_appear()
        self.result(exp)
        self.initUI()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.index = QLabel(txt_index+str(self.index))
        self.workheart = QLabel(txt_workheart+self.res)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.index, alignment = Qt.AlignCenter)
        self.layout.addWidget(self.workheart, alignment = Qt.AlignCenter)
        self.setLayout(self.layout)
    def result(self, exp):
        self.index = (4*(int(exp.t1)+int(exp.t2)+int(exp.t3))-200)/10
        if int(exp.age) < 9:
            age = age7_8
        elif int(exp.age) < 11:
            age = age9_10
        elif int(exp.age) < 13:
            age = age11_12
        elif int(exp.age) < 15:
            age = age13_14
        else:
            age = age15_99
        if self.index < age[0]:
            self.res = txt_res5
        elif self.index < age[1]:
            self.res = txt_res4
        elif self.index < age[2]:
            self.res = txt_res3
        elif self.index < age[4]:
            self.res = txt_res2
        else:
            self.res = txt_res1

if __name__ == '__main__':
    class Exp():
        def __init__(self):
            self.t1 = 15
            self.t2 = 22
            self.t3 = 19
            self.age = 16
    app = QApplication([])
    final_win = FinalWin(Exp())
    app.exec_()