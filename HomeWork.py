#Написать программу редактор текстовых файлов с графическим интерфейсом. Обязательно: Кнопка сохранить, кнопка выхода. Необязательно, но приветствуется: возможность открытия файла и отображения текста в окне, изменение цвета и размера текста, упаковка программы, изменение цвета кнопок принаведении мыши и др.
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QFileDialog, QWidget
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt
import qdarkstyle


class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.text_edit = QTextEdit(self)
        self.save_button = QPushButton('Сохранить', self)
        self.exit_button = QPushButton('Выход', self)
        self.open_button = QPushButton('Открыть', self)
        self.color_button = QPushButton('Изменить цвет текста', self)

        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(self.save_button)
        layout.addWidget(self.exit_button)
        layout.addWidget(self.open_button)
        layout.addWidget(self.color_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.save_button.clicked.connect(self.save_text)
        self.exit_button.clicked.connect(self.close)
        self.open_button.clicked.connect(self.open_file)
        self.color_button.clicked.connect(self.change_text_color)

        self.setGeometry(0, 0, 800, 600)
        self.setWindowTitle('Текстовый редактор')

    def save_text(self):
        # Сохранение текста в файл
        filename, _ = QFileDialog.getSaveFileName(self, 'Сохранить файл', '', 'Text Files (*.txt);;All Files (*)')

        if filename:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(self.text_edit.toPlainText())

    def open_file(self):
        # Открытие файла с текстом
        filename, _ = QFileDialog.getOpenFileName(self, 'Открыть файл', '', 'Text Files (*.txt);;All Files (*)')

        if filename:
            with open(filename, 'r', encoding='utf-8') as file:
                self.text_edit.setPlainText(file.read())

    def change_text_color(self):
        # Изменение цвета текста
        color = QColorDialog.getColor()
        if color.isValid():
            self.text_edit.setTextColor(color)

def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    editor = TextEditor()
    editor.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
