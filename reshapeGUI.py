import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QCheckBox
from PyQt6.QtGui import QFont
from arabic_reshaper import ArabicReshaper
import qdarktheme

__version__ = "2.0.0"

configuration = {
    'delete_harakat': False
}

reshaper = ArabicReshaper(configuration=configuration)

reverse_reshaper_dict = {
    'ﺍ': 'ا', 'ﺄ': 'ا', 'ﺇ': 'ا', 'ﺃ': 'ا',
    'ﺏ': 'ب', 'ﺐ': 'ب', 'ﺒ': 'ب', 'ﺑ': 'ب',
    'ﺕ': 'ت', 'ﺖ': 'ت', 'ﺘ': 'ت', 'ﺗ': 'ت',
    'ﺙ': 'ث', 'ﺚ': 'ث', 'ﺜ': 'ث', 'ﺛ': 'ث',
    'ﺝ': 'ج', 'ﺞ': 'ج', 'ﺠ': 'ج', 'ﺟ': 'ج',
    'ﺡ': 'ح', 'ﺢ': 'ح', 'ﺤ': 'ح', 'ﺣ': 'ح',
    'ﺥ': 'خ', 'ﺦ': 'خ', 'ﺨ': 'خ', 'ﺧ': 'خ',
    'ﺩ': 'د', 'ﺪ': 'د',
    'ﺫ': 'ذ', 'ﺬ': 'ذ',
    'ﺭ': 'ر', 'ﺮ': 'ر',
    'ﺯ': 'ز', 'ﺰ': 'ز',
    'ﺱ': 'س', 'ﺲ': 'س', 'ﺴ': 'س', 'ﺳ': 'س',
    'ﺵ': 'ش', 'ﺶ': 'ش', 'ﺸ': 'ش', 'ﺷ': 'ش',
    'ﺹ': 'ص', 'ﺺ': 'ص', 'ﺼ': 'ص', 'ﺻ': 'ص',
    'ﺽ': 'ض', 'ﺾ': 'ض', 'ﻀ': 'ض', 'ﺿ': 'ض',
    'ﻁ': 'ط', 'ﻂ': 'ط', 'ﻄ': 'ط', 'ﻃ': 'ط',
    'ﻅ': 'ظ', 'ﻆ': 'ظ', 'ﻈ': 'ظ', 'ﻇ': 'ظ',
    'ﻉ': 'ع', 'ﻊ': 'ع', 'ﻌ': 'ع', 'ﻋ': 'ع',
    'ﻍ': 'غ', 'ﻎ': 'غ', 'ﻐ': 'غ', 'ﻏ': 'غ',
    'ﻑ': 'ف', 'ﻒ': 'ف', 'ﻔ': 'ف', 'ﻓ': 'ف',
    'ﻕ': 'ق', 'ﻖ': 'ق', 'ﻘ': 'ق', 'ﻗ': 'ق',
    'ﻙ': 'ك', 'ﻚ': 'ك', 'ﻜ': 'ك', 'ﻛ': 'ك',
    'ﻝ': 'ل', 'ﻞ': 'ل', 'ﻠ': 'ل', 'ﻟ': 'ل',
    'ﻡ': 'م', 'ﻢ': 'م', 'ﻤ': 'م', 'ﻣ': 'م',
    'ﻥ': 'ن', 'ﻦ': 'ن', 'ﻨ': 'ن', 'ﻧ': 'ن',
    'ﻩ': 'ه', 'ﻪ': 'ه', 'ﻬ': 'ه', 'ﻫ': 'ه',
    'ﻭ': 'و', 'ﻮ': 'و',
    'ﻱ': 'ي', 'ﻲ': 'ي', 'ﻴ': 'ي', 'ﻳ': 'ي',
    'ﻻ': 'لا',
    'ﺎ': 'ا',
    'ﺔ': 'ة',
}

class ArabicReshaperApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.setGeometry(100, 100, 400, 650)


    def initUI(self):
        self.setWindowTitle("Ara Reshaper UI")

        self.arabic_font = QFont("Arial", 18)

        self.label_input = QLabel("Enter text:")
        self.text_input = QTextEdit()
        # self.text_input.setFont(self.arabic_font)
        self.text_input.textChanged.connect(self.take_input)
        self.text_input.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.checkbox = QCheckBox("Include {a:r:}")
        self.checkbox.stateChanged.connect(self.take_input)

        self.btn_paste = QPushButton("Paste")
        self.btn_paste.clicked.connect(self.paste_text)

        self.btn_copy_output = QPushButton("Copy Output")
        self.btn_copy_output.clicked.connect(lambda: self.copy_output(self.text_output))

        self.btn_delete = QPushButton("Delete")
        self.btn_delete.clicked.connect(self.delete_text)

        self.label_output = QLabel("Converted text:")
        self.text_output = QTextEdit()

        # self.text_output.setFont(self.arabic_font)
        self.text_output.setReadOnly(True)
        self.text_output.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.text_output.setStyleSheet("font-size: 12px;")

        self.label_reversed = QLabel("Reversed text:")
        self.text_reversed = QTextEdit()

        # self.text_reversed.setFont(self.arabic_font)
        self.text_reversed.setReadOnly(True)
        self.text_reversed.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.text_reversed.setStyleSheet("font-size: 12px;")

        self.btn_reverse = QPushButton("Reverse")
        self.btn_reverse.clicked.connect(self.reverse_text)

        self.btn_copy_reversed = QPushButton("Copy Reversed")
        self.btn_copy_reversed.clicked.connect(lambda: self.copy_output(self.text_reversed))

        layout = QVBoxLayout()
        layout.addWidget(self.label_input)
        layout.addWidget(self.text_input)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.btn_paste)
        button_layout.addWidget(self.btn_copy_output)
        button_layout.addWidget(self.btn_delete)
        layout.addLayout(button_layout)

        layout.addWidget(self.checkbox)
        layout.addWidget(self.label_output)
        layout.addWidget(self.text_output)
        layout.addWidget(self.label_reversed)
        layout.addWidget(self.btn_reverse)
        layout.addWidget(self.btn_copy_reversed)
        layout.addWidget(self.text_reversed)

        self.setLayout(layout)

    def take_input(self):
        input_text = self.text_input.toPlainText()
        reshaped_text = reshaper.reshape(input_text)
        if self.checkbox.isChecked():
            reshaped_text = "\n".join(["{a:r:}" + line + "{a:r:}" for line in reshaped_text.split('\n')])
        self.text_output.setPlainText(reshaped_text)

    def copy_output(self, text_widget):
        clipboard = QApplication.clipboard()
        clipboard.setText(text_widget.toPlainText())

    def paste_text(self):
        self.text_input.setPlainText(QApplication.clipboard().text())

    def delete_text(self):
        self.text_input.clear()
        self.text_output.clear()
        self.text_reversed.clear()

    def reverse_text(self):
        reshaped_text = self.text_output.toPlainText()
        reversed_text = ""
        i = 0
        while i < len(reshaped_text):
            if reshaped_text[i] == "ﻼ":
                reversed_text += "لا"
                i += 1
            else:
                reversed_text += reverse_reshaper_dict.get(reshaped_text[i], reshaped_text[i])
                i += 1

        self.text_reversed.setPlainText(reversed_text)


app = QApplication(sys.argv)
qdarktheme.setup_theme("auto")

window = ArabicReshaperApp()
window.show()
sys.exit(app.exec())
