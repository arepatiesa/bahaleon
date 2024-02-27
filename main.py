import pymysql  # importar el módulo pymysql
from tkinter import *
from tkinter import filedialog
from functools import partial
import tkinter
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox as MessageBox
import openpyxl 
from datetime import date
from datetime import datetime

# Conexion a base de datos 
 
conexion = pymysql.connect(host='localhost',
                           db='bahaleon.db',
                           user='root',
                           passwd='')

# Variables de Estilo
padding = 7.5
fuentePrincipal = "Arial, Segoe UI, Ubuntu"
colorPrimary = "#084298"
colorSuccess = "#0f5132"
colorDanger = "#842029"
bgColorPrimary = "#0d6efd"
bgColorSecondary = "#6c757d"
bgColorSuccess = "#198754"
bgColorDanger = "#dc3545"
bgColorTextBox = "#f1f1f1"
fontSize5 = 5
fontSize10 = 10
fontSize15 = 15
fontSize20 = 20

# Iniciacion de Variables Globales
pcepl = None
pcspl = None
rtsoLabel = None
rmlpLabel = None
pcept = None
pcspt = None
rtphLabel = None
rmtpLabel = None
pcepd = None
pcspd = None
rtcasLabel = None
rmcpLabel = None
pnoiepr = None
pchospr = None
rtcaschoLabel = None
rmpchoLabel = None
rmermatotalLabel = None
ml = None
mt = None
md = None
mch = None
mtr = None
# Botones
btnAddMermaTotal = None
btnCalcularMermaTotal = None
btnLimpiarMermaTotal = None
btnExportExcel = None


def salir():
    exit()


