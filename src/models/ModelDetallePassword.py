from src.database.db_postgresql import get_connection
from src.models.entities.DetallePassword import DetallePassword


class ModelDetallePassword:

    @classmethod
    def add_detalle_password(cls, obj_detalle_password):
        try:
            connection = get_connection()
            with connection:
                with connection.cursor() as cursor:
                    query = f'''INSERT INTO \"detalle-password\" (id, titulo, usuario, url, descripcion)
                                VALUES (%s, %s, %s, %s, %s)'''
                    tuplaDeValores = (
                    obj_detalle_password.id, obj_detalle_password.titulo, obj_detalle_password.usuario,
                    obj_detalle_password.url, obj_detalle_password.descripcion)

                    #cursor.execute(query, tuplaDeValores)
                    #affectedRows = cursor.rowcount

                    transaccion = (query, tuplaDeValores)

            return transaccion
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_detalle_password(cls, id):
        try:
            connection = get_connection()
            with connection:
                with connection.cursor() as cursor:
                    query = f'''SELECT usuario, titulo, url, descripcion FROM \"detalle-password\" WHERE id=\'{id}\''''
                    cursor.execute(query)
                    detallePassword = cursor.fetchone()

            objDetallePassword = DetallePassword(id, detallePassword[0], detallePassword[1], detallePassword[2],
                                                 detallePassword[3])

            detallePassword = objDetallePassword.to_json()
            return detallePassword
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_detalle_password(cls, obj_detalle_password):
        try:
            connection = get_connection()
            with connection:
                with connection.cursor() as cursor:

                    query = f'''UPDATE \"detalle-password\" SET usuario=%s, titulo=%s, url=%s, descripcion=%s  
                                WHERE id=\'{obj_detalle_password.id}\''''
                    tuplaDeValores = (obj_detalle_password.usuario, obj_detalle_password.titulo,
                                      obj_detalle_password.url, obj_detalle_password.descripcion)
                    cursor.execute(query, tuplaDeValores)
                    affectedRows = cursor.rowcount

            return affectedRows
        except Exception as ex:
            raise Exception(ex)


if __name__ == '__main__':
    objDetallePassword = DetallePassword('fhwefiergeguhfuwi', 'nateovalenzuela@gmail.com')
    #ModelDetallePassword.add_detalle_password(objDetallePassword)

    detallePassword = ModelDetallePassword.get_detalle_password(objDetallePassword.id)
    print(detallePassword)

    objDetallePassword.usuario = 'mateovalenzuela773@gmail.com'
    ModelDetallePassword.update_detalle_password(objDetallePassword)

    detallePassword = ModelDetallePassword.get_detalle_password(objDetallePassword.id)
    print(detallePassword)
