import PySide6.QtCore
from PySide6.QtCore import QLine
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow, QWidget, QMenuBar, QMenu, QApplication, QLabel, QVBoxLayout, QLineEdit, \
    QGridLayout, QSpinBox, QPushButton, QHBoxLayout, QDateEdit, QDoubleSpinBox, QComboBox, QPlainTextEdit, QTableWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nuevo entrenamiento")
        ##self.setGeometry(100, 100, 600, 700)
        self.crear_inicio()
        self.ui_elegir_usuario()
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

        nuevo_deportista.triggered.connect(self.ui_registrar_usuario)
        cambiar_deportista.triggered.connect(self.ui_elegir_usuario)
        mostrar_resultados.triggered.connect(self.ui_ficha_ususario)

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
    # USUARIOS
    ##Registrar ususario
    def ui_registrar_usuario(self):
        #WIDGET CENTRAL
        registro=QWidget()
        registro_layout=QVBoxLayout(registro)
        titulo=QLabel("REGISTRAR USUARIO")
        registro_layout.addWidget(titulo)

        ##Grid

        grid_registro=QGridLayout()

        ###Definir tamaño de las columnas
        grid_registro.setColumnStretch(0, 1)
        grid_registro.setColumnStretch(1, 1)
        grid_registro.setColumnStretch(2, 1)

        ###Labels
        n_nombre_label = QLabel("Nombre")
        grid_registro.addWidget(n_nombre_label, 0, 0)
        n_apellidos_label = QLabel("Apellidos")
        grid_registro.addWidget(n_apellidos_label, 0, 1)
        n_telefono_label = QLabel("Teléfono")
        grid_registro.addWidget(n_telefono_label, 2, 0)
        n_direccion_label = QLabel("Direccion")
        grid_registro.addWidget(n_direccion_label, 4, 0)
        n_email_label = QLabel("E-mail")
        grid_registro.addWidget(n_email_label, 2, 1)
        n_edad_label = QLabel("Edad")
        grid_registro.addWidget(n_edad_label, 6, 0)
        n_alto_label = QLabel("Estatura")
        grid_registro.addWidget(n_alto_label, 6, 1)
        n_genero_label = QLabel("Género")
        grid_registro.addWidget(n_genero_label, 6, 2)
        n_notas_label = QLabel("Observaciones")
        grid_registro.addWidget(n_notas_label, 8, 0)
        ###Inputs
        ipt_name=QLineEdit()
        grid_registro.addWidget(ipt_name, 1, 0)
        ipt_apellido=QLineEdit()
        grid_registro.addWidget(ipt_apellido, 1, 1,1,2)
        ipt_tlfn=QLineEdit()
        ipt_tlfn.setMaxLength(9)
        grid_registro.addWidget(ipt_tlfn, 3, 0)
        ipt_direccion=QLineEdit()
        grid_registro.addWidget(ipt_direccion, 5, 0, 1, 3)
        ipt_mail=QLineEdit()
        grid_registro.addWidget(ipt_mail, 3, 1, 1, 2)
        ipt_edad=QSpinBox()
        grid_registro.addWidget(ipt_edad, 7, 0)
        ipt_alto = QDoubleSpinBox()
        grid_registro.addWidget(ipt_alto, 7, 1)
        ipt_alto.setDecimals(2)
        ipt_genero=QComboBox()
        ipt_genero.addItems(['Masculino', 'Femenino', 'Otros'])
        grid_registro.addWidget(ipt_genero, 7, 2)
        ipt_notas=QPlainTextEdit()
        grid_registro.addWidget(ipt_notas, 9, 0, 2, 3)

        registro_layout.addLayout(grid_registro)

        guardar=QPushButton("Guardar")

        registro_layout.addWidget(guardar)

        #Definir widget central
        self.setCentralWidget(registro)
    ##Elegir ususario
    def ui_elegir_usuario(self):
        #WIDGET CENTRAL
        elegir=QWidget()
        elegir_layout=QVBoxLayout(elegir)
        titulo=QLabel("REGISTRAR USUARIO")
        elegir_layout.addWidget(titulo)
        #OPCIONES DE TABLA

        ##Buscar
        buscar=QHBoxLayout()
        buscar_input=QLineEdit()
        buscar_input.setPlaceholderText("Introduce el nombre del usuario")
        buscar_boton=QPushButton("Buscar")

        buscar.addWidget(buscar_input)
        buscar.addWidget(buscar_boton)

        ##PAsar páginas
        paginas=QHBoxLayout()
        pagina_anterior=QPushButton("Anterior")
        pagina_siguiente=QPushButton("Siguiente")

        paginas.addWidget(pagina_anterior)
        paginas.addWidget(pagina_siguiente)

        ##Contenedor de als opciones
        opciones=QVBoxLayout()
        opciones.addLayout(buscar)
        opciones.addLayout(paginas)

        elegir_layout.addLayout(opciones)

        #TABLA
        ##Configurar tabla
        tabla=QTableWidget()
        tabla.setColumnCount(2)
        tabla.setHorizontalHeaderLabels(["Ususario", "ID"])
        ##Próximamente aquí irá el bucle que mostrará los datos.
        ##Agregar tabla al layout
        elegir_layout.addWidget(tabla)
        #BOTONES
        btnElegirElegir=QPushButton("Elegir")
        btnElegirEliminar=QPushButton("Eliminar")

        optElegirUsuario=QHBoxLayout()
        optElegirUsuario.addWidget(btnElegirElegir)
        optElegirUsuario.addWidget(btnElegirEliminar)

        elegir_layout.addLayout(optElegirUsuario)

        #IMPRIMIR VISTA
        self.setCentralWidget(elegir)
    ##Mostrar ficha
    def ui_ficha_ususario(self):
        #WIDGET CENTRAL
        ficha=QWidget()
        ficha_layout=QVBoxLayout(ficha)
        tituloFicha=QLabel("NOMBRE DEL USUARIO")
        ficha_layout.addWidget(tituloFicha)

        #TABLA DE DATOS
        subtitulo1Ficha=QLabel("Datos personales")
        ficha_layout.addWidget(subtitulo1Ficha)

        tablaDatosPers=QVBoxLayout()
        ##Funcion para extraer datos para rellenar los label

        ##Datos
        grid_ficha = QGridLayout()

        ###Definir tamaño de las columnas
        grid_ficha.setColumnStretch(0, 1)
        grid_ficha.setColumnStretch(1, 1)
        grid_ficha.setColumnStretch(2, 1)

        ###Labels
        n_nombre_label = QLabel("Nombre")
        grid_ficha.addWidget(n_nombre_label, 0, 0)
        n_apellidos_label = QLabel("Apellidos")
        grid_ficha.addWidget(n_apellidos_label, 0, 1)
        n_telefono_label = QLabel("Teléfono")
        grid_ficha.addWidget(n_telefono_label, 2, 0)
        n_direccion_label = QLabel("Direccion")
        grid_ficha.addWidget(n_direccion_label, 4, 0)
        n_email_label = QLabel("E-mail")
        grid_ficha.addWidget(n_email_label, 2, 1)
        n_edad_label = QLabel("Edad")
        grid_ficha.addWidget(n_edad_label, 6, 0)
        n_alto_label = QLabel("Estatura")
        grid_ficha.addWidget(n_alto_label, 6, 1)
        n_genero_label = QLabel("Género")
        grid_ficha.addWidget(n_genero_label, 6, 2)
        n_notas_label = QLabel("Observaciones")
        grid_ficha.addWidget(n_notas_label, 8, 0)
        ###Inputs
        ipt_name = QLineEdit()
        grid_ficha.addWidget(ipt_name, 1, 0)
        ipt_apellido = QLineEdit()
        grid_ficha.addWidget(ipt_apellido, 1, 1, 1, 2)
        ipt_tlfn = QLineEdit()
        ipt_tlfn.setMaxLength(9)
        grid_ficha.addWidget(ipt_tlfn, 3, 0)
        ipt_direccion = QLineEdit()
        grid_ficha.addWidget(ipt_direccion, 5, 0, 1, 3)
        ipt_mail = QLineEdit()
        grid_ficha.addWidget(ipt_mail, 3, 1, 1, 2)
        ipt_edad = QSpinBox()
        grid_ficha.addWidget(ipt_edad, 7, 0)
        ipt_alto = QDoubleSpinBox()
        grid_ficha.addWidget(ipt_alto, 7, 1)
        ipt_alto.setDecimals(2)
        ipt_genero = QComboBox()
        ipt_genero.addItems(['Masculino', 'Femenino', 'Otros'])
        grid_ficha.addWidget(ipt_genero, 7, 2)
        ipt_notas = QPlainTextEdit()
        grid_ficha.addWidget(ipt_notas, 9, 0, 2, 3)

        ficha_layout.addLayout(grid_ficha)

        guardarCambiosUsuario = QPushButton("Guardar cambios")

        ficha_layout.addWidget(guardarCambiosUsuario)
        ##Imprimir
        ficha_layout.addLayout(tablaDatosPers)
        #PRs
        ##Configuración
        subtitulo2Ficha = QLabel("Pesos Record")
        ficha_layout.addWidget(subtitulo2Ficha)

        tablaPrPers = QTableWidget()
        tablaPrPers.setColumnCount(3)
        tablaPrPers.setHorizontalHeaderLabels(["Ejercicio", "Repeticiones", "Peso"])
        ##Aquí ira la función que rellene la tabla
        ##mostrar en layout
        ficha_layout.addWidget(tablaPrPers)

        #MOSTRAR LAYOUT
        self.setCentralWidget(ficha)
if __name__=="__main__":
    app=QApplication()
    ventana=MainWindow()
    ventana.show()
    app.exec()