# Ventana Calculadora de Merma Total
def ventanaCalculoMerma():
    global pcepl, pcspl, rtsoLabel, rmlpLabel
    global pcept, pcspt, rtphLabel, rmtpLabel
    global pcepd, pcspd, rtcasLabel, rmcpLabel
    global pnoiepr, pchospr, rtcaschoLabel, rmpchoLabel
    global rmermatotalLabel
    global btnAddMermaTotal, btnCalcularMermaTotal, btnLimpiarMermaTotal
    tkVentanaCalculoMerma = Toplevel()
    tkVentanaCalculoMerma.geometry("1240x750")
    tkVentanaCalculoMerma.title("Bahaleon - Calculadora de Merma Total")
    tkVentanaCalculoMerma.configure(bg="white")
    tkVentanaCalculoMerma.attributes('-toolwindow', True)

    # Declara variables de control
    tkVentanaCalculoMerma.total = DoubleVar(value=0.0)

    # Etiqueta Titulo de la Ventana
    Label(tkVentanaCalculoMerma, text=" Bahaleon - Calculadora de Merma Total ",
          font=(fuentePrincipal, 20), bg="#239e2a", fg='#fff').place(x=padding*2, y=padding)
    # Separador
    ttk.Separator(tkVentanaCalculoMerma).place(x=0, y=padding*6, relwidth=1)

    # Etiqueta Titulo de Proceso de Limpieza
    Label(tkVentanaCalculoMerma, text="Limpieza - Peso Cacao (KG)",
          font=(fuentePrincipal, 15), bg="#baac61", fg='#fff').place(x=20, y=padding*8)
    # Separador
    ttk.Separator(tkVentanaCalculoMerma).place(x=0, y=padding*12, relwidth=1)

    # Etiqueta PCEPL
    Label(tkVentanaCalculoMerma, text="ENTRADA - PCEPL(P1)",
          font=(fuentePrincipal, 15), bg="#0d6efd", fg='#fff').place(x=20, y=padding*14)
    # Variable almacena valor PCEPL
    pcepl = tkinter.DoubleVar(tkVentanaCalculoMerma, value=0.0)
    # Caja de Texto PCEPL
    Entry(tkVentanaCalculoMerma, textvariable=pcepl, font=(
        fuentePrincipal, 15), bg="#f1f1f1", fg='#303030').place(x=300, y=padding*14)

    # Etiqueta PCSPL
    Label(tkVentanaCalculoMerma, text="SALIDA  -  PCSPL(P2L)",
          font=(fuentePrincipal, 15), bg="#198754", fg='#fff').place(x=20, y=padding*20)
    # Variable almacena valor PCSPL
    pcspl = tkinter.DoubleVar(tkVentanaCalculoMerma, value=0.0)
    # Caja de Texto PCSPL
    Entry(tkVentanaCalculoMerma, textvariable=pcspl, font=(
        fuentePrincipal, 15), bg="#f1f1f1", fg='#303030').place(x=300, y=padding*20)

    # Etiqueta Suciedad Obtenida
    Label(tkVentanaCalculoMerma, text="PESO TOTAL DE LA SUCIEDAD OBTENIDA (KG)", font=(
        fuentePrincipal, 15), bg=colorPrimary, fg='#fff').place(x=600, y=padding*14)

    # Etiqueta Merma de Limpieza
    Label(tkVentanaCalculoMerma, text="MERMA DE LIMPIEZA DE PRODUCTO ML (%)", font=(
        fuentePrincipal, 15), bg=colorDanger, fg='#fff').place(x=600, y=padding*20)

    # Etiqueta del Resultado Suciedad Obtenida
    rtsoLabel = tkinter.Label(tkVentanaCalculoMerma, text="0.00")
    rtsoLabel.config(font=(fuentePrincipal, 15),
                     bg=bgColorSecondary, fg='#fff')
    rtsoLabel.place(x=1075, y=padding*14)
    # Etiqueta del Resultado Merma de Limpieza
    rmlpLabel = tkinter.Label(tkVentanaCalculoMerma, text="0.00")
    rmlpLabel.config(font=(fuentePrincipal, 15),
                     bg=bgColorSecondary, fg='#fff')
    rmlpLabel.place(x=1075, y=padding*20)

    # Etiqueta Titulo de Proceso de Tostado
    Label(tkVentanaCalculoMerma, text="Tostado - Peso Cacao (KG)",
          font=(fuentePrincipal, 15), bg="#bbad87", fg='#fff').place(x=20, y=padding*26)
    # Separador
    ttk.Separator(tkVentanaCalculoMerma).place(x=0, y=padding*30, relwidth=1)

    # Etiqueta PCEPT
    Label(tkVentanaCalculoMerma, text="ENTRADA - PCEPT(P1)",
          font=(fuentePrincipal, 15), bg="#0d6efd", fg='#fff').place(x=20, y=padding*32)
    # Variable almacena valor PCEPT
    pcept = tkinter.DoubleVar(tkVentanaCalculoMerma, value=0.0)
    # Caja de Texto PCEPT
    Entry(tkVentanaCalculoMerma, textvariable=pcept, font=(
        fuentePrincipal, 15), bg="#f1f1f1", fg='#303030').place(x=300, y=padding*32)

    # Etiqueta PCSPT
    Label(tkVentanaCalculoMerma, text="SALIDA  -  PCSPT(P2T)",
          font=(fuentePrincipal, 15), bg="#198754", fg='#fff').place(x=20, y=padding*38)
    # Variable almacena valor PCSPT
    pcspt = tkinter.DoubleVar(tkVentanaCalculoMerma, value=0.0)
    # Caja de Texto PCSPT
    Entry(tkVentanaCalculoMerma, textvariable=pcspt, font=(
        fuentePrincipal, 15), bg="#f1f1f1", fg='#303030').place(x=300, y=padding*38)

    # Etiqueta Perdida de Humedad
    Label(tkVentanaCalculoMerma, text="PESO TOTAL DE PERDIDA DE HUMEDAD", font=(
        fuentePrincipal, 15), bg=colorPrimary, fg='#fff').place(x=600, y=padding*32)

    # Etiqueta Merma de Tostado
    Label(tkVentanaCalculoMerma, text="MERMA DE TOSTADO DE PRODUCTO MT (%)", font=(
        fuentePrincipal, 15), bg=colorDanger, fg='#fff').place(x=600, y=padding*38)

    # Etiqueta del Resultado Perdida de Humedad
    rtphLabel = tkinter.Label(tkVentanaCalculoMerma, text="0.00")
    rtphLabel.config(font=(fuentePrincipal, 15),
                     bg=bgColorSecondary, fg='#fff')
    rtphLabel.place(x=1075, y=padding*32)

    # Etiqueta del Resultado Merma de Tostado
    rmtpLabel = tkinter.Label(tkVentanaCalculoMerma, text="0.00")
    rmtpLabel.config(font=(fuentePrincipal, 15),
                     bg=bgColorSecondary, fg='#fff')
    rmtpLabel.place(x=1075, y=padding*38)

    # Etiqueta Titulo de Proceso de Descascarillado
    Label(tkVentanaCalculoMerma, text="Descascarillado - Peso Cacao (KG)",
          font=(fuentePrincipal, 15), bg="#856147", fg='#fff').place(x=20, y=padding*44)
    # Separador
    ttk.Separator(tkVentanaCalculoMerma).place(x=0, y=padding*48, relwidth=1)

    # Etiqueta PCEPD
    Label(tkVentanaCalculoMerma, text="ENTRADA - PCEPD(P1)",
          font=(fuentePrincipal, 15), bg="#0d6efd", fg='#fff').place(x=20, y=padding*50)
    # Variable almacena valor PCEPD
    pcepd = tkinter.DoubleVar(tkVentanaCalculoMerma, value=0.0)
    # Caja de Texto PCEPD
    Entry(tkVentanaCalculoMerma, textvariable=pcepd, font=(
        fuentePrincipal, 15), bg="#f1f1f1", fg='#303030').place(x=300, y=padding*50)

    # Etiqueta PCSPD
    pcspdLabel = Label(tkVentanaCalculoMerma, text="SALIDA  -  PCSPD(P2D)", font=(
        fuentePrincipal, 15), bg="#198754", fg='#fff').place(x=20, y=padding*56)
    # Variable almacena valor PCSPD
    pcspd = tkinter.DoubleVar(tkVentanaCalculoMerma, value=0.0)
    # Caja de Texto PCSPD
    Entry(tkVentanaCalculoMerma, textvariable=pcspd, font=(
        fuentePrincipal, 15), bg="#f1f1f1", fg='#303030').place(x=300, y=padding*56)

    # Etiqueta Total de la Cascarilla
    Label(tkVentanaCalculoMerma, text="PESO TOTAL DE LA CASCARILLA", font=(
        fuentePrincipal, 15), bg=colorPrimary, fg='#fff').place(x=600, y=padding*50)

    # Etiqueta Merma de la Cascarilla
    Label(tkVentanaCalculoMerma, text="MERMA DE LA CASCARILLA  MC (%)", font=(
        fuentePrincipal, 15), bg=colorDanger, fg='#fff').place(x=600, y=padding*56)

    # Etiqueta del Resultado Total de La Cascarilla
    rtcasLabel = tkinter.Label(tkVentanaCalculoMerma, text="0.00")
    rtcasLabel.config(font=(fuentePrincipal, 15),
                      bg=bgColorSecondary, fg='#fff')
    rtcasLabel.place(x=1075, y=padding*50)

    # Etiqueta del Resultado Merma de Descascarillado
    rmcpLabel = tkinter.Label(tkVentanaCalculoMerma, text="0.00")
    rmcpLabel.config(font=(fuentePrincipal, 15),
                     bg=bgColorSecondary, fg='#fff')
    rmcpLabel.place(x=1075, y=padding*56)

    # Etiqueta Titulo de Proceso de Refinado
    Label(tkVentanaCalculoMerma, text="Refinado - Peso NIBS a Chocolate (KG)",
          font=(fuentePrincipal, 15), bg="#4a3732", fg='#fff').place(x=20, y=padding*62)
    # Separador
    ttk.Separator(tkVentanaCalculoMerma).place(x=0, y=padding*66, relwidth=1)

    # Etiqueta PNOIEPR
    Label(tkVentanaCalculoMerma, text="ENTRADA - PNOIEPR(P1)",
          font=(fuentePrincipal, 15), bg="#0d6efd", fg='#fff').place(x=20, y=padding*68)
    # Variable almacena valor PNOIEPR
    pnoiepr = tkinter.DoubleVar(tkVentanaCalculoMerma, value=0.0)
    Entry(tkVentanaCalculoMerma, textvariable=pnoiepr, font=(
        fuentePrincipal, 15), bg="#f1f1f1", fg='#303030').place(x=300, y=padding*68)

    # Etiqueta PCHOSPR
    Label(tkVentanaCalculoMerma, text="SALIDA  -  PCHOSPR(P2C)",
          font=(fuentePrincipal, 15), bg="#198754", fg='#fff').place(x=20, y=padding*74)
    pchospr = tkinter.DoubleVar(tkVentanaCalculoMerma, value=0.0)
    Entry(tkVentanaCalculoMerma, textvariable=pchospr, font=(
        fuentePrincipal, 15), bg="#f1f1f1", fg='#303030').place(x=300, y=padding*74)

    # Etiqueta Total de la Cascarilla Chocolate
    Label(tkVentanaCalculoMerma, text="PESO TOTAL DE LA CASCARILLA", font=(
        fuentePrincipal, 15), bg=colorPrimary, fg='#fff').place(x=600, y=padding*68)

    # Etiqueta Merma de Producto Chocolate
    Label(tkVentanaCalculoMerma, text="MERMA DE PERDIDA DE PRODUCTO MCH(%)", font=(
        fuentePrincipal, 15), bg=colorDanger, fg='#fff').place(x=600, y=padding*74)

    # Etiqueta del Resultado Total de La Cascarilla
    rtcaschoLabel = tkinter.Label(tkVentanaCalculoMerma, text="0.00")
    rtcaschoLabel.config(font=(fuentePrincipal, 15),
                         bg=bgColorSecondary, fg='#fff')
    rtcaschoLabel.place(x=1075, y=padding*68)

    # Etiqueta del Resultado Merma de Descascarillado
    rmpchoLabel = tkinter.Label(tkVentanaCalculoMerma, text="0.00")
    rmpchoLabel.config(font=(fuentePrincipal, 15),
                       bg=bgColorSecondary, fg='#fff')
    rmpchoLabel.place(x=1075, y=padding*74)

    # Etiqueta Titulo de Proceso de Tostado
    titulomermatotalLabel = Label(tkVentanaCalculoMerma, text="MERMA TOTAL  (MTR) = ML+MT+MC+MCH", font=(
        fuentePrincipal, 15), bg=colorDanger, fg='#fff').place(x=600, y=padding*80)

    # Etiqueta del Resultado Merma total
    rmermatotalLabel = tkinter.Label(tkVentanaCalculoMerma, text="0.00")
    rmermatotalLabel.config(font=(fuentePrincipal, 15),
                            bg=bgColorSecondary, fg='#fff')
    rmermatotalLabel.place(x=1075, y=padding*80)
    # Separador
    ttk.Separator(tkVentanaCalculoMerma).place(x=0, y=padding*84, relwidth=1)

    # boton de Calcular Merma total
    btnCalcularMermaTotal = tkinter.Button(tkVentanaCalculoMerma)
    btnCalcularMermaTotal.configure(text="Calcular", font=(
        fuentePrincipal, 12), bg=bgColorPrimary, fg='#fff', command=calcularMermaTotal)
    btnCalcularMermaTotal.place(x=50, y=padding*86)
    # boton de Limpiar Formulario
    btnLimpiarMermaTotal = Button(tkVentanaCalculoMerma, text="Limpiar", font=(
        fuentePrincipal, 12), bg=bgColorSecondary, fg='#fff', command=limpiarCalculoMerma).place(x=200, y=padding*86)
    # boton de Guardar Registro de Produccion
    btnAddMermaTotal = tkinter.Button(tkVentanaCalculoMerma)
    btnAddMermaTotal.configure(text="Guardar", state=DISABLED, font=(
        fuentePrincipal, 12), bg=bgColorSuccess, fg='#fff', command=guardarCalculoMermaTotal)
    btnAddMermaTotal.place(x=350, y=padding*86)
    # boton de cerrar
    Button(tkVentanaCalculoMerma, text="Cerrar", font=(fuentePrincipal, 12), bg=bgColorDanger,
           fg='#fff', command=tkVentanaCalculoMerma.destroy).place(x=500, y=padding*86)
    # boton exportar a excel
    btnExportExcel = tkinter.Button(tkVentanaCalculoMerma)
    btnExportExcel.configure(text="Exportar a Excel", font=(fuentePrincipal, 12), bg=bgColorSuccess, fg="#fff", command=exportarExcel)
    btnExportExcel.place(x=1000, y=padding*86)
    

def exportarExcel():
    # Seleccionar tabla y obtener datos
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM produccion")
    data = cursor.fetchall()

    # Crear Libro de Excel
    wb = openpyxl.Workbook()
    ws = wb.active
    for row in data:
        ws.append(row)

    # Ventana emergente de guardar como
    root = Tk()
    root.withdraw()
    # Formato de fecha
    now = datetime.now()    
    format = now.strftime('%d-%m-%Y')
    file_path = filedialog.asksaveasfilename(title="Guardar como", filetypes=[('Archivos Excel', "*.xlsx"), ("Archivos CVS", "*.csv"), ("Cualquier Archivo", "*")], initialfile=f'Seguimiento_Merma_{format}.xlsx', initialdir="./Archivos_Excel")
    # Se asegura de que si se cancela la ventana no se genere el archivo
    if file_path is not None:
        wb.save(file_path)
        
    root.destroy()

def calcularMermaTotal():
    global pcepl, pcspl, rtsoLabel, rmlpLabel
    global pcept, pcspt, rtphLabel, rmtpLabel
    global pcepd, pcspd, rtcasLabel, rmcpLabel
    global pnoiepr, pchospr, rtcaschoLabel, rmpchoLabel
    global ml, mt, md, mch, mtr
    global rmermatotalLabel
    global btnAddMermaTotal, btnCalcularMermaTotal, btnLimpiarMermaTotal

    # Utilidad para detectar si un numero es float
    def is_float(string):
        try:
            float(string)
            return True
        except ValueError:
            return False

    if is_float(pcepl.get()) or is_float(pcspl.get()) or pcspl.get() == "0.00" or pcspl.get() == "0.00":

        if float(pcepl.get()) > float(pcspl.get()):

            pt1 = float(pcepl.get()) - float(pcspl.get())
            ml = round((pt1*100)/float(pcepl.get()), 2)
            rmlpLabel.config(text=ml)
            rtsoLabel.config(text=pt1)

            pt1 = float(pcept.get()) - float(pcspt.get())
            mt = round((pt1*100)/float(pcept.get()), 2)
            rmtpLabel.config(text=mt)
            rtphLabel.config(text=pt1)

            pt1 = float(pcepd.get()) - float(pcspd.get())
            md = round((pt1*100)/float(pcepd.get()), 2)
            rmcpLabel.config(text=md)
            rtcasLabel.config(text=pt1)

            pt1 = float(pnoiepr.get()) - float(pchospr.get())
            mch = round((pt1*100)/float(pnoiepr.get()), 2)
            rmpchoLabel.config(text=mch)
            rtcaschoLabel.config(text=pt1)
            mtr = ml + mt + md + mch

            rmermatotalLabel.config(text=round(mtr, 2))
        else:
            MessageBox.showwarning(
                title="Atención", message="La Entrada no puede ser menor que la Salida")

        if btnAddMermaTotal["state"] == DISABLED:
            btnAddMermaTotal["state"] = NORMAL
        else:
            btnAddMermaTotal["state"] = DISABLED
    else:
        MessageBox.showwarning(
            title="Atención", message="Datos Requeridos y/o no validos")


def limpiarCalculoMerma():
    global pcepl, pcspl, rtsoLabel, rmlpLabel
    global pcept, pcspt, rtphLabel, rmtpLabel
    global pcepd, pcspd, rtcasLabel, rmcpLabel
    global pnoiepr, pchospr, rtcaschoLabel, rmpchoLabel
    global rmermatotalLabel
    global btnAddMermaTotal, btnCalcularMermaTotal, btnLimpiarMermaTotal

    pcepl.set(0.00)
    pcspl.set(0.00)
    rtsoLabel.config(text=0.00)
    rmlpLabel.config(text=0.00)
    pcept.set(0.00)
    pcspt.set(0.00)
    rtphLabel.config(text=0.00)
    rmtpLabel.config(text=0.00)
    pcepd.set(0.00)
    pcspd.set(0.00)
    rtcasLabel.config(text=0.00)
    rmcpLabel.config(text=0.00)
    pnoiepr.set(0.00)
    pchospr.set(0.00)
    rtcaschoLabel.config(text=0.00)
    rmpchoLabel.config(text=0.00)
    rmermatotalLabel.config(text=0.00)

    if btnAddMermaTotal["state"] == DISABLED:
        btnAddMermaTotal["state"] = NORMAL
    else:
        btnAddMermaTotal["state"] = DISABLED


