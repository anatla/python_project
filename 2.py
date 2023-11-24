import sys
import math  # библиотека math
import numpy # импортируем библиотеку

from PyQt5 import QtCore, QtGui, QtWidgets

from pyqtgraph import PlotWidget, plot                                 # +++ 


#from kyrsovaya import Ui_MainWindow  # Импортируем.
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(859, 844)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 70, 19, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 110, 19, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 70, 741, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 110, 741, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 160, 161, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(540, 160, 141, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(690, 160, 141, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 340, 331, 51))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(90, 200, 161, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(90, 240, 161, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(260, 160, 161, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(260, 200, 161, 31))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(260, 240, 161, 31))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(170, 280, 171, 31))
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 400, 331, 51))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(90, 460, 331, 51))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(90, 530, 331, 51))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")

# +++ vvv 
# ???        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView = PlotWidget(self.centralwidget)
# +++ ^^^        
        
        self.graphicsView.setGeometry(QtCore.QRect(30, 320, 791, 471))
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(640, 240, 141, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 859, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "a:"))
        self.label_2.setText(_translate("MainWindow", "b:"))
        self.pushButton.setText(_translate("MainWindow", "Линейная регрессия"))
        self.pushButton_2.setText(_translate("MainWindow", "Очистить"))
        self.pushButton_3.setText(_translate("MainWindow", "Выход"))
        self.pushButton_4.setText(_translate("MainWindow", "Степенная регрессия"))
        self.pushButton_5.setText(_translate("MainWindow", "Квадратичная регрессия"))
        self.pushButton_7.setText(_translate("MainWindow", "Гиперболическая регрессия"))
        self.pushButton_8.setText(_translate("MainWindow", "Показательная регрессия"))
        self.pushButton_9.setText(_translate("MainWindow", "Логарифмическая регрессия"))
        self.pushButton_10.setText(_translate("MainWindow", "Экспоненциальная регрессия"))
        self.pushButton_6.setText(_translate("MainWindow", "График "))


# Создание формы и Ui.
class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.myFun)
        self.ui.pushButton_4.clicked.connect(self.myFun2)
        self.ui.pushButton_7.clicked.connect(self.myFun3)
        self.ui.pushButton_8.clicked.connect(self.myFun4)
        self.ui.pushButton_9.clicked.connect(self.myFun5)
        self.ui.pushButton_10.clicked.connect(self.myFun6)
        self.ui.pushButton_5.clicked.connect(self.myFun7)
        self.ui.pushButton_2.clicked.connect(self.myFun8)
        self.ui.pushButton_3.clicked.connect(sys.exit)
        self.ui.pushButton_6.clicked.connect(self.btn_clk)
        
# +++ vvv
    def btn_clk(self):
#        L = [1,2,3,4,5]
        x = list(map(float, self.ui.lineEdit.text().split()))      
        y = list(map(float, self.ui.lineEdit_2.text().split()))
        
# AttributeError: 'MyWin' object has no attribute 'graphicsView'
#        self.graphicsView.plot(L)
# AttributeError: 'QGraphicsView' object has no attribute 'plot'
#        self.ui.graphicsView.plot(L)

        self.ui.graphicsView.plot(
            x, y, 
            pen='r', symbol='o', symbolPen='r', symbolBrush=0.2, name='_red')
# +++ ^^^   
        

    def myFun(self): # Создаем функцию линейной регрессии.
        self.text1 = str(self.ui.lineEdit.text())
        self.text2 = str(self.ui.lineEdit_2.text())
        razdel_y = self.text2.split() # разделяем
        razdel_x = self.text1.split() # разделяем
        n = len(razdel_x) # количество элементов в списках
        m = [float(f) for f in razdel_y]
        o = [float(h) for h in razdel_x]
        x_na_y = [float(x*y) for x,y in zip(o,m)]
        x_v_kvadrate = [float(i*i) for i in o]
        y_v_kvadrate = [float(q*q) for q in m]
# ??? деление на 0
        a =round(((sum(o)*sum(m)-n*sum(x_na_y))/((sum(o)**2)-n*sum(x_v_kvadrate))),4)
        b =round((sum(o)*sum(x_na_y)-sum(x_v_kvadrate)*sum(m))/((sum(o)**2)-n*sum(x_v_kvadrate)),4)
        Y = [a*o[i]+b for i in range(0,n)] # список значений линейной функции
        so = [abs((m[i]-Y[i])/(n*m[i])) for i in range(0,n)]
        srednya_oshibka_approksimacii = sum(so)*100
        r = (n * sum(x_na_y) - sum(o) * sum(m)) / (((n * sum(x_v_kvadrate) - (sum(o) ** 2)) * (n * sum(y_v_kvadrate) - (sum(m) ** 2))) ** 0.5) # Коэффициент парной корреляции
        R_v_kvadrate = r**2 # Коэффициент детерминации

        self.ui.label_3.setText('Коэффициент линейной парной корреляции %f' % r) # Выводим данные
        self.ui.label_4.setText('Коэффициент детерминации %f' % R_v_kvadrate)  # Выводим данные
        self.ui.label_5.setText('Средняя ошибка аппроксимации %f' % srednya_oshibka_approksimacii)  # Выводим данные
        self.ui.label_6.setText(f'Уравнение линейной регрессии {a}x+({b}) ')  # Выводим данные

    def myFun2(self): # Создаем функцию степенной регрессии.
        self.text1 = str(self.ui.lineEdit.text())
        self.text2 = str(self.ui.lineEdit_2.text())
        razdel_y = self.text2.split()
        razdel_x = self.text1.split()
        n = len(razdel_x)  # количество элементов в списках
        m = [float(f) for f in razdel_y]
        o = [float(h) for h in razdel_x]
        lnx = [math.log(i) for i in o]
        lny = [math.log(i) for i in m]
        lnx_na_lny = [(math.log(x)*math.log(y)) for x,y in zip(o,m)]
        lnx_v_kvadrate = [math.log(i)*math.log(i) for i in o]
        b = round((n*sum(lnx_na_lny)-sum(lnx)*sum(lny))/(n*sum(lnx_v_kvadrate)-sum(lnx)**2),4)
        a = round(math.e ** (1/n*sum(lny)-b/n*sum(lnx)),4)
        Y = [a * o[i]**b for i in range(0, n)]  # список значений степенной функции
        so = [abs((m[i] - Y[i]) / (n * m[i])) for i in range(0, n)]
        srednya_oshibka_approksimacii = sum(so) * 100  # средняя ошибка аппроксимации
        r_spec = [abs((m[i]-Y[i])) for i in range(0,n)]
        r_spec_v_kvadrate = [float(i*i) for i in r_spec]
        y_sredniy = 1/n*sum(m)
        r_spec2 = [abs((m[i]-y_sredniy)) for i in range(0,n)]
        r_spec2_v_kvadrate = [float(i*i) for i in r_spec2]
        r = (1-(sum(r_spec_v_kvadrate))/(sum(r_spec2_v_kvadrate )))**0.5 # Коэффициент парной корреляции
        R_v_kvadrate = r ** 2 # Коэффициент детерминации

        self.ui.label_3.setText('Коэффициент линейной парной корреляции %f' % r) # Выводим данные
        self.ui.label_4.setText('Коэффициент детерминации %f' % R_v_kvadrate )  # Выводим данные
        self.ui.label_5.setText('Средняя ошибка аппроксимации %f' % srednya_oshibka_approksimacii)  # Выводим данные
        self.ui.label_6.setText(f'Уравнение степенной регрессии {a}x^({b}) ')  # Выводим данные

    def myFun3(self): # Создаем функцию гиперболической регрессии.
        self.text1 = str(self.ui.lineEdit.text())
        self.text2 = str(self.ui.lineEdit_2.text())
        razdel_y = self.text2.split()
        razdel_x = self.text1.split()
        n = len(razdel_x) # количество элементов в списках
        m = [float(f) for f in razdel_y]
        o = [float(h) for h in razdel_x]
        s = sum(m) # сумма значений y
        s1 = sum([1 / o[i] for i in range(0, n)])  # сумма 1/x
        s2 = sum([(1 / o[i]) ** 2 for i in range(0, n)])  # сумма (1/x)**2
        s3 = sum([m[i] / o[i] for i in range(0, n)])  # сумма y/x
        a = round((s * s2 - s1 * s3) / (n * s2 - s1 ** 2), 3)  # коэфициент а с тремя дробными цифрами
        b = round((n * s3 - s1 * s) / (n * s2 - s1 ** 2), 3)  # коэфициент b с тремя дробными цифрами
        Y = [a + b / o[i] for i in range(0, n)]  # список значений гиперболической функции
        so = [abs((m[i]-Y[i])/(n*m[i])) for i in range(0,n)]
        srednya_oshibka_approksimacii = sum(so) * 100 # средняя ошибка аппроксимации
        r_spec = [abs((m[i]-Y[i])) for i in range(0,n)]
        r_spec_v_kvadrate = [float(i*i) for i in r_spec]
        y_sredniy = 1/n*sum(m)
        r_spec2 = [abs((m[i]-y_sredniy)) for i in range(0,n)]
        r_spec2_v_kvadrate = [float(i*i) for i in r_spec2]
        r = (1-(sum(r_spec_v_kvadrate))/(sum(r_spec2_v_kvadrate )))**0.5 # Коэффициент парной корреляции
        R_v_kvadrate = r ** 2 # Коэффициент детерминации

        self.ui.label_3.setText('Коэффициент линейной парной корреляции %f' % r) # Выводим данные
        self.ui.label_4.setText('Коэффициент детерминации %f' % R_v_kvadrate )  # Выводим данные
        self.ui.label_5.setText('Средняя ошибка аппроксимации %f' % srednya_oshibka_approksimacii)  # Выводим данные
        self.ui.label_6.setText(f'Уравнение гиперболической регрессии {a}x+({b}/x) ')  # Выводим данные

    def myFun4(self): # Создаем функцию показательной регрессии.
        self.text1 = str(self.ui.lineEdit.text())
        self.text2 = str(self.ui.lineEdit_2.text())
        razdel_y = self.text2.split()
        razdel_x = self.text1.split()
        n = len(razdel_x)  # количество элементов в списках
        m = [float(f) for f in razdel_y]
        o = [float(h) for h in razdel_x]
        lny = [math.log(i) for i in m]
        x_na_lny = [x * math.log(y)  for x,y in zip(o,m)]
        x_v_kvadrate = [float(i * i) for i in o]
        b = round(math.e ** ((n*sum(x_na_lny)-sum(o)*sum(lny))/(n*sum(x_v_kvadrate)-sum(o)**2)),4)
        a = round(math.e ** (1/n*sum(lny)-math.log(b)/n*sum(o)),4)
        Y = [a*b**o[i] for i in range(0, n)]  # список значений показательной функции
        so = [abs((m[i]-Y[i])/(n*m[i])) for i in range(0,n)]
        srednya_oshibka_approksimacii = sum(so) * 100 # средняя ошибка аппроксимации
        r_spec = [abs((m[i]-Y[i])) for i in range(0,n)]
        r_spec_v_kvadrate = [float(i*i) for i in r_spec]
        y_sredniy = 1/n*sum(m)
        r_spec2 = [abs((m[i]-y_sredniy)) for i in range(0,n)]
        r_spec2_v_kvadrate = [float(i*i) for i in r_spec2]
        r = (1-(sum(r_spec_v_kvadrate))/(sum(r_spec2_v_kvadrate )))**0.5 # Коэффициент парной корреляции
        R_v_kvadrate = r ** 2 # Коэффициент детерминации

# !!!
        self.ui.label_3.setText(
            f'Коэффициент линейной парной корреляции: {r}') 
        self.ui.label_4.setText(
            f'Коэффициент детерминации: {R_v_kvadrate}')    
        self.ui.label_5.setText(
            f'Средняя ошибка аппроксимации: {srednya_oshibka_approksimacii}') 
        self.ui.label_6.setText(
            f'Уравнение показательной регрессии {a}*{b}^x ')  

    def myFun5(self): # Создаем функцию логарифмической регрессии.
        self.text1 = str(self.ui.lineEdit.text())
        self.text2 = str(self.ui.lineEdit_2.text())
        razdel_y = self.text2.split()
        razdel_x = self.text1.split()
        n = len(razdel_x)  # количество элементов в списках
        m = [float(f) for f in razdel_y]
        o = [float(h) for h in razdel_x]
        y_na_lnx = [math.log(x) * y  for x,y in zip(o,m)]
        lnx = [math.log(i) for i in o]
        lnx_v_kvadrate = [math.log(i)*math.log(i) for i in o]
        b = round((n*sum(y_na_lnx) - sum(m)*sum(lnx))/(n*sum(lnx_v_kvadrate)-sum(lnx)**2),4)
        a = round(1/n*sum(m)-b/n*sum(lnx),4)
        Y = [a+b*math.log(o[i]) for i in range(0, n)]  # список значений логарифмической функции
        so = [abs((m[i]-Y[i])/(n*m[i])) for i in range(0,n)]
        srednya_oshibka_approksimacii = sum(so) * 100 # средняя ошибка аппроксимации
        r_spec = [abs((m[i]-Y[i])) for i in range(0,n)]
        r_spec_v_kvadrate = [float(i*i) for i in r_spec]
        y_sredniy = 1/n*sum(m)
        r_spec2 = [abs((m[i]-y_sredniy)) for i in range(0,n)]
        r_spec2_v_kvadrate = [float(i*i) for i in r_spec2]
        r = (1-(sum(r_spec_v_kvadrate))/(sum(r_spec2_v_kvadrate )))**0.5 # Коэффициент парной корреляции
        R_v_kvadrate = r ** 2 # Коэффициент детерминации

        self.ui.label_3.setText('Коэффициент линейной парной корреляции %f' % r) # Выводим данные
        self.ui.label_4.setText('Коэффициент детерминации %f' % R_v_kvadrate )  # Выводим данные
        self.ui.label_5.setText('Средняя ошибка аппроксимации %f' % srednya_oshibka_approksimacii)  # Выводим данные
        self.ui.label_6.setText(f'Уравнение логарифмической регрессии {a}+{b}*ln(x)')  # Выводим данные

    def myFun6(self):  # Создаем функцию экспоненциальной регрессии.
        self.text1 = str(self.ui.lineEdit.text())
        self.text2 = str(self.ui.lineEdit_2.text())
        razdel_y = self.text2.split()
        razdel_x = self.text1.split()
        n = len(razdel_x)  # количество элементов в списках
        m = [float(f) for f in razdel_y]
        o = [float(h) for h in razdel_x]
        x_na_lny = [x*math.log(y) for x, y in zip(o, m)]
        lny = [math.log(i) for i in m]
        x_v_kvadrate = [float(i * i) for i in o]
        b = round((n * sum(x_na_lny ) - sum(o) * sum(lny)) / (n * sum(x_v_kvadrate) - sum(o) ** 2), 4)
        a = round(1 / n * sum(lny) - b / n * sum(o), 4)
        Y = [math.e ** (a+b*o[i]) for i in range(0, n)]  # список значений экспонениальной функции
        so = [abs((m[i] - Y[i]) / (n * m[i])) for i in range(0, n)]
        srednya_oshibka_approksimacii = sum(so) * 100  # средняя ошибка аппроксимации
        r_spec = [abs((m[i] - Y[i])) for i in range(0, n)]
        r_spec_v_kvadrate = [float(i * i) for i in r_spec]
        y_sredniy = 1 / n * sum(m)
        r_spec2 = [abs((m[i] - y_sredniy)) for i in range(0, n)]
        r_spec2_v_kvadrate = [float(i * i) for i in r_spec2]
        r = (1 - (sum(r_spec_v_kvadrate)) / (sum(r_spec2_v_kvadrate))) ** 0.5 # Коэффициент парной корреляции
        R_v_kvadrate = r ** 2 # Коэффициент детерминации

        self.ui.label_3.setText('Коэффициент линейной парной корреляции %f' % r)  # Выводим данные
        self.ui.label_4.setText('Коэффициент детерминации %f' % R_v_kvadrate)  # Выводим данные
        self.ui.label_5.setText('Средняя ошибка аппроксимации %f' % srednya_oshibka_approksimacii)  # Выводим данные
        self.ui.label_6.setText(f'Уравнение экспоненциальной регрессии e^({a}+{b}*x')  # Выводим данные

    def myFun7(self): # Создаем функцию квадратичной регрессии.
        self.text1 = str(self.ui.lineEdit.text())
        self.text2 = str(self.ui.lineEdit_2.text())
        razdel_y = self.text2.split()
        razdel_x = self.text1.split()
        n = len(razdel_x)  # количество элементов в списках
        m = [float(f) for f in razdel_y]
        o = [float(h) for h in razdel_x]
        x_v_kvadrate = [float(i * i) for i in o]
        x_v_kybe = [float(i * i * i) for i in o]
        x_v_chetvertoi = [float(i * i * i * i) for i in o]
        x_na_y = [float(x * y) for x, y in zip(o, m)]
        x_v_kvadrate_na_y = [float(x**2 * y) for x, y in zip(o, m)]
        A = numpy.array([[sum(x_v_kvadrate), sum(o), n], [sum(x_v_kybe ), sum(x_v_kvadrate ), sum(o)], [sum(x_v_chetvertoi), sum(x_v_kybe), sum(x_v_kvadrate)]])  # Матрица (левая часть системы)
        B = numpy.array([sum(m), sum(x_na_y),sum(x_v_kvadrate_na_y)])  # Вектор (правая часть системы)
#numpy.linalg.LinAlgError: Singular matrix
        X = numpy.linalg.inv(A).dot(B)
        a = round(X[0],4)
        b = round(X[1],4)
        c = round(X[2],4)
        Y = [a*(o[i])**2+b*o[i]+c for i in range(0, n)]  # список значений квадратичной функции
        so = [abs((m[i] - Y[i]) / (n * m[i])) for i in range(0, n)]
        srednya_oshibka_approksimacii = sum(so) * 100  # средняя ошибка аппроксимации
        r_spec = [abs((m[i] - Y[i])) for i in range(0, n)]
        r_spec_v_kvadrate = [float(i * i) for i in r_spec]
        y_sredniy = 1 / n * sum(m)
        r_spec2 = [abs((m[i] - y_sredniy)) for i in range(0, n)]
        r_spec2_v_kvadrate = [float(i * i) for i in r_spec2]
        r = (1 - (sum(r_spec_v_kvadrate)) / (sum(r_spec2_v_kvadrate))) ** 0.5 # Коэффициент парной корреляции
        R_v_kvadrate = r ** 2 # Коэффициент детерминации


        self.ui.label_3.setText('Коэффициент линейной парной корреляции %f' % r)  # Выводим данные
        self.ui.label_4.setText('Коэффициент детерминации %f' % R_v_kvadrate)  # Выводим данные
        self.ui.label_5.setText('Средняя ошибка аппроксимации %f' % srednya_oshibka_approksimacii)  # Выводим данные
        self.ui.label_6.setText(f'Уравнение квадратичной регрессии {a}*x^2-{b}*x+{c}')  # Выводим данные

    def myFun8(self):  # Создаем функцию чистки.
        self.ui.label_3.setText('')  # Очищаем данные
        self.ui.label_4.setText('')  # Очищаем данные
        self.ui.label_5.setText('')  # Очищаем данные
        self.ui.label_6.setText('')  # Очищаем данные
        self.ui.lineEdit.setText('') # Очищаем данные
        self.ui.lineEdit_2.setText('') # Очищаем данные

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())