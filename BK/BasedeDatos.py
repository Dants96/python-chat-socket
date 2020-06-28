import pymysql

class BasedeDatos():

    @staticmethod
    def reqName(nom):
        try:
            conexion = pymysql.connect(
                host='localhost',
                user='user_test',
                password='12345',
                db='databasesc'
            )
            cursor = conexion.cursor()
            sentencia = "SELECT nombre FROM tablasc WHERE nombre like '%{}%'".format(nom)
            cursor.execute(sentencia)
            datos = cursor.fetchall()
            out_datos = ""
            conexion.close()
            if datos :
                for nom in datos:
                    out_datos += "{}. ".format(nom[0])
                return {"get":True, "req":out_datos}
            else:
                return {"get": False,"req": "No se encontro nombre en la base de datos"}
        except:
            raise
            return {"get": False,"req": "Error al conectar con la base de datos"}

