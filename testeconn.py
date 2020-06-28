import pymysql

class DataBase():
    def __init__(self):
        self.conection = pymysql.connect(
            host='localhost',
            user='user_test',
            password='12345',
            db='databasesc'
        )
        self.cursor = self.conection.cursor()

    def select_user(self):
        sql = 'SELECT * FROM tablasc'
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()

            for user in data:
                print("id-> {0} nombre-> {1}".format(user[0], user[1]))
        except:
            raise

    def getName(self, name):
        sql = 'SELECT * FROM tablasc WHERE nombre like "%{0}%"'.format(name)
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()

            out_data = ""

            if data:
                for name in data:
                    out_data += "{}. ".format(name[1])
                print(out_data)
                self.conection.close()
            else: 
                print("no se encontro nombre")
        except:
            raise

if __name__ == "__main__":
    from BK.BasedeDatos import BasedeDatos as bd
    print(bd.reqName("Juan")["req"])

