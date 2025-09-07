import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton

class word_switch(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        
        self.setGeometry(300, 300, 500, 200)
        self.setWindowTitle('Перекидыватель слов')
        
        # Создаем первое и второе поля ввода
        self.input1 = QLineEdit(self)
        self.input1.move(150, 30)
        self.input1.resize(200, 30)
        self.input1.setPlaceholderText("Введите текст здесь...")
        
        self.input2 = QLineEdit(self)
        self.input2.move(150, 130)
        self.input2.resize(200, 30)
        self.input2.setPlaceholderText("Сюда перейдет текст...")
        
        # Кнопка со стрелкой
        self.button = QPushButton("↓", self)
        self.button.move(225, 80)
        self.button.resize(50, 30)
                
        self.button.clicked.connect(self.transfer_text)
        
        # Буллево значение направления (True = input1 → input2, False = input2 → input1)
        self.direction_forward = True
            
    def transfer_text(self):
        if self.direction_forward:
            # Перекидываем из первого поля во второе
            text = self.input1.text()
            self.input2.setText(text)
            self.input1.clear()
            self.button.setText("↑")
        else:
            # Перекидываем из второго поля в первое
            text = self.input2.text()
            self.input1.setText(text)
            self.input2.clear()
            self.button.setText("↓")
        
        # Меняем направление для следующего нажатия
        self.direction_forward = not self.direction_forward


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = word_switch()
    ex.show()
    sys.exit(app.exec())