import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Калькулятор')
        
        # Ввода выражения
        self.expression_input = QLineEdit(self)
        self.expression_input.move(50, 60)
        self.expression_input.resize(200, 30)
        self.expression_input.setPlaceholderText("Введите выражение...")
        
        # Вывод результата
        self.result_output = QLineEdit(self)
        self.result_output.move(50, 170)
        self.result_output.resize(200, 30)
        self.result_output.setReadOnly(True)
        self.result_output.setPlaceholderText("Результат")
        
        self.calc_button = QPushButton("Вычислить", self)
        self.calc_button.move(100, 120)
        self.calc_button.resize(100, 30)
        
        self.calc_button.clicked.connect(self.calculate)

    
    def calculate(self):
        expression = self.expression_input.text()
        try:
            result = eval(expression)
            self.result_output.setText(str(result))
        except:
            self.result_output.setText("Ошибка")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec())