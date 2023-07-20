from PyQt5.QtWidgets import *
from os import system

system("cls")

class Button(QPushButton):
    def __init__(self, btn):
        super().__init__(btn)
        self.style = """
            background-color: #529bb7;
            font-size: 60px;
        """
        self.setFixedSize(135, 135)
        self.setStyleSheet(self.style)

    def addStyle(self, st):
        self.setStyleSheet(self.style + st)
        


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.turn = 0
        self.score_x = 0
        self.score_o = 0
        self.design()
        self.clear_btn.clicked.connect(self.clear_function)
        self.new_game_btn.clicked.connect(self.new_game_function)

        self.buttons[0][0].clicked.connect(lambda: self.bosildi(0, 0))
        self.buttons[0][1].clicked.connect(lambda: self.bosildi(0, 1))
        self.buttons[0][2].clicked.connect(lambda: self.bosildi(0, 2))
        self.buttons[1][0].clicked.connect(lambda: self.bosildi(1, 0))
        self.buttons[1][1].clicked.connect(lambda: self.bosildi(1, 1))
        self.buttons[1][2].clicked.connect(lambda: self.bosildi(1, 2))
        self.buttons[2][0].clicked.connect(lambda: self.bosildi(2, 0))
        self.buttons[2][1].clicked.connect(lambda: self.bosildi(2, 1))
        self.buttons[2][2].clicked.connect(lambda: self.bosildi(2, 2))

        self.show()

    def clear_function(self):
        for i in range(len(self.buttons)):
            for k in range(len(self.buttons[i])):
                self.buttons[i][k].setEnabled(True)
                self.buttons[i][k].setText("")
                self.buttons[i][k].setStyleSheet("""
                    background-color: #529bb7;
                    font-size: 60px;
                """)
        self.turn = 0
        self.turn_label.setText("X ni navbati")
        self.turn_label.setStyleSheet("""
            color: black;
            font-size: 20px;
        """)
        self.X_score_label.setText("X: "+ str(self.score_x))
        self.O_score_label.setText("O: "+ str(self.score_o))

    def new_game_function(self):
        self.clear_function()
        self.score_x = 0
        self.score_o = 0
        self.X_score_label.setText("X: "+ str(self.score_x))
        self.O_score_label.setText("O: "+ str(self.score_o))

    def checked_win_function(self, btn1, btn2, btn3):
        if not (btn1.text() == btn2.text() and btn2.text() == btn3.text() and btn3.text() == btn1.text() and btn1.text() != "" and btn2.text() != "" and btn3.text() != ""):
            return 0
        for i in range(len(self.buttons)):
            for k in range(len(self.buttons[i])):
                if len(self.buttons[i][k].text()) == 0:
                    self.buttons[i][k].setEnabled(False)
        btn1.setStyleSheet("""
            background-color: red;
            font-size: 60px;
        """)
        btn2.setStyleSheet("""
            background-color: red;
            font-size: 60px;
        """)
        btn3.setStyleSheet("""
            background-color: red;
            font-size: 60px;
        """)
        self.turn = 0
        self.turn_label.setText("X ni navbati")
        if btn1.text() == "X":
            self.score_x += 1 
        else: self.score_o += 1
        self.X_score_label.setText("X: "+ str(self.score_x))
        self.O_score_label.setText("O: "+ str(self.score_o))
        self.turn_label.setText(btn1.text() + "  yutdi!")
        self.turn_label.setStyleSheet("""
            color: green;
            font-size: 30px;
        """)

    def checked_draw_function(self):
        check = 0
        for i in range(3):
            for k in range(3):
                if len(self.buttons[i][k].text()) == 0:
                    check += 1
        if check: return 0
        self.turn_label.setText("Durrang")
        self.turn_label.setStyleSheet("""
            color: green;
            font-size: 35px;
        """)
        


    def design(self):
        self.main_layout = QVBoxLayout(self)
        self.setStyleSheet("""
            background-color: #a8ccf1;
            font-size: 20px;
            font-family: Calibri;
        """)

        self.setWindowTitle("TicTacToe")
        self.setFixedSize(500, 630)
        score_layout = QVBoxLayout()

        self.X_score_label = QLabel(self)
        self.X_score_label.setText("X: 0")
        self.X_score_label.adjustSize()

        self.O_score_label = QLabel(self)
        self.O_score_label.setText("O: 0")
        self.O_score_label.adjustSize()

        score_layout.addWidget(self.X_score_label)
        score_layout.addWidget(self.O_score_label)

        self.turn_label = QLabel(self)
        self.turn_label.setText("X ni navbati")


        header_layout = QHBoxLayout()
        header_layout.addLayout(score_layout)
        header_layout.addStretch(3)
        header_layout.addWidget(self.turn_label)
        header_layout.addStretch(5)

        self.buttons = list()
        buttons_layout = QVBoxLayout()
        for i in range(3):
            button_h_layout = QHBoxLayout()
            qator = list()
            for k in range(3):
                btn = Button(self)
                qator.append(btn)
                button_h_layout.addWidget(btn)
                button_h_layout.addStretch()
            buttons_layout.addLayout(button_h_layout)
            self.buttons.append(qator)
            buttons_layout.addStretch()
                
        self.clear_btn = Button(self)
        self.clear_btn.setFixedSize(120, 50)
        self.clear_btn.setText("Clear")
        self.clear_btn.addStyle("font-size: 18px; bg-color: ")

        self.new_game_btn = Button(self)
        self.new_game_btn.setFixedSize(120, 50)
        self.new_game_btn.setText("New Game")
        self.new_game_btn.addStyle("font-size: 18px; bg-color: ")

        self.restart_layout = QHBoxLayout()
        self.restart_layout.addStretch(20)
        self.restart_layout.addWidget(self.new_game_btn)
        self.restart_layout.addWidget(self.clear_btn)
        self.restart_layout.addStretch(25)

        self.main_layout.addLayout(header_layout)
        self.main_layout.addLayout(buttons_layout)
        self.main_layout.addLayout(self.restart_layout)

    def bosildi(self, s: int, q: int):

        if len(self.buttons[s][q].text()) > 0:
            return 0
        self.buttons[s][q].setText('X' if self.turn % 2 == 0 else 'O')
        self.turn_label.setText('O ni navbati' if self.turn % 2 == 0 else 'X ni navbati')
        self.turn += 1
        self.checked(self.buttons)
    def checked(self, buttons):
            self.checked_win_function(buttons[0][0], buttons[1][0], buttons[2][0])
            self.checked_win_function(buttons[0][1], buttons[1][1], buttons[2][1])
            self.checked_win_function(buttons[0][2], buttons[1][2], buttons[2][2])        
            self.checked_win_function(buttons[0][0], buttons[0][1], buttons[0][2])
            self.checked_win_function(buttons[1][0], buttons[1][1], buttons[1][2])
            self.checked_win_function(buttons[2][0], buttons[2][1], buttons[2][2])
            self.checked_win_function(buttons[0][0], buttons[1][1], buttons[2][2])
            self.checked_win_function(buttons[0][2], buttons[1][1], buttons[2][0])
            self.checked_draw_function()
            
        

app = QApplication([])

window = Window()

app.exec_()