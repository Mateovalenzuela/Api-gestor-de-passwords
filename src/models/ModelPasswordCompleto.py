from src.database.db_postgresql import get_connection
from src.models.entities.PasswordCompleto import PasswordCompleto
from src.models.ModelPassword import ModelPassword
from src.models.ModelDetalle import ModelDetalle
from src.utils.IdGenerate import IdGenerate

from src.models.entities.Password import Password
from src.models.entities.Detalle import Detalle


class ModelPasswordCompleto:

    @classmethod
    def add_password_completo(cls, obj_password_completo):
        try:
            connection = get_connection()
            with connection:
                with connection.cursor() as cursor:
                    # generate id's
                    idObjPasswordCompleto = IdGenerate.generate_id()
                    idObjPassword = IdGenerate.generate_id()
                    idObjDetalle = IdGenerate.generate_id()

                    # set id's in object's
                    obj_password_completo.id = idObjPasswordCompleto
                    obj_password_completo.password_id = idObjPassword
                    obj_password_completo.obj_password.id = idObjPassword
                    obj_password_completo.detalle_id = idObjDetalle
                    obj_password_completo.obj_detalle.id = idObjDetalle

                    transaccionAddPassword = ModelPassword.add_password(obj_password_completo.obj_password)
                    cursor.execute(transaccionAddPassword[0], transaccionAddPassword[1])

                    transaccionAddDetalle = ModelDetalle.add_detalle(obj_password_completo.obj_detalle_password)
                    cursor.execute(transaccionAddDetalle[0], transaccionAddDetalle[1])

                    query = f'''INSERT INTO password_detalle (id, password_id, detalle_id, baja)
                                VALUES (%s, %s, %s, %s)'''
                    tuplaDeValores = (obj_password_completo.id, obj_password_completo.password_id,
                                      obj_password_completo.detalle_id, obj_password_completo.baja)

                    cursor.execute(query, tuplaDeValores)

            return obj_password_completo.id
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_password_completo(cls, id):
        try:
            connection = get_connection()
            with connection:
                with connection.cursor() as cursor:
                    query = f'''SELECT password_id, detalle_id, fecha_creacion
                                FROM password_detalle 
                                WHERE id=\'{id}\' and baja=False'''
                    cursor.execute(query)
                    objPasswordCompleto = cursor.fetchone()

            idObjPassword = objPasswordCompleto[0]
            idObjDetalle = objPasswordCompleto[1]
            fechaCreacion = objPasswordCompleto[2]

            objPassword = ModelPassword.get_password(idObjPassword)
            objDetalle = ModelDetalle.get_detalle(idObjDetalle)

            objPasswordCompleto = PasswordCompleto(id, objPassword, objDetalle)
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
                    query = f'''SELECT id, password_id, detalle_id, fecha_creacion
                                    FROM password_detalle
                                    WHERE baja=False'''
                    cursor.execute(query)
                    all_passwords = cursor.fetchall()

                for password in all_passwords:
                    idObjPaswordCompleto = password[0]
                    idObjPassword = password[1]
                    idObjDetalle = password[2]
                    fechaCreacion = password[3]

                    objPassword = ModelPassword.get_password(idObjPassword)
                    objDetalle = ModelDetalle.get_detalle(idObjDetalle)

                    objPasswordCompleto = PasswordCompleto(idObjPaswordCompleto, objPassword, objDetalle)
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
                    query = f'''UPDATE password_detalle
                                SET baja=True
                                WHERE id=\'{id}\''''
                    cursor.execute(query)
                    row_afecteds = cursor.rowcount()
            if row_afecteds:
                return id
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

                    transaccionUpdatePassword = ModelPassword.update_password(obj_password_completo.obj_password)
                    cursor.execute(transaccionUpdatePassword[0], transaccionUpdatePassword[1])

                    transaccionUpdateDetalle = ModelDetalle.update_detalle(obj_password_completo.obj_detalle_password)
                    cursor.execute(transaccionUpdateDetalle[0], transaccionUpdateDetalle[1])

            return obj_password_completo.id
        except Exception as ex:
            raise Exception(ex)


if __name__ == '__main__':




    # método get_all funciona
    all_passwords = ModelPasswordCompleto.get_all_password_completo()
    print(all_passwords)


    
