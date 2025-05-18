from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QMessageBox, QVBoxLayout, QHBoxLayout
from instr import *
from final_win import *
from PyQt5.QtGui import QFont

class Exp():
    def __init__(self, age, t1, t2, t3):
        self.age = age
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

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
        self.text_timer = QLabel('00:00:00')
        self.text_timer.setFont(QFont('Arial', 36, QFont.Bold))

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
        self.line2.addWidget(self.text_timer, alignment = Qt.AlignLeft)
        self.gen_line.addLayout(self.line)
        self.gen_line.addLayout(self.line2)
        self.setLayout(self.gen_line)

    # Первый таймер и его обработка
    def timer_test(self):
        global time
        time = QTime(0,0,15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)
    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:mm:ss'))
        self.text_timer.setFont(QFont('Arial',36, QFont.Bold))
        self.text_timer.setStyleSheet('color: rgb(0,0,0)')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()
    
    # Второй таймер и его обработка
    def timer_sits(self):
        global time
        time = QTime(0,0,30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)
    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:mm:ss')[6:8])
        self.text_timer.setFont(QFont('Arial',36, QFont.Bold))
        self.text_timer.setStyleSheet('color: rgb(0,0,0)')
        if time.toString('hh:mm:ss'[6:8]) == '00':
            self.timer.stop()

    # Третий таймер и его обработка
    def timer_final(self):
        global time
        time = QTime(0,1,0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)
    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:mm:ss')[6:8])
        self.text_timer.setFont(QFont('Arial',36, QFont.Bold))
        if int(time.toString('hh:mm:ss')[6:8]) >= 45:
            self.text_timer.setStyleSheet('color: rgb(0,255,0)')
        elif int(time.toString('hh:mm:ss')[6:8]) <= 15:
            self.text_timer.setStyleSheet('color: rgb(0,255,0)')
        else:
            self.text_timer.setStyleSheet('color: rgb(0,0,0)')
        if time.toString('hh:mm:ss'[6:8]) == '00':
            self.timer.stop()

    # Проверка нажатий
    def connects(self):
        self.next_button.clicked.connect(self.next_click)
        self.w_starttest1.clicked.connect(self.timer_test)
        self.w_starttest2.clicked.connect(self.timer_sits)
        self.w_starttest3.clicked.connect(self.timer_final)
    
    # Переход на другое окно
    def next_click(self):
        self.hide()
        exp = Exp(self.w_hintage.text(), self.w_hinttest1.text(), self.w_hinttest2.text(), self.w_hinttest3.text())
        self.final_win = FinalWin(exp)

if __name__ == '__main__':
    app = QApplication([])
    win = TestWin()
    app.exec_()