def guardarCalculoMermaTotal():
    global pcepl, pcspl
    global pcept, pcspt
    global pcepd, pcspd
    global pnoiepr, pchospr
    global ml, mt, md, mch, mtr

    global btnAddMermaTotal, btnCalcularMermaTotal, btnLimpiarMermaTotal

    vpcepl = float(pcepl.get())
    vpcspl = float(pcspl.get())
    vpcept = float(pcept.get())
    vpcspt = float(pcspt.get())
    vpcepd = float(pcepd.get())
    vpcspd = float(pcspd.get())
    vpnoiepr = float(pnoiepr.get())
    vpchospr = float(pchospr.get())

    now = datetime.now()
    fecha = now.strftime("%Y-%m-%d %H:%M:%S")

    # crear el cursor
    cursor = conexion.cursor()

    # definir la consulta con parámetros
    query = "INSERT INTO produccion VALUES(null,%s,%s,100,%s,%s,%s,100,%s,%s,%s,100,%s,%s,%s,100,%s,%s,%s);"

    # ejecutar la consulta con los valores de las variables
    cursor.execute(query, (vpcepl, vpcspl, ml, vpcept, vpcspt, mt,
                   vpcepd, vpcspd, md, vpnoiepr, vpchospr, mch, mtr, fecha))

    # confirmar los cambios en la base de datos
    conexion.commit()

    # cerrar la conexión
    conexion.close()

    MessageBox.showinfo(title="Atención", message="Registro Guardado!!!")


