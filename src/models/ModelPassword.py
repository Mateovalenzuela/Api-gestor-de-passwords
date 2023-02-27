from src.database.db_postgresql import get_connection
from src.models.entities.Password import Password


class ModelPassword:

    @classmethod
    def add_password(cls, obj_password, return_query=True):
        try:
            obj_password.clave = Password.generate_key()
            query = f'''INSERT INTO password (id, password, clave)
                                            VALUES (%s, PGP_SYM_ENCRYPT(%s, \'{obj_password.clave}\'), %s)'''
            tuplaDeValores = (obj_password.id, obj_password.password, obj_password.clave)

            if return_query:
                transaccion = (query, tuplaDeValores)
                return transaccion
            else:
                connection = get_connection()
                with connection:
                    with connection.cursor() as cursor:
                        cursor.execute(query, tuplaDeValores)
                        return obj_password.id

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_password(cls, id):
        try:
            connection = get_connection()
            with connection:
                with connection.cursor() as cursor:
                    query = f'''SELECT clave FROM password WHERE id=\'{id}\''''
                    cursor.execute(query)
                    clave = cursor.fetchone()[0]

                    query = f'''SELECT PGP_SYM_DECRYPT(password::bytea, \'{clave}\') 
                                FROM password WHERE id=\'{id}\''''
                    cursor.execute(query)
                    password = cursor.fetchone()[0]

            objPassword = Password(id, password)
            return objPassword
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_password(cls, obj_password, return_query=True):
        try:
            claveNueva = Password.generate_key()

            query = f'''UPDATE password SET password=PGP_SYM_ENCRYPT(%s,\'{claveNueva}\'), clave=%s  
                                            WHERE id=\'{obj_password.id}\''''
            tuplaDeValores = (obj_password.password, claveNueva)

            if return_query:
                transaccion = (query, tuplaDeValores)
                return transaccion
            else:
                connection = get_connection()
                with connection:
                    with connection.cursor() as cursor:
                        cursor.execute(query, tuplaDeValores)
                        return obj_password.id

        except Exception as ex:
            raise Exception(ex)


if __name__ == '__main__':
    id = 'dca03d96-8052-428a-8be9-0b41bc628cd5'
    password = ModelPassword.get_password(id)
    print(password)
