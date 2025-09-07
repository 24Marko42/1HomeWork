import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout, QGridLayout

class MorseCodeApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('Азбука Морзе')

        main_layout = QVBoxLayout()

        self.morse_display = QLineEdit()
        self.morse_display.setReadOnly(True) 
        self.morse_display.setPlaceholderText("Код Морзе появится здесь...")
        main_layout.addWidget(self.morse_display)

        grid_layout = QGridLayout()
        
        # Словарь с азбукой Морзе
        self.morse_dict = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
            'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
            'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
            'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
            'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..'
        }
        
        row, col = 0, 0
        for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            btn = QPushButton(letter)
            
            btn.clicked.connect(lambda checked, l=letter: self.add_morse_code(l))
        
            grid_layout.addWidget(btn, row, col)
            
            col += 1
            if col > 7:
                col = 0
                row += 1
        
        main_layout.addLayout(grid_layout)
        
        clear_btn = QPushButton("Очистить")
        clear_btn.clicked.connect(self.clear_display)
        main_layout.addWidget(clear_btn)

        self.setLayout(main_layout)
        
        self.show()
    
    def add_morse_code(self, letter):
        code = self.morse_dict[letter]
        
        current_text = self.morse_display.text()
        
        if current_text:
            new_text = f"{current_text} {code}"
        else:
            new_text = code
        
        self.morse_display.setText(new_text)
    
    def clear_display(self):
        """Очищает поле отображения кода Морзе"""
        self.morse_display.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MorseCodeApp()
    ex.show()
    sys.exit(app.exec())