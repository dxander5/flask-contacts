import pymysql

class Bd:
    def __init__(self):
        self.conection = pymysql.connect(
            host='localhost',
            user='root',
            password='Db1123',
            db='ejercicios'
        )

        self.cursor = self.conection.cursor()
        # print('conexion exitosa')

    def insert(self, nombre, telefono, email):
        sql = f"INSERT INTO contactos (nombre, telefono, email) VALUES ('{nombre}', '{telefono}','{email}')"
        try:
            self.cursor.execute(sql)
            self.conection.commit()
            # print('Se agrego el producto')
        except Exception as e:
            raise
    def select(self, id):
        sql = f'SELECT * FROM contactos WHERE id={id}'
        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone()
            return user
            # print("Id: ", user[0], " nombre: ", user[1], " edad ", user[2])
        except Exception as e:
            raise

    def selectAllData(self):
        sql = 'SELECT * FROM contactos'
        try:
            self.cursor.execute(sql)
            users = self.cursor.fetchall()
            return users
            # for user in users:
            #     print("Id: ", user[0], " nombre: ", user[1], " telefono ", user[2], " email ", user[3])
            #     # print('\n')
        except Exception as e:
            raise

    def update(self, id, name, phone, email):
        sql = f"UPDATE contactos set nombre='{name}', telefono='{phone}', email='{email}' WHERE id={id}"

        try:
            self.cursor.execute(sql)
            self.conection.commit()
            # print('Se actualizo el dato con el id', id)
        except Exception as e:
            raise

    def delete(self, id):
        sql = f"DELETE FROM contactos WHERE id={id}"
        try:
            self.cursor.execute(sql)
            self.conection.commit()
            # print('Se elimino el producto con el id', id)
        except Exception as e:
            raise
    def closeConnection(self):
        print('conexion cerrada')
        self.conection.close()