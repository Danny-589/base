#Módulo para realizar Crud de autos
#Fecha: 6/04/2026

import mysql.connector


#Conexión a la base de datos
def conectar_con_base_datos():
    return mysql.connector.connect(
        user='root',
        password='1234',
        host='127.0.0.1',
        database='rentacar',
        port='3306'
    )


#Agregar auto
def agregar_auto_db(código, matrícula, descripción, marca,
                    tipo, modelo, color_1, color_2,
                    nro_pasajeros, año_auto, combustible):

    conexion=conectar_con_base_datos()
    cursor=conexion.cursor()

    query="""
    INSERT INTO auto
    (cod_auto, mat_auto, des_auto, mar_auto,
    tip_auto, mod_auto, col1_auto,
    col2_auto, numpas_auto, a_auto, comb_auto)

    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    cursor.execute(query,(
        código,
        matrícula,
        descripción,
        marca,
        tipo,
        modelo,
        color_1,
        color_2,
        nro_pasajeros,
        año_auto,
        combustible
    ))

    conexion.commit()

    cursor.close()
    conexion.close()


#Obtener un auto por ID
def obtener_auto_db(id):

    conexion=conectar_con_base_datos()
    cursor=conexion.cursor()

    query="SELECT * FROM auto WHERE id_auto=%s"

    cursor.execute(query,(id,))
    auto=cursor.fetchone()

    cursor.close()
    conexion.close()

    return auto


#Modificar auto
def modificar_auto_db(código, matrícula, descripción,
                      marca, tipo, modelo,
                      color_1, color_2,
                      nro_pasajeros,
                      año_auto,
                      combustible,
                      id):

    conexion=conectar_con_base_datos()
    cursor=conexion.cursor()

    query="""
    UPDATE auto
    SET
    cod_auto=%s,
    mat_auto=%s,
    des_auto=%s,
    mar_auto=%s,
    tip_auto=%s,
    mod_auto=%s,
    col1_auto=%s,
    col2_auto=%s,
    numpas_auto=%s,
    a_auto=%s,
    comb_auto=%s
    WHERE id_auto=%s
    """

    cursor.execute(query,(
        código,
        matrícula,
        descripción,
        marca,
        tipo,
        modelo,
        color_1,
        color_2,
        nro_pasajeros,
        año_auto,
        combustible,
        id
    ))

    conexion.commit()

    cursor.close()
    conexion.close()


#Eliminar auto
def eliminar_auto_db(id):

    conexion=conectar_con_base_datos()

    try:

        cursor=conexion.cursor()

        query="DELETE FROM auto WHERE id_auto=%s"

        cursor.execute(query,(id,))
        conexion.commit()

    except Exception as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        conexion.close()


#Consultar un auto
def consultar_auto_db(id):

    conexion=conectar_con_base_datos()
    cursor=conexion.cursor()

    query="SELECT * FROM auto WHERE id_auto=%s"

    cursor.execute(query,(id,))
    auto=cursor.fetchone()

    cursor.close()
    conexion.close()

    return auto


#Consultar todos los autos
def consultar_autos_db():

    conexion=conectar_con_base_datos()

    try:

        cursor=conexion.cursor()

        query="""
        SELECT
        id_auto,
        cod_auto,
        mat_auto,
        des_auto
        FROM auto
        """

        cursor.execute(query)

        autos=cursor.fetchall()

        return autos

    except Exception as e:
        print(f"Error al consultar autos: {e}")
        return []

    finally:
        cursor.close()
        conexion.close()