def ventanaPanel():
    # Ventana Panel
    tkVentanaPanel = Toplevel(tkVentanaLogin)
    tkVentanaLogin.withdraw()
    tkVentanaPanel.geometry("1080x450")
    tkVentanaPanel.title("Bahaleon - Menu Principal")
    tkVentanaPanel.configure(bg="white")

    # logo
    logo = Image.open('logo.jpg')
    image = logo.resize((300, 300), Image.LANCZOS)
    logo2 = ImageTk.PhotoImage(image)

    # etiqueta de la imagen
    logolabel = Label(tkVentanaPanel, image=logo2).place(x=150, y=75)

    # Etiqueta Titulo de la Ventana
    tituloLabel = Label(tkVentanaPanel, text=" Bahaleon - Menu Principal", font=(
        fuentePrincipal, 20), bg="#239e2a", fg='#fff').place(x=padding*2, y=padding)
    # Separador
    ttk.Separator(tkVentanaPanel).place(x=0, y=padding*6, relwidth=1)

    # boton de Ventana de Calculadora
    ventanaCalculoMermaButton = Button(tkVentanaPanel, text="Calculadora", font=(
        fuentePrincipal, 12), bg=bgColorPrimary, fg='#fff', command=ventanaCalculoMerma).place(x=600, y=150)
    # boton de salir
    salirButton = Button(tkVentanaPanel, text="Salir", font=(
        fuentePrincipal, 12), bg=bgColorDanger, fg='#fff', command=salir).place(x=600, y=200)
    tkVentanaPanel.mainloop()


