from src.database.db_postgresql import get_connection
from src.models.entities.Detalle import Detalle


class ModelDetalle:

    @classmethod
    def add_detalle(cls, obj_detalle, return_query=True):
        try:
            query = f'''INSERT INTO detalle (id, titulo, usuario, url, descripcion)
                                            VALUES (%s, %s, %s, %s, %s)'''
            tuplaDeValores = (
                obj_detalle.id, obj_detalle.titulo, obj_detalle.usuario,
                obj_detalle.url, obj_detalle.descripcion)

            if return_query:
                transaccion = (query, tuplaDeValores)
                return transaccion
            else:
                connection = get_connection()
                with connection:
                    with connection.cursor() as cursor:
                        cursor.execute(query, tuplaDeValores)
                        return obj_detalle.id
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_detalle(cls, id):
        try:
            connection = get_connection()
            with connection:
                with connection.cursor() as cursor:
                    query = f'''SELECT usuario, titulo, url, descripcion FROM detalle WHERE id=\'{id}\''''
                    cursor.execute(query)
                    detalle = cursor.fetchone()

            objDetalle = Detalle(id, detalle[0], detalle[1], detalle[2],
                                 detalle[3])
            return objDetalle
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_detalle(cls, obj_detalle, return_query=True):
        try:
            query = f'''UPDATE detalle SET usuario=%s, titulo=%s, url=%s, descripcion=%s  
                                            WHERE id=\'{obj_detalle.id}\''''
            tuplaDeValores = (obj_detalle.usuario, obj_detalle.titulo,
                              obj_detalle.url, obj_detalle.descripcion)

            if return_query:
                transaccion = (query, tuplaDeValores)
                return transaccion
            else:
                connection = get_connection()
                with connection:
                    with connection.cursor() as cursor:
                        cursor.execute(query, tuplaDeValores)
                        return obj_detalle.id
        except Exception as ex:
            raise Exception(ex)


if __name__ == '__main__':
    id = '452a0505-bd52-478b-a3df-87abd25d646b'
    detalle = ModelDetalle.get_detalle(id)
    print(detalle)

