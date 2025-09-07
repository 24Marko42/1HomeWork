import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLineEdit, QPushButton, QGridLayout, QVBoxLayout)
from PyQt6.QtCore import Qt

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.expression = ""  
        self.initUI()  
                
    def initUI(self):
        self.setGeometry(300, 300, 300, 400)  
        self.setWindowTitle('Калькулятор')  
        
        
        self.display = QLineEdit('0')  # Начальное значение "0"
        self.display.setReadOnly(True)  # Запрет на прямое редактирование
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)  # Выравнивание по правому краю
        self.display.setFixedHeight(50)  
        self.display.setStyleSheet("font-size: 20px;")  # Размер шрифта
        
        # Сетка для кнопок
        grid = QGridLayout()
        grid.setSpacing(5)  # Расстояние между кнопками
        
        buttons = [
            '7', '8', '9', '/', 'D',  
            '4', '5', '6', '*', 'C',
            '1', '2', '3', '-', '(',
            '0', '.', '=', '+', ')'
        ]
        
        positions = [(i, j) for i in range(4) for j in range(5)]
        
        for position, button in zip(positions, buttons):
            btn = QPushButton(button)
            btn.setFixedSize(50, 50)  # Размер кнопок
            btn.setStyleSheet("font-size: 16px;")  # Размер шрифта на кнопках
            
            # Обработчик нажатия
            if button == '=':
                btn.clicked.connect(self.calculate)
            elif button == 'D':  
                btn.clicked.connect(self.backspace)
            elif button == 'C':  
                btn.clicked.connect(self.clear)
            else:
                btn.clicked.connect(lambda _, b=button: self.append_expression(b))
            
            grid.addWidget(btn, *position)
        
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.display)
        main_layout.addLayout(grid)
        self.setLayout(main_layout)
        
    def append_expression(self, char):
        #Добавляет символ к текущему выражению
        if self.display.text() == '0' or self.display.text() == "Ошибка":
            self.expression = ""
        self.expression += char  
        self.display.setText(self.expression)  
    
    def calculate(self):
        """Вычисляет результат выражения"""
        if not self.expression:
            return
            
        try:
            # Вычисляем результат с помощью eval()
            result = eval(self.expression)
            
            # Если результат целое число, отображаем без десятичной части
            if isinstance(result, float) and result.is_integer():
                result = int(result)
                
            # Обновляем выражение и дисплей
            self.expression = str(result)
            self.display.setText(self.expression)
        except ZeroDivisionError:
            self.display.setText("Ошибка: деление на 0")
            self.expression = ""
        except:
            self.display.setText("Ошибка")
            self.expression = ""
    
    def clear(self):
        """Очищает выражение и дисплей"""
        self.expression = ""
        self.display.setText('0')
    
    def backspace(self):
        """Удаляет последний символ из выражения"""
        if self.expression:
            # Удаляем последний символ
            self.expression = self.expression[:-1]
            
            # Если выражение пустое, показываем "0"
            if not self.expression:
                self.display.setText('0')
            else:
                self.display.setText(self.expression)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec())