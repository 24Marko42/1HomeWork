import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel
from PyQt6.QtCore import Qt

class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Устанавливаем заголовок окна
        self.setWindowTitle('Простой калькулятор выражений')

        # Основной вертикальный макет
        layout = QVBoxLayout()

        # Подпись к первому полю
        input_label = QLabel('Введите арифметическое выражение:')
        layout.addWidget(input_label)

        # Поле для ввода выражения
        self.expression_input = QLineEdit(self)
        self.expression_input.setPlaceholderText('Например: 5 + 3 * 2')
        layout.addWidget(self.expression_input)

        # Кнопка для вычисления
        self.calc_button = QPushButton('Вычислить', self)
        self.calc_button.clicked.connect(self.calculate)  # Привязываем функцию к кнопке
        layout.addWidget(self.calc_button)

        # Подпись ко второму полю
        result_label = QLabel('Результат:')
        layout.addWidget(result_label)

        # Поле для вывода результата (только для чтения)
        self.result_output = QLineEdit(self)
        self.result_output.setReadOnly(True)  # Пользователь не может редактировать
        self.result_output.setPlaceholderText('Здесь появится результат')
        layout.addWidget(self.result_output)

        # Устанавливаем макет окну
        self.setLayout(layout)

        # Устанавливаем размеры окна
        self.resize(400, 200)

        # Показываем окно
        self.show()

    def calculate(self):
        """
        Метод вызывается при нажатии на кнопку "Вычислить".
        Получает текст из поля ввода, вычисляет его с помощью eval(),
        и выводит результат. Если есть ошибка — показывает сообщение об ошибке.
        """
        # Получаем текст из поля ввода
        expression = self.expression_input.text().strip()

        # Проверяем, не пустое ли поле
        if not expression:
            self.result_output.setText("Ошибка: пустое выражение")
            return

        try:
            # Используем eval() для вычисления выражения
            # Например: "2 + 3 * 4" → 14
            result = eval(expression)

            # Преобразуем результат в строку и выводим
            self.result_output.setText(str(result))

        except SyntaxError:
            # Если ошибка в синтаксисе (например, "2 + + 3")
            self.result_output.setText("Ошибка: синтаксис")

        except ZeroDivisionError:
            # Если деление на ноль
            self.result_output.setText("Ошибка: деление на ноль")

        except Exception as e:
            # Любая другая ошибка (например, использование недопустимых имён)
            self.result_output.setText(f"Ошибка: {str(e)}")


# Основная функция запуска приложения
def main():
    app = QApplication(sys.argv)  # Создаём приложение
    window = CalculatorApp()      # Создаём главное окно
    sys.exit(app.exec())         # Запускаем цикл событий


# Запускаем программу, если файл запущен напрямую
if __name__ == '__main__':
    main()