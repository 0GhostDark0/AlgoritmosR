import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt
import math

class Calculadora(QWidget):
    def init(self):
        super().init()

        self.initUI()

    def initUI(self):
        # Inicializar componentes de la GUI
        self.input1 = QLineEdit()
        self.input2 = QLineEdit()
        self.resultLabel = QLabel()

        # Crear botones para cada operación
        self.sumaButton = Qsuma("+")
        self.restaButton = Qresta("-")
        self.multiplicacionButton = Qmultiplicar("*")
        self.divisionButton = Qdivision("/")
        self.senoButton = Qseno("sen")
        self.cosenoButton = Qcoseno("cos")
        self.tangenteButton = Qtangente("tan")
        self.cotangenteButton = Qcotangente("cot")
        self.secanteButton = Qsecante("sec")
        self.cosecanteButton = Qcosecante("csc")

        # Conectar botones con sus respectivas operaciones
        self.sumaButton.clicked.connect(self.sumaOperacion)
        self.restaButton.clicked.connect(self.restaOperacion)
        self.multiplicacionButton.clicked.connect(self.multiplicacionOperacion)
        self.divisionButton.clicked.connect(self.divisionOperacion)
        self.senoButton.clicked.connect(self.senoOperacion)
        self.cosenoButton.clicked.connect(self.cosenoOperacion)
        self.tangenteButton.clicked.connect(self.tangenteOperacion)
        self.cotangenteButton.clicked.connect(self.cotangenteOperacion)
        self.secanteButton.clicked.connect(self.secanteOperacion)
        self.cosecanteButton.clicked.connect(self.cosecanteOperacion)

        # Configurar la disposición de los componentes
        layout = QVBoxLayout()
        layout.addWidget(self.input1)
        layout.addWidget(self.input2)
        layout.addWidget(self.sumaButton)
        layout.addWidget(self.restaButton)
        layout.addWidget(self.multiplicacionButton)
        layout.addWidget(self.divisionButton)
        layout.addWidget(self.senoButton)
        layout.addWidget(self.cosenoButton)
        layout.addWidget(self.tangenteButton)
        layout.addWidget(self.cotangenteButton)
        layout.addWidget(self.secanteButton)
        layout.addWidget(self.cosecanteButton)
        layout.addWidget(self.resultLabel)

        self.setLayout(layout)

    def sumaOperacion(self):
        # Obtener los valores de entrada
        num1 = float(self.input1.text())
        num2 = float(self.input2.text())

        # Realizar la suma
        resultado = num1 + num2

        # Mostrar el resultado
        self.resultLabel.setText(str(resultado))

    def restaOperacion(self):
        # Obtener los valores de entrada
        num1 = float(self.input1.text())
        num2 = float(self.input2.text())

        # Realizar la resta
        resultado = num1 - num2

        # Mostrar el resultado
        self.resultLabel.setText(str(resultado))

    def multiplicacionOperacion(self):
        # Obtener los valores de entrada
        num1 = float(self.input1.text())
        num2 = float(self.input2.text())

        # Realizar la multiplicación
        resultado = num1 * num2

        # Mostrar el resultado
        self.resultLabel.setText(str(resultado))

    def divisionOperacion(self):
        # Obtener los valores de entrada
        num1 = float(self.input1.text())
        num2 = float(self.input2.text())

        # Realizar la división
        if num2 != 0:
            resultado = num1 / num2
        else:
            resultado = "Error: División por cero"

        # Mostrar el resultado
        self.resultLabel.setText(str(resultado))

    def senoOperacion(self):
        # Obtener el valor de entrada
        num = float(self.input1.text())

        # Realizar la operación de seno
        resultado = math.sin(math.radians(num))

        # Mostrar el resultado
        self.resultLabel.setText(str(resultado))

    def cosenoOperacion(self):
        # Obtener el valor de entrada
        num = float(self.input1.text())

        # Realizar la operación de coseno
        resultado = math.cos(math.radians(num))

        # Mostrar el resultado
        self.resultLabel.setText(str(resultado))

    def tangenteOperacion(self):
        # Obtener el valor de entrada
        num = float(self.input1.text())

        # Realizar la operación de tangente
        resultado = math.tan(math.radians(num))

        # Mostrar el resultado
        self.resultLabel.setText(str(resultado))

    def cotangenteOperacion(self):
        # Obtener el valor de entrada
        num = float(self.input1.text())

        # Realizar la operación de cotangente
        resultado = 1 / math.tan(math.radians(num))

        # Mostrar el resultado
        self.resultLabel.setText(str(resultado))

    def secanteOperacion(self):
        # Obtener el valor de entrada
        num = float(self.input1.text())

        # Realizar la operación de secante
        resultado = 1 / math.cos(math.radians(num))

        # Mostrar el resultado
        self.resultLabel.setText(str(resultado))

    def cosecanteOperacion(self):
        # Obtener el valor de entrada
        num = float(self.input1.text())

        # Realizar la operación de cosecante
        resultado = 1 / math.sin(math.radians(num))

        # Mostrar el resultado
        self.resultLabel.setText(str(resultado))

def main():
    app = QApplication(sys.argv)
    calculadora = Calculadora()
    calculadora.show()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()
