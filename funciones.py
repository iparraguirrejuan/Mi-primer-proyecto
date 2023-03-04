import mysql.connector
import os


class App:

    def __init__(self):
        self.conn = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'proyecto_antropometria',
        )
        self.cursor = self.conn.cursor()

    def Insertar(self):
        nombre = input("Ingrese nombre: ")
        apellido = input("Ingrese apellido: ")
        edad = int(input("Ingrese edad: "))
        peso = float(input("Ingrese peso: "))
        altura = float(input("Ingrese altura: "))
        obra_social = input("Ingrese Obra social: ")
        sql = "insert into pacientes(nombre, apellido, edad, peso, altura, obra_social) values('{nombre}','{apellido}','{edad}','{peso}','{altura}','{obra_social}')".format(nombre=nombre, apellido=apellido, edad=edad, peso=peso, altura=altura, obra_social=obra_social)
        self.cursor.execute(sql)
        print("Ingresado correctamente \n")
        self.conn.commit()
        os.system('pause')



        