def validarUsuario(username, password):
    # now = datetime.now()
    # fecha = now.strftime("%Y-%m-%d %H:%M:%S")
    cursor = conexion.cursor()
    # cursor.execute("CREATE TABLE usuario (id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,nombre TEXT NOT NULL,usuario TEXT NOT NULL,clave TEXT NOT NULL);")
    # cursor.execute("CREATE TABLE produccion (id_produccion INTEGER PRIMARY KEY,pcepl DECIMAL(10, 2) NOT NULL,pcspl DECIMAL(10, 2) NOT NULL,rtso DECIMAL(10, 2) NOT NULL,rmlp DECIMAL(10, 2) NOT NULL,pcept DECIMAL(10, 2) NOT NULL,pcspt DECIMAL(10, 2) NOT NULL,rtph DECIMAL(10, 2) NOT NULL,rmtp DECIMAL(10, 2) NOT NULL,pcepd DECIMAL(10, 2) NOT NULL,pcspd DECIMAL(10, 2) NOT NULL,rtcas DECIMAL(10, 2) NOT NULL,rmcp DECIMAL(10, 2) NOT NULL,pnoiepr DECIMAL(10, 2) NOT NULL,pchospr DECIMAL(10, 2) NOT NULL,rtcascho DECIMAL(10, 2) NOT NULL,rmpcho DECIMAL(10, 2) NOT NULL,rmermatotal DECIMAL(10, 2) NOT NULL,fecreacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL);")
    # cursor.execute("INSERT INTO usuario VALUES(null,'administrador','admin','12345');")
    # query = "INSERT INTO produccion VALUES(null,1000,900,100,10.00,900,800,100,11.11,800,700,100,12.50,700,600,100,14.28,47.89,'"+fecha+"');"
    # cursor.execute(query)
    # conexion.commit()
    # conexion.close()

    if len(username.get()) == 0 or len(password.get()) == 0:
        MessageBox.showwarning(
            title="Atención", message="Usuario y Clave Requeridos")
    else:
        cursor.execute('SELECT clave FROM usuario WHERE usuario=%s and clave=%s',
                       (username.get(), password.get()))
        result = cursor.fetchone()
        if result is not None:
            MessageBox.showinfo(title="Atención", message="Bienvenido/a")
            ventanaPanel()
        else:
            MessageBox.showwarning(
                title="Atención", message="Usuario y Clave incorrectos")


# Ventana tkVentanaLogin
tkVentanaLogin = tkinter.Tk()
tkVentanaLogin.geometry('600x650')
tkVentanaLogin.title('Bahaleon')
tkVentanaLogin.configure(bg="white")
tkVentanaLogin.resizable(False, False)


# logo
logo = Image.open('logo.jpg')
image = logo.resize((300, 300), Image.LANCZOS)
logo2 = ImageTk.PhotoImage(image)

# etiqueta de la imagen
logolabel = Label(tkVentanaLogin, image=logo2).place(x=150, y=75)

# etiqueta del usuario
usernameLabel = Label(tkVentanaLogin, text="usuario",
                      bg='#ae6727').place(x=165, y=395)
username = StringVar()
usernameEntry = Entry(
    tkVentanaLogin, textvariable=username).place(x=240, y=395)

# etiqueta de la clave
passwordLabel = Label(tkVentanaLogin, text="clave",
                      bg='#ae6727').place(x=165, y=420)
password = StringVar()
passwordEntry = Entry(tkVentanaLogin, textvariable=password,
                      show='*').place(x=240, y=420)

validarUsuario = partial(validarUsuario, username, password)

# boton de inicio
loginButton = Button(tkVentanaLogin, bg='#239e2a',
                     text="Ingresar", command=validarUsuario).place(x=165, y=450)

tkVentanaLogin.mainloop()
