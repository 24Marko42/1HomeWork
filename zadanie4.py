import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLineEdit, QLabel
)

# Словарь с азбукой Морзе для латинских букв A-Z
MORSE_CODE = {
    'A': '.-',   'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.',  'H': '....', 'I': '..',  'J': '.---',
    'K': '-.-',  'L': '.-..', 'M': '--',   'N': '-.',  'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',  'S': '...', 'T': '-',
    'U': '..-',  'V': '...-', 'W': '.--',  'X': '-..-', 'Y': '-.--',
    'Z': '--..'
}


class MorseCodeApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Устанавливаем заголовок окна
        self.setWindowTitle('Азбука Морзе — Пишем кнопками')

        # Основной вертикальный макет
        layout = QVBoxLayout()

        # Подпись к полю ввода
        label = QLabel('Текст в азбуке Морзе:')
        layout.addWidget(label)

        # Поле для вывода кода Морзе
        self.morse_display = QLineEdit(self)
        self.morse_display.setReadOnly(True)  # Только для чтения
        self.morse_display.setPlaceholderText('Здесь будет код Морзе...')
        layout.addWidget(self.morse_display)

        # Создаём сетку для кнопок (например, 5 столбцов)
        grid_layout = QHBoxLayout()
        row_layout = QHBoxLayout()
        buttons_per_row = 9  # Сколько кнопок в ряду

        # Проходим по всем латинским буквам от A до Z
        for i, letter in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            # Создаём кнопку с буквой
            btn = QPushButton(letter, self)

            # Подключаем нажатие кнопки к обработчику, передавая букву через lambda
            btn.clicked.connect(lambda ch, l=letter: self.add_morse_code(l))

            # Добавляем кнопку в текущую строку
            row_layout.addWidget(btn)

            # Если в строке уже buttons_per_row кнопок — начинаем новую строку
            if (i + 1) % buttons_per_row == 0:
                grid_layout.addLayout(row_layout)
                row_layout = QHBoxLayout()  # Новая строка

        # Добавляем остаток (если есть)
        if not row_layout.isEmpty():
            grid_layout.addLayout(row_layout)

        # Добавляем сетку кнопок в основной макет
        layout.addLayout(grid_layout)

        # Кнопка "Очистить" (опционально)
        clear_btn = QPushButton('Очистить', self)
        clear_btn.clicked.connect(self.clear_display)
        layout.addWidget(clear_btn)

        # Устанавливаем макет окну
        self.setLayout(layout)

        # Устанавливаем размер окна
        self.resize(800, 300)

        # Показываем окно
        self.show()

    def add_morse_code(self, letter):
        """
        Добавляет код буквы в поле ввода.
        :param letter: символ латинской буквы (например, 'A')
        """
        # Получаем код Морзе для буквы
        code = MORSE_CODE.get(letter.upper(), '?')  # если вдруг нет — ставим ?

        # Получаем текущий текст из поля
        current_text = self.morse_display.text()

        # Если поле не пустое — добавляем пробел перед новым кодом
        separator = ' ' if current_text else ''

        # Обновляем текст
        self.morse_display.setText(current_text + separator + code)

    def clear_display(self):
        """Очищает поле ввода."""
        self.morse_display.clear()


# Основная функция запуска приложения
def main():
    app = QApplication(sys.argv)
    window = MorseCodeApp()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()