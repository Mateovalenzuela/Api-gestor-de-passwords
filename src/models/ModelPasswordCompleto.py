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

                    transaccionAddDetallePassword = ModelDetallePassword.add_detalle_password(obj_password_completo.obj_detalle_password)
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
            fechaCreacion = [2]

            objPassword = ModelPassword.get_password(idObjPassword)
            objDetallePassword = ModelDetallePassword.get_detalle_password(idObjDetallePassword)

            objPasswordCompleto = PasswordCompleto(id, objPassword, objDetallePassword)
            objPasswordCompleto.fecha_creacion = fechaCreacion
            passwordCompleto = objPasswordCompleto.to_json()

            return passwordCompleto
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
    objPassword = Password(None, 'gmail123')
    objDetallePassword = DetallePassword(None, 'nateovalenzuela@gmail.com', 'gmail')
    objPasswordCompleto = PasswordCompleto(None, objPassword, objDetallePassword)

    #ModelPasswordCompleto.add_password_completo(objPasswordCompleto)
    id = 'c3e855c9-1e84-4943-9c9d-27fc50ee8d38'
    passwordCompleto = ModelPasswordCompleto.get_password_completo(id)
    print(passwordCompleto)
