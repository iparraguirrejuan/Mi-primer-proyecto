import mysql.connector
import os


class App:

    def __init__(self):
        self.conn = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'app_antropometria',
        )
        self.cursor = self.conn.cursor()

    def Posicion_pacientes(self):
        select_pacientes = "use pacientes" 
        self.cursor.execute(select_pacientes)
        print("Ahora usted esta trabajando con la tabla pacientes")
        

    def Insertar_paciente(self):
        nombre = input("Ingrese nombre: ")
        apellido = input("Ingrese apellido: ")
        edad = int(input("Ingrese edad: "))
        peso = float(input("Ingrese peso: "))
        altura = float(input("Ingrese altura: "))
        obra_social = input("Ingrese Obra social: ")
        sexo = input("Seleccione sexo: ")
        sql = "insert into pacientes(nombre, apellido, edad, peso, altura, obra_social, sexo) values('{nombre}','{apellido}','{edad}','{peso}','{altura}','{obra_social}', '{sexo}')".format(nombre=nombre, apellido=apellido, edad=edad, peso=peso, altura=altura, obra_social=obra_social, sexo = sexo)
        self.cursor.execute(sql)
        print("Ingresado correctamente \n")
        self.conn.commit()
        os.system('pause')

    def listar_pacientes(self):
        lista_pacientes = "select * from pacientes"
        self.cursor.execute(lista_pacientes)
        resultado_paciente = self.cursor.fetchall()
        for fila in resultado_paciente:
            print(fila)
    
    def buscar_paciente_nombre(self):
        columna = input("Ingrese en que columna desea buscar: ")
        consulta = f"select * from prueba1 where {columna} like %s "
        valor= input("Ingrese el valor a buscar: ")
        parametro = f"%{valor}%"
        self.cursor.execute(consulta, (parametro,))
        resultados = self.cursor.fetchall()
        for resultado in resultados:
            print(resultado)

    def eliminar_paciente(self):
       columna= input("Ingrese en que columna quiere buscar: ")
       consutla = f"delete from pacientes where {columna} = %s"
       valor = input("Introduce el valor a borrar: ")
       parametro = f"{valor}"
       self.cursor.execute(consutla, (parametro,))
       self.conn.commit()
       print("Los datos se borraron correctamente")
        
    def __del__(self):
        self.conn.close()
        self.cursor.close()
        print("Conexion con base de datos cerrada")






        