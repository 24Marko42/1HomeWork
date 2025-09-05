import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QGridLayout

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.expression = ""  # Текущее выражение
        self.initUI()
        
    def initUI(self):
        # Настройки окна
        self.setGeometry(300, 300, 280, 350)
        self.setWindowTitle('Калькулятор')
        
        # Дисплей
        self.display = QLineEdit('0')
        self.display.setReadOnly(True)
        self.display.setAlignment(2)  # Выравнивание по правому краю
        self.display.setFixedHeight(50)
        
        # Сетка для кнопок
        grid = QGridLayout()
        
        # Кнопки калькулятора
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', 'C', '+',
            '='
        ]
        
        # Расположение кнопок
        positions = [(i, j) for i in range(4) for j in range(4)]
        positions.append((4, 0, 1, 4))  # '=' занимает всю нижнюю строку
        
        # Создание кнопок
        for i, button in enumerate(buttons):
            btn = QPushButton(button)
            btn.setFixedSize(60, 50)
            
            # Подключение обработчика
            btn.clicked.connect(lambda _, b=button: self.button_clicked(b))
            
            # Добавление в сетку
            if i < 16:
                grid.addWidget(btn, *positions[i])
            else:
                grid.addWidget(btn, *positions[i])
        
        # Основной макет
        main_layout = grid
        main_layout.addWidget(self.display, 0, 0, 1, 4)
        
        self.setLayout(main_layout)
        self.show()
    
    def button_clicked(self, button):
        """Обработка нажатия кнопки"""
        if button == 'C':
            # Очистка
            self.expression = ""
            self.display.setText('0')
        
        elif button == '=':
            # Вычисление
            if not self.expression:
                return
                
            try:
                # Разбиваем выражение на числа и операции
                tokens = []
                current = ""
                
                for char in self.expression:
                    if char in '+-*/':
                        if current: tokens.append(current)
                        tokens.append(char)
                        current = ""
                    else:
                        current += char
                if current: tokens.append(current)
                
                # Начинаем с первого числа
                result = float(tokens[0])
                
                # Выполняем операции последовательно
                for i in range(1, len(tokens), 2):
                    op = tokens[i]
                    num = float(tokens[i+1])
                    
                    if op == '+': result += num
                    elif op == '-': result -= num
                    elif op == '*': result *= num
                    elif op == '/': 
                        if num == 0:
                            self.display.setText("Ошибка: деление на 0")
                            return
                        result /= num
                
                # Отображаем результат
                self.display.setText(str(int(result) if result.is_integer() else result))
                self.expression = str(result)
                
            except:
                self.display.setText("Ошибка")
                self.expression = ""
        
        else:
            # Добавление символа в выражение
            self.expression += button
            self.display.setText(self.expression)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    sys.exit(app.exec())