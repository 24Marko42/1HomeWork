import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QCheckBox, QSpinBox, QLabel, QPlainTextEdit, QPushButton
)
from PyQt6.QtCore import Qt


class RestaurantOrderApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Устанавливаем заголовок окна
        self.setWindowTitle('Заказ в ресторане')

        # Основной вертикальный макет
        main_layout = QVBoxLayout()

        # Заголовок для меню
        menu_label = QLabel('Меню:')
        menu_label.setStyleSheet("font-weight: bold; font-size: 14px;")
        main_layout.addWidget(menu_label)

        # Список блюд: (название, цена за порцию)
        self.menu_items = [
            ("Борщ", 150),
            ("Пельмени", 200),
            ("Стейк", 600),
            ("Салат Цезарь", 250),
            ("Картофель фри", 80),
            ("Чай", 40),
            ("Кофе", 70)
        ]

        # Список виджетов для управления заказом
        self.checkboxes = []
        self.spin_boxes = []

        # Создаём строки для каждого блюда
        for name, price in self.menu_items:
            # Горизонтальный макет для одной строки (блюдо + чекбокс + спинбокс + цена)
            row_layout = QHBoxLayout()

            # Чекбокс для выбора блюда
            checkbox = QCheckBox(name)
            checkbox.stateChanged.connect(self.update_bill)  # При изменении — обновляем чек
            row_layout.addWidget(checkbox)

            # Спинбокс для выбора количества
            spinbox = QSpinBox()
            spinbox.setRange(0, 99)  # от 0 до 99 порций
            spinbox.setEnabled(False)  # по умолчанию отключён
            spinbox.valueChanged.connect(self.update_bill)  # при изменении количества — обновляем чек
            row_layout.addWidget(spinbox)

            # Метка с ценой за порцию
            price_label = QLabel(f"{price} ₽")
            price_label.setAlignment(Qt.AlignRight)
            row_layout.addWidget(price_label)

            # Сохраняем ссылки на виджеты
            self.checkboxes.append(checkbox)
            self.spin_boxes.append(spinbox)

            # Подключаем чекбокс к функции включения/выключения спинбокса
            checkbox.stateChanged.connect(
                lambda state, sb=spinbox: sb.setEnabled(state == Qt.Checked)
            )

            # Добавляем строку в основной макет
            main_layout.addLayout(row_layout)

        # Кнопка "Очистить заказ"
        clear_button = QPushButton("Очистить заказ")
        clear_button.clicked.connect(self.clear_order)
        main_layout.addWidget(clear_button)

        # Поле для вывода чека
        self.bill_display = QPlainTextEdit()
        self.bill_display.setPlaceholderText("Здесь будет ваш чек...")
        self.bill_display.setReadOnly(True)
        main_layout.addWidget(self.bill_display)

        # Устанавливаем макет окну
        self.setLayout(main_layout)

        # Устанавливаем размер окна
        self.resize(500, 600)

        # Показываем окно
        self.show()

        # Инициализируем чек (сразу обновляем)
        self.update_bill()

    def update_bill(self):
        """
        Обновляет содержимое чека на основе выбранных блюд и количества.
        """
        total = 0
        bill_lines = []
        bill_lines.append("🧾 ЧЕК ЗАКАЗА\n")
        bill_lines.append(f"{'Блюдо':<20} {'Кол-во':<8} {'Стоимость'}")
        bill_lines.append("-" * 40)

        # Проходим по всем блюдам
        for i, (name, price) in enumerate(self.menu_items):
            checkbox = self.checkboxes[i]
            spinbox = self.spin_boxes[i]
            quantity = spinbox.value()

            # Если блюдо выбрано или количество > 0
            if checkbox.isChecked() or quantity > 0:
                # Убедимся, что спинбокс включён и чекбокс установлен
                if not checkbox.isChecked():
                    checkbox.setChecked(True)  # Автоматически ставим галочку, если количество > 0
                    spinbox.setEnabled(True)

                item_cost = price * quantity
                total += item_cost
                bill_lines.append(f"{name:<20} {quantity:<8} {item_cost} ₽")

        # Добавляем итог
        bill_lines.append("-" * 40)
        bill_lines.append(f"{'ИТОГО':<30} {total} ₽")

        # Обновляем текст в чеке
        self.bill_display.setPlainText("\n".join(bill_lines))

    def clear_order(self):
        """
        Сбрасывает весь заказ: убирает галочки, обнуляет количество.
        """
        for checkbox in self.checkboxes:
            checkbox.setChecked(False)
        for spinbox in self.spin_boxes:
            spinbox.setValue(0)
        # update_bill вызывается автоматически через сигналы


# Основная функция запуска приложения
def main():
    app = QApplication(sys.argv)
    window = RestaurantOrderApp()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()