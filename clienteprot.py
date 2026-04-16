#Módulo para realizar Crud de clientes
#Fecha: 6/04/2026

#pip install mysql-connector-python
import mysql.connector

#Método para la conección con la base de datos

def conectar_con_base_datos():
    return mysql.connector.connect(user='root', password='1234',
                                   host='127.0.0.1',
                                   database='rentacar',
                                   port='3306')

#Método para agragar cliente en la base de datos
def agregar_cliente_db(cedula, nombres, apellidos, sexo, direccion, telefono, correo, fecha_nac):
    conexion=conectar_con_base_datos()
    cursor=conexion.cursor()
    query="insert into cliente (ced_cliente ,nom_cliente ,ape_cliente , sex_cliente , dir_cliente , tel_cliente , cor_cliente,fec_nac_cliente) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(query,(cedula, nombres, apellidos, sexo, direccion, telefono, correo, fecha_nac))
    conexion.commit()
    cursor.close()
    conexion.close()
