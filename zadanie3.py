import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QLineEdit, QCheckBox
)
from PyQt6.QtCore import Qt

class CheckboxHider(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Устанавливаем заголовок окна
        self.setWindowTitle('Управление видимостью через QCheckBox')

        # Основной вертикальный макет
        main_layout = QVBoxLayout()

        # Список пар: (виджет, чекбокс)
        # Мы будем хранить их, чтобы легко связать
        self.widget_checkbox_pairs = []

        # Создаём несколько виджетов и чекбоксов
        items = [
            ("Метка", QLabel("Это QLabel — текстовая метка")),
            ("Кнопка", QPushButton("Это QPushButton")),
            ("Поле ввода", QLineEdit("Это QLineEdit")),
        ]

        for label_text, widget in items:
            # Горизонтальный макет для каждой пары
            row_layout = QHBoxLayout()

            # Создаём чекбокс с подписью
            checkbox = QCheckBox(label_text)
            checkbox.setChecked(True)  # По умолчанию виджет видим

            # Добавляем чекбокс в макет слева
            row_layout.addWidget(checkbox)

            # Добавляем сам виджет
            row_layout.addWidget(widget)

            # Добавляем строку в основной макет
            main_layout.addLayout(row_layout)

            # Сохраняем пару: чекбокс и виджет
            self.widget_checkbox_pairs.append((widget, checkbox))

            # Подключаем сигнал чекбокса к универсальному обработчику
            checkbox.stateChanged.connect(self.toggle_widget_visibility)

        # Устанавливаем макет окну
        self.setLayout(main_layout)

        # Устанавливаем размер окна
        self.resize(400, 200)

        # Показываем окно
        self.show()

    def toggle_widget_visibility(self):
        """
        Универсальный обработчик изменения состояния чекбокса.
        Проходит по всем парам (виджет, чекбокс) и устанавливает видимость
        виджета в зависимости от состояния его чекбокса.
        """
        # Получаем объект, который вызвал сигнал (какой чекбокс был изменён)
        sender = self.sender()  # Это QCheckBox

        # Проходим по всем парам
        for widget, checkbox in self.widget_checkbox_pairs:
            # Обновляем видимость виджета в зависимости от состояния его чекбокса
            if checkbox.isChecked():
                widget.setVisible(True)
            else:
                widget.setVisible(False)


# Основная функция запуска приложения
def main():
    app = QApplication(sys.argv)
    window = CheckboxHider()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()