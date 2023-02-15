from database.db_postgresql import get_connection
from models.entities.Password import Password


class ModelPassword:
    @classmethod
    def get_passwords(cls):
        try:
            connection = get_connection()
            listaDePassword = []

            with connection:
                with connection.cursor() as cursor:
                    clave = 'CLAVE_AES'
                    # query = f'SELECT id, usuario,  PGP_SYM_DECRYPT(password::bytea, {clave}), titulo, url, ' \
                    #       f'descripcion, fecha_creacion FROM gestor_password WHERE baja=false'

                    query = f'SELECT id, usuario,  password, titulo, url, ' \
                           f'descripcion, fecha_creacion FROM gestor_password WHERE baja=false'
                    cursor.execute(query)
                    resultset = cursor.fetchall()

                    for registro in resultset:
                        objPassword = Password(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5])
                        objPassword.fecha_creacion = registro[6]
                        listaDePassword.append(objPassword.to_JSON())

            return listaDePassword
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_password(cls, obj_password):
        try:
            connection = get_connection()
            with connection:
                with connection.cursor() as cursor:
                    query = f'INSERT INTO gestor_password (usuario, password, titulo, url, descripcion, baja) ' \
                            f'VALUES (%s, PGP_SYM_ENCRYPT(%s,\'CLAVE_AES\'), %s, %s, %s, %s)'
                    tuplaDeValores = (obj_password.usuario, obj_password.password, obj_password.url,
                                      obj_password.titulo, obj_password.descripcion, obj_password.baja)
                    cursor.execute(query, tuplaDeValores)
                    affectedRows = cursor.rowcount

            return affectedRows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_password(cls, id):
        try:
            connection = get_connection()
            with connection:
                with connection.cursor() as cursor:
                    query = f'SELECT id, usuario,  PGP_SYM_DECRYPT(password::bytea, \'CLAVE_AES\'), titulo, url, ' \
                            f'descripcion, fecha_creacion FROM gestor_password WHERE baja=false and id={id}'
                    cursor.execute(query)
                    registro = cursor.fetchone()

            password = None
            if registro is not None:
                objPassword = Password(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5])
                objPassword.fecha_creacion = registro[6]
                password = objPassword.to_JSON()
                return password
            else:
                return password
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def delete_password(cls, obj_password):
        try:
            connection = get_connection()
            with connection:
                with connection.cursor() as cursor:
                    query = f'UPDATE gestor_password SET baja=TRUE WHERE baja=FALSE and id={obj_password.id}'
                    cursor.execute(query)
                    affectedRows = cursor.rowcount

                return affectedRows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_password(cls, obj_password):
        try:
            connection = get_connection()
            with connection:
                with connection.cursor() as cursor:
                    query = f'UPDATE gestor_password SET usuario=%s, password=PGP_SYM_ENCRYPT(%s,\'CLAVE_AES\'),  ' \
                            f'titulo=%s, url=%s, descripcion=%s WHERE id={obj_password.id}'
                    tuplaDeValores = (obj_password.usuario, obj_password.password, obj_password.titulo,
                                      obj_password.url, obj_password.descripcion)
                    cursor.execute(query, tuplaDeValores)
                    affectedRows = cursor.rowcount

            return affectedRows
        except Exception as ex:
            raise Exception(ex)


if __name__ == '__main__':
    pass