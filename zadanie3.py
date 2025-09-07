import sys
from PyQt6.QtWidgets import QApplication, QWidget, QCheckBox, QLabel, QPushButton, QLineEdit

class VisibilityController(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Видимость виджетов')
        
        self.widget_pairs = []
        
        # Пара 1: QLabel
        label = QLabel("Это метка", self)
        label.move(180, 34)
        checkbox1 = QCheckBox("Показать метку", self)
        checkbox1.move(10, 30)
        checkbox1.setChecked(True)  # По умолчанию видима
        self.widget_pairs.append((checkbox1, label))
        
        # Пара 2: QPushButton
        button = QPushButton("Это кнопка", self)
        button.move(180, 80)
        checkbox2 = QCheckBox("Показать кнопку", self)
        checkbox2.move(10, 80)
        checkbox2.setChecked(True)  # По умолчанию видима
        self.widget_pairs.append((checkbox2, button))
        
        # Пара 3: QLineEdit
        line_edit = QLineEdit(self)
        line_edit.setPlaceholderText("Введите текст...")
        line_edit.move(150, 130)
        checkbox3 = QCheckBox("Показать поле", self)
        checkbox3.move(10, 130)
        checkbox3.setChecked(True)  # По умолчанию видимо
        self.widget_pairs.append((checkbox3, line_edit))
        
        # Подключаем все чекбоксы к ОДНОМУ обработчику
        for checkbox, _ in self.widget_pairs:
            checkbox.stateChanged.connect(self.isibility)
    
    def isibility(self):
        # Получаем чекбокс, который отправил сигнал
        sender = self.sender()
        
        # Проходим по всем парам в поисках нужной
        for checkbox, widget in self.widget_pairs:
            if checkbox == sender:
                # Устанавливаем видимость виджета
                widget.setVisible(checkbox.isChecked())
                break


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = VisibilityController()
    ex.show()
    sys.exit(app.exec())