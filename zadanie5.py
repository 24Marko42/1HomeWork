import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QCheckBox, QSpinBox, QLabel, QPlainTextEdit, QPushButton, QVBoxLayout, QHBoxLayout
)

class RestaurantOrder(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
     
        self.setGeometry(300, 300, 500, 400)
        self.setWindowTitle("Marko's bar")
        
        main_layout = QVBoxLayout()
        
        # Cписок блюд с ценами
        self.menu_items = [
            ("Pivo", 150),
            ("Viski", 200),
            ("Stake", 600),
            ("Salat", 250),
            ("Coffee", 70)
        ]

        self.widget_pairs = []
        for name, price in self.menu_items:
            row_layout = QHBoxLayout()
            
            # Чекбокс для выбора блюда
            checkbox = QCheckBox(name)
            row_layout.addWidget(checkbox)
            
            # Спинбокс для выбора количества
            spinbox = QSpinBox()
            spinbox.setRange(0, 10)  # от 0 до 10 порций
            spinbox.setEnabled(False)  # по умолчанию отключен
            row_layout.addWidget(spinbox)
            
            # Метка с ценой
            price_label = QLabel(f"{price} ₽")
            row_layout.addWidget(price_label)
            self.widget_pairs.append((checkbox, spinbox, price))
            checkbox.stateChanged.connect(self.update_bill)
            spinbox.valueChanged.connect(self.update_bill)
           
            checkbox.stateChanged.connect(
                lambda state, sb=spinbox: sb.setEnabled(state == 2)
            )
            
            # 8. Если количество изменяется, устанавливаем чекбокс
            spinbox.valueChanged.connect(
                lambda value, cb=checkbox: cb.setChecked(value > 0)
            )
            
            main_layout.addLayout(row_layout)

        clear_btn = QPushButton("Очистить заказ")
        clear_btn.clicked.connect(self.clear_order)
        main_layout.addWidget(clear_btn)
        
        # Чек
        self.bill_display = QPlainTextEdit()
        self.bill_display.setReadOnly(True)
        self.bill_display.setPlaceholderText("Ваш заказ появится здесь...")
        main_layout.addWidget(self.bill_display)
        
        self.setLayout(main_layout)
        
        # Инициализируем чек
        self.update_bill()

    def update_bill(self):
        total = 0
        bill_lines = ["ЧЕК ЗАКАЗА\n"]
        bill_lines.append(f"{'Блюдо':<15} {'Кол-во':<8} {'Стоимость'}")
        bill_lines.append("-" * 35)
        
        # Проход по всем блюдам
        for (checkbox, spinbox, price) in self.widget_pairs:
            quantity = spinbox.value()
            
            if checkbox.isChecked() or quantity > 0:
                # Устанавливаем количество в 1, если чекбокс включен, но количество 0
                if checkbox.isChecked() and quantity == 0:
                    spinbox.setValue(1)
                    quantity = 1
                
                item_cost = price * quantity
                total += item_cost
                
                bill_lines.append(f"{checkbox.text():<15} {quantity:<8} {item_cost} ₽")
        bill_lines.append("-" * 35)
        bill_lines.append(f"{'ИТОГО':<23} {total} ₽")
 
        self.bill_display.setPlainText("\n".join(bill_lines))
    
    def clear_order(self):
        for (checkbox, spinbox, _) in self.widget_pairs:
            checkbox.setChecked(False)
            spinbox.setValue(0)
        self.update_bill()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RestaurantOrder()
    ex.show()
    sys.exit(app.exec())