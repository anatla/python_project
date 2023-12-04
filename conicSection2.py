import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QComboBox, QLineEdit, QPushButton
from PyQt5.QtCore import Qt
import matplotlib.pyplot as plt
import numpy as np

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Отображение кривых второго порядка")
        self.setGeometry(100, 100, 400, 200)

        # Создание виджетов
        self.curve_type_label = QLabel("Выберите тип кривой:")
        self.curve_type_combo = QComboBox()
        self.curve_type_combo.addItem("Эллипс")
        self.curve_type_combo.addItem("Гипербола")
        self.curve_type_combo.addItem("Парабола")
        self.curve_type_combo.setCurrentIndex(0)
        self.curve_type_combo.currentIndexChanged.connect(self.update_parameters)

        self.parameter1_label = QLabel("Введите параметр 1:")
        self.parameter1_input = QLineEdit()

        self.parameter2_label = QLabel("Введите параметр 2:")
        self.parameter2_input = QLineEdit()

        self.plot_button = QPushButton("Построить график")
        self.plot_button.clicked.connect(self.plot_curve)

        # Создание layout и настройка виджетов
        layout = QVBoxLayout()
        layout.addWidget(self.curve_type_label)
        layout.addWidget(self.curve_type_combo)
        layout.addWidget(self.parameter1_label)
        layout.addWidget(self.parameter1_input)
        layout.addWidget(self.parameter2_label)
        layout.addWidget(self.parameter2_input)
        layout.addWidget(self.plot_button)

        # Создание основного виджета и установка layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Изначально скрываем поле ввода параметра 2
        self.parameter2_label.hide()
        self.parameter2_input.hide()

        # Установка значения по умолчанию и вызов обновления параметров
        self.curve_type_combo.setCurrentIndex(0)
        self.update_parameters()

    def update_parameters(self):
        # Получение выбранного типа кривой
        curve_type = self.curve_type_combo.currentText()

        # Показываем/скрываем поле ввода параметра 2 в зависимости от выбранного типа кривой
        if curve_type in ["Эллипс", "Гипербола"]:
            self.parameter2_label.setText("Введите параметр 2:")
            self.parameter2_label.show()
            self.parameter2_input.show()
        else:
            self.parameter2_label.hide()
            self.parameter2_input.hide()

    def plot_curve(self):
        # Получение выбранного типа кривой и введенных параметров
        curve_type = self.curve_type_combo.currentText()
        parameter1 = float(self.parameter1_input.text())

        if curve_type in ["Эллипс", "Гипербола"]:
            parameter2 = float(self.parameter2_input.text())
        #     x = np.linspace(-10, 10, 200)
        # else:
        #     x = np.linspace(0, 10, 100)
        
        if curve_type == "Эллипс":
            theta = np.linspace(0, 2*np.pi, 100)  # Углы от 0 до 2π
            x = parameter1 * np.cos(theta)  # Координаты x точек эллипса
            y = parameter2 * np.sin(theta)  # Координаты y точек эллипса
            # y = np.sqrt(parameter2 - (parameter2/parameter1)**2 * x**2)
            
        elif curve_type == "Гипербола":
            y = np.linspace(-5, 5, 1000)  # Координаты x точек гиперболы
            x1 = parameter1 * np.sqrt(1 + (y/parameter2)**2)  # Координаты y для верхней ветви гиперболы
            x2 = -parameter1 * np.sqrt(1 + (y/parameter2)**2)  # Координаты y для нижней ветви гиперболы

            plt.figure()
            plt.plot(x1, y)
            plt.plot(x2, y)
            plt.xlabel("x")
            plt.ylabel("y")
            plt.title("Гипербола")
            plt.grid(True)
            plt.legend()
            plt.show()
            
        else:
            x = np.linspace(-10, 10, 100)  # Координаты x точек параболы
            y = parameter1 * x**2  # Координаты y точек параболы
            
        if curve_type in ["Эллипс", "Парабола"]:
            # Построение графика
            plt.plot(x, y)
            plt.xlabel("x")
            plt.ylabel("y")
            plt.title(curve_type)
            plt.grid(True)
            plt.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())