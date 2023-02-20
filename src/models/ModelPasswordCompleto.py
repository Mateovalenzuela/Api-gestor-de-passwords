from src.database.db_postgresql import get_connection
from src.models.entities.PasswordCompleto import PasswordCompleto
from src.models.ModelPassword import ModelPassword
from src.models.ModelDetallePassword import ModelDetallePassword
from src.utils.IdGenerate import IdGenerate

from src.models.entities.Password import Password
from src.models.entities.DetallePassword import DetallePassword


class ModelPasswordCompleto:

    @classmethod
    def add_password_completo(cls, obj_password_completo):
        try:
            connection = get_connection()
            with connection:
                with connection.cursor() as cursor:
                    idObjPassword = IdGenerate.generate_id()
                    idObjDetallePassword = IdGenerate.generate_id()

                    obj_password_completo.id_password = idObjPassword
                    obj_password_completo.id_detalle_password = idObjDetallePassword

                    # set id's in object's
                    obj_password_completo.id = IdGenerate.generate_id()
                    obj_password_completo.obj_password.id = idObjPassword
                    obj_password_completo.obj_detalle_password.id = idObjDetallePassword

                    # falta añadir los metodos add de los otros dos modelos

                    transaccionAddPassword = ModelPassword.add_password(obj_password_completo.obj_password)
                    cursor.execute(transaccionAddPassword[0], transaccionAddPassword[1])

                    transaccionAddDetallePassword = ModelDetallePassword.add_detalle_password(
                        obj_password_completo.obj_detalle_password)
                    cursor.execute(transaccionAddDetallePassword[0], transaccionAddDetallePassword[1])

                    query = f'''INSERT INTO \"conjunto-password-detalle\" (id, \"PASSWORD_ID\", \"DETALLE_PASSWORD_ID\", 
                    baja)
                                VALUES (%s, %s, %s, %s)'''
                    tuplaDeValores = (obj_password_completo.id, obj_password_completo.id_password,
                                      obj_password_completo.id_detalle_password, obj_password_completo.baja)

                    cursor.execute(query, tuplaDeValores)
                    affectedRows = cursor.rowcount

            return affectedRows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_password_completo(cls, id):
        try:
            connection = get_connection()
            with connection:
                with connection.cursor() as cursor:
                    query = f'''SELECT \"PASSWORD_ID\", \"DETALLE_PASSWORD_ID\", \"fecha_creacion\" 
                                FROM \"conjunto-password-detalle\" 
                                WHERE id=\'{id}\''''
                    cursor.execute(query)
                    passwordCompleto = cursor.fetchone()

            idObjPassword = passwordCompleto[0]
            idObjDetallePassword = passwordCompleto[1]
            fechaCreacion = passwordCompleto[2]

            objPassword = ModelPassword.get_password(idObjPassword)
            objDetallePassword = ModelDetallePassword.get_detalle_password(idObjDetallePassword)

            objPasswordCompleto = PasswordCompleto(id, objPassword, objDetallePassword)
            objPasswordCompleto.fecha_creacion = fechaCreacion
            passwordCompleto = objPasswordCompleto.to_json()

            return passwordCompleto
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_all_password_completo(cls):
        try:
            connection = get_connection()
            listaDePasswords = []
            with connection:
                with connection.cursor() as cursor:
                    query = f'''SELECT id, \"PASSWORD_ID\", \"DETALLE_PASSWORD_ID\", \"fecha_creacion\" 
                                    FROM \"conjunto-password-detalle\" 
                                    WHERE baja=False'''
                    cursor.execute(query)
                    all_passwords = cursor.fetchall()

            for password in all_passwords:
                idObjPassword = password[0]
                idObjDetallePassword = password[1]
                fechaCreacion = password[2]

                objPassword = ModelPassword.get_password(idObjPassword)
                objDetallePassword = ModelDetallePassword.get_detalle_password(idObjDetallePassword)

                objPasswordCompleto = PasswordCompleto(id, objPassword, objDetallePassword)
                objPasswordCompleto.fecha_creacion = fechaCreacion
                passwordCompleto = objPasswordCompleto.to_json()
                listaDePasswords.append(passwordCompleto)

            return listaDePasswords
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_password_completo(cls, id):
        try:
            connection = get_connection()
            with connection:
                with connection.cursor() as cursor:
                    query = f'''UPDATE \"conjunto-password-detalle\"
                                SET baja=True
                                WHERE id=\'{id}\''''
                    cursor.execute(query)
                    row_afecteds = cursor.rowcount()
            if row_afecteds:
                return row_afecteds
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_password_completo(cls, obj_password_completo):
        try:
            connection = get_connection()
            with connection:
                with connection.cursor() as cursor:
                    # generar nuevos id's para obj password y obj detalle password

                    transaccionPassword = ModelPassword.add_password(obj_password_completo.obj_password)
                    cursor.execute(transaccionPassword[0], transaccionPassword[1])

                    transaccionDetallePassword = ModelDetallePassword.add_detalle_password(
                        obj_password_completo.obj_detalle_password)
                    cursor.execute(transaccionDetallePassword[0], transaccionDetallePassword[1])

                    query = f'''UPDATE \"conjunto-password-detalle\" 
                                SET \'PASSWORD_ID\'=%s, \'DETALLE_PASSWORD_ID\'=%s 
                                WHERE id=\'{obj_password_completo.id}\''''

                    tuplaDeValores = (
                    obj_password_completo.obj_password.id, obj_password_completo.obj_detalle_password.id)
                    cursor.execute(query, tuplaDeValores)
                    affectedRows = cursor.rowcount

            return affectedRows
        except Exception as ex:
            raise Exception(ex)


if __name__ == '__main__':
    objPassword = Password(None, 'gmail123')
    objDetallePassword = DetallePassword(None, 'nateovalenzuela@gmail.com', 'gmail')
    objPasswordCompleto = PasswordCompleto(None, objPassword, objDetallePassword)

    # ModelPasswordCompleto.add_password_completo(objPasswordCompleto)
    id = 'c3e855c9-1e84-4943-9c9d-27fc50ee8d38'
    passwordCompleto = ModelPasswordCompleto.get_password_completo(id)
    print(passwordCompleto)
