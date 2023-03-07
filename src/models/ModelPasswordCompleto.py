import uuid

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

                    transaccionAddDetalle = ModelDetalle.add_detalle(obj_password_completo.obj_detalle)
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

                    query = f'''SELECT password_detalle.id, detalle.usuario, detalle.titulo, detalle.url, 
                    detalle.descripcion, pgp_sym_decrypt(password.password::bytea, (password.clave)) AS password, 
                    password_detalle.fecha_creacion
                                FROM password_detalle
                                INNER JOIN detalle
                                ON password_detalle.detalle_id = detalle.id
                                INNER JOIN password
                                ON password_detalle.password_id = password.id
                                WHERE password_detalle.baja = false AND password_detalle.id = \'{id}\';'''
                    cursor.execute(query)
                    resulset = cursor.fetchone()

            objDetalle = Detalle(None, resulset[1], resulset[2], resulset[3], resulset[4])
            objPassword = Password(None, resulset[5])
            objPasswordCompleto = PasswordCompleto(resulset[0], objPassword, objDetalle)
            objPasswordCompleto.fecha_creacion = resulset[6]

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

                    query = '''SELECT password_detalle.id, detalle.usuario, detalle.titulo, detalle.url, 
                    detalle.descripcion, pgp_sym_decrypt(password.password::bytea, (password.clave)) AS password, 
                    password_detalle.fecha_creacion
                                FROM password_detalle
                                INNER JOIN detalle
                                ON password_detalle.detalle_id = detalle.id
                                INNER JOIN password
                                ON password_detalle.password_id = password.id
                                WHERE password_detalle.baja = false;'''

                    cursor.execute(query)
                    all_passwords = cursor.fetchall()

                for resulset in all_passwords:
                    objDetalle = Detalle(None, resulset[1], resulset[2], resulset[3], resulset[4])
                    objPassword = Password(None, resulset[5])
                    objPasswordCompleto = PasswordCompleto(resulset[0], objPassword, objDetalle)
                    objPasswordCompleto.fecha_creacion = resulset[6]

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
                    row_afecteds = cursor.rowcount
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
                    query = f'''SELECT password_id, detalle_id FROM password_detalle
                                WHERE id=\'{obj_password_completo.id}\''''
                    cursor.execute(query)
                    resulset = cursor.fetchone()

                    obj_password_completo.obj_password.id = resulset[0]
                    obj_password_completo.obj_detalle.id = resulset[1]

                    transaccionUpdatePassword = ModelPassword.update_password(obj_password_completo.obj_password)
                    cursor.execute(transaccionUpdatePassword[0], transaccionUpdatePassword[1])

                    transaccionUpdateDetalle = ModelDetalle.update_detalle(obj_password_completo.obj_detalle)
                    cursor.execute(transaccionUpdateDetalle[0], transaccionUpdateDetalle[1])

            return obj_password_completo.id
        except Exception as ex:
            raise Exception(ex)


if __name__ == '__main__':
    id = 'c3e855c9-1e84-4943-9c9d-27fc50ee8d38'
    lista = ModelPasswordCompleto.get_all_password_completo()
    #id = ModelPasswordCompleto.delete_password_completo('46c7079c-d024-42fa-9bb8-391a929030f9')
    print(lista)
    #idObjPassword = '4de53f0a-7be0-41bb-9d2a-6f58978705d7'

    #objPassword = Password(None, 'ZANAORIA10')
    #objDetalle = Detalle(None, 'mateovalenzuela773@gmail.com', 'gmail')
    #objPasswordCompleto = PasswordCompleto(idObjPassword, objPassword, objDetalle)


    # idNewObj = ModelPasswordCompleto.update_password_completo(objPasswordCompleto)




    #get one
    #newPassword = ModelPasswordCompleto.get_password_completo(idNewObj)
    #print(newPassword)

    # método get_all funciona
    # all_passwords = ModelPasswordCompleto.get_all_password_completo()
    # print(all_passwords)


    
