from src.database.db_postgresql import get_connection
from src.models.entities.Password import Password



class ModelPassword:

    @classmethod
    def add_password(cls, obj_password):
        try:
            connection = get_connection()
            with connection:
                with connection.cursor() as cursor:
                    obj_password.clave = Password.generate_key()

                    query = f'''INSERT INTO password (id, password, clave)
                                VALUES (%s, PGP_SYM_ENCRYPT(%s, \'{obj_password.clave}\'), %s)'''
                    tuplaDeValores = (obj_password.id, obj_password.password, obj_password.clave)

                    #cursor.execute(query, tuplaDeValores)
                    #affectedRows = cursor.rowcount

                    transaccion = (query, tuplaDeValores)

            return transaccion
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
            password = objPassword.to_json()
            return password
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def update_password(cls, obj_password):
        try:
            connection = get_connection()
            with connection:
                with connection.cursor() as cursor:
                    claveNueva = Password.generate_key()

                    query = f'''UPDATE password SET password=PGP_SYM_ENCRYPT(%s,\'{claveNueva}\'), clave=%s  
                                WHERE id=\'{obj_password.id}\''''
                    tuplaDeValores = (obj_password.password, claveNueva)
                    cursor.execute(query, tuplaDeValores)
                    affectedRows = cursor.rowcount

            return affectedRows
        except Exception as ex:
            raise Exception(ex)


if __name__ == '__main__':
    objPassword = Password('fwfwqfewfef', 'batata')
    #ModelPassword.add_password(objPassword)

    password = ModelPassword.get_password(objPassword.id)
    print(password)

    # objPassword.password = 'Manzana verde'
    # ModelPassword.update_password(objPassword)

    password = ModelPassword.get_password(objPassword.id)
    print(password)
