from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QMessageBox, QVBoxLayout, QHBoxLayout
from instr import *

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_x, win_y) 

    def initUI(self):
        self.gen_line = QHBoxLayout()
        self.line = QVBoxLayout()
        self.line2 = QVBoxLayout()
        
        # Текстовые подсказки
        self.w_name = QLabel(txt_name)
        self.w_age = QLabel(txt_age)
        self.w_test1 = QLabel(txt_test1)
        self.w_test2 = QLabel(txt_test2)
        self.w_test3 = QLabel(txt_test3)
        self.timer = QLabel('00:00:00')

        # Ввод текста
        self.w_hintname = QLineEdit(txt_hintname)
        self.w_hintage = QLineEdit(txt_hintage)
        self.w_hinttest1 = QLineEdit(txt_hinttest1)
        self.w_hinttest2 = QLineEdit(txt_hinttest2)
        self.w_hinttest3 = QLineEdit(txt_hinttest3)
        
        # Кнопки
        self.w_starttest1 = QPushButton(txt_starttest1)
        self.w_starttest2 = QPushButton(txt_starttest2)
        self.w_starttest3 = QPushButton(txt_starttest3)
        self.next_button = QPushButton(txt_sendresults)

        # Прикрепление
        self.line.addWidget(self.w_name, alignment = Qt.AlignLeft)
        self.line.addWidget(self.w_hintname, alignment = Qt.AlignLeft)
        self.line.addWidget(self.w_age, alignment = Qt.AlignLeft)
        self.line.addWidget(self.w_hintage, alignment = Qt.AlignLeft)
        self.line.addWidget(self.w_test1, alignment = Qt.AlignLeft)
        self.line.addWidget(self.w_starttest1, alignment = Qt.AlignLeft)
        self.line.addWidget(self.w_hinttest1, alignment = Qt.AlignLeft)
        self.line.addWidget(self.w_test2, alignment = Qt.AlignLeft)
        self.line.addWidget(self.w_starttest2, alignment = Qt.AlignLeft)
        self.line.addWidget(self.w_hinttest2, alignment = Qt.AlignLeft)
        self.line.addWidget(self.w_test3, alignment = Qt.AlignLeft)
        self.line.addWidget(self.w_starttest3, alignment = Qt.AlignLeft)
        self.line.addWidget(self.w_hinttest3, alignment = Qt.AlignLeft)
        self.line.addWidget(self.next_button, alignment = Qt.AlignRight)
        self.line2.addWidget(self.timer, alignment = Qt.AlignLeft)
        self.gen_line.addLayout(self.line)
        self.gen_line.addLayout(self.line2)
        self.setLayout(self.gen_line)

    def connects(self):
        self.next_button.connect(next_click)
    
    def next_click():
        self.hide()
        # final_win = КЛАСС


if __name__ == '__main__':
    app = QApplication([])
    win = TestWin()
    app.exec_()