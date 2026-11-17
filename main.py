import PySide6.QtCore
from PySide6.QtCore import QLine
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow, QWidget, QMenuBar, QMenu, QApplication, QLabel, QVBoxLayout, QLineEdit, \
    QGridLayout, QSpinBox, QPushButton, QHBoxLayout, QDateEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nuevo entrenamiento")
        ##self.setGeometry(100, 100, 600, 700)
        self.crear_inicio()
        self.ui_nueva_sesion()
        #MENÚ
    def crear_inicio(self):
        menu_bar=QMenuBar()
        self.setMenuBar(menu_bar)

        #Opciones del Menú

        ## Sesiones
        entrenamiento_menu=QMenu("Sesión")
        nueva_sesion=QAction("Nueva sesión", self)
        buscar_sesion=QAction("Buscar sesión", self)

        nueva_sesion.triggered.connect(self.ui_nueva_sesion)
        buscar_sesion.triggered.connect(self.ui_ultima_sesion)

        entrenamiento_menu.addAction(nueva_sesion)
        entrenamiento_menu.addAction(buscar_sesion)


        menu_bar.addMenu(entrenamiento_menu)

        ##Deportistas
        deportista_menu=QMenu("Deportista")
        mostrar_resultados=QAction("Mostrar ficha", self)
        cambiar_deportista=QAction("Elegir", self)
        nuevo_deportista=QAction("Registrar", self)

        deportista_menu.addAction(mostrar_resultados)
        deportista_menu.addAction(cambiar_deportista)
        deportista_menu.addAction(nuevo_deportista)

        menu_bar.addMenu(deportista_menu)

    # WIDGET SESIONES

    def ui_nueva_sesion(self):
        #Nueva sesión
        nueva_sesion = QWidget()
        sesion_layout=QGridLayout(nueva_sesion)
        texto_sesion=QLabel("Aquí irá la página de nueva sesión")
        sesion_layout.addWidget(texto_sesion, 0, 0, 1, 5)
        ##Elegir ejercicio
        txt_ejercicio=QLabel("Ejercicio:")
        insert_ejercicio=QLineEdit()
        insert_ejercicio.setPlaceholderText("Nombre del ejercicio")
        sesion_layout.addWidget(txt_ejercicio, 1, 0)
        sesion_layout.addWidget(insert_ejercicio, 1, 1, 1, 4)

        ##Series

        txt_serie1 = QLabel("Serie 1")
        sesion_layout.addWidget(txt_serie1, 2, 1)
        txt_serie2 = QLabel("Serie 2")
        sesion_layout.addWidget(txt_serie2, 2, 2)
        txt_serie3 = QLabel("Serie 3")
        sesion_layout.addWidget(txt_serie3, 2, 3)
        txt_serie4 = QLabel("Serie 4")
        sesion_layout.addWidget(txt_serie4, 2, 4)

        ##Repeticiones
        texto_sesion = QLabel("Repeticiones")
        sesion_layout.addWidget(texto_sesion, 3, 0)
        serie_1 = QSpinBox()
        sesion_layout.addWidget(serie_1, 3, 1)
        serie_2 = QSpinBox()
        sesion_layout.addWidget(serie_2, 3, 2)
        serie_3 = QSpinBox()
        sesion_layout.addWidget(serie_3, 3, 3)
        serie_4 = QSpinBox()
        sesion_layout.addWidget(serie_4, 3, 4)

        ##Peso
        txt_peso = QLabel("Peso en Kg")
        sesion_layout.addWidget(txt_peso, 4, 0)
        peso_1 = QSpinBox()
        sesion_layout.addWidget(peso_1, 4, 1)
        peso_2 = QSpinBox()
        sesion_layout.addWidget(peso_2, 4, 2)
        peso_3 = QSpinBox()
        sesion_layout.addWidget(peso_3, 4, 3)
        peso_4 = QSpinBox()
        sesion_layout.addWidget(peso_4, 4, 4)

        ##Guardar

        btn_guardar=QPushButton("Guardar Ejercicio")
        sesion_layout.addWidget(btn_guardar, 5,4)

        #Imprimir formulario
        self.setCentralWidget(nueva_sesion)

    # WIDGET MOSTRAR SESIÓN
    def ui_ultima_sesion(self):

        ##Elegir el día que quieres ver
        ultima_sesion=QWidget()
        elegir_layout=QHBoxLayout(ultima_sesion)
        elegir_dia_titulo=QLabel("Elige un día")
        elegir_layout.addWidget(elegir_dia_titulo)
        elegir_dia_imput=QDateEdit()
        elegir_layout.addWidget(elegir_dia_imput)
        btn_elegir_ok=QPushButton("Buscar")
        elegir_layout.addWidget(btn_elegir_ok)

        ##Imprimir

        self.setCentralWidget(ultima_sesion)



if __name__=="__main__":
    app=QApplication()
    ventana=MainWindow()
    ventana.show()
    app.exec()