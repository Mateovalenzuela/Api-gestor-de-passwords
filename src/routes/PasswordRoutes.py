from flask import Blueprint, jsonify, request

# Models
from models.ModelPasswordCompleto import ModelPasswordCompleto

# Entities
from models.entities.Password import Password
from models.entities.Detalle import Detalle
from models.entities.PasswordCompleto import PasswordCompleto

main = Blueprint('password_blueprint', __name__)


@main.route('/')
def get_passwords():
    try:
        passwords = ModelPasswordCompleto.get_all_password_completo()
        return jsonify(passwords)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/<id>')
def get_password(id):
    try:
        if (len(id) == 36) and (type(id) == str):
            password = ModelPasswordCompleto.get_password_completo(id)
            if password is not None:
                return jsonify(password)
            else:
                return jsonify({'message': "Error, password not found"}), 404
        else:
            return jsonify({'message': "Error, id no valid"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/add', methods=['POST'])
def add_password():
    try:
        objPassword = Password(None, request.json['password'])
        objDetalle = Detalle(None, request.json['usuario'], request.json['titulo'], request.json['url'],
                             request.json['descripcion'])

        if objPassword.is_valid() and objDetalle.is_valid():
            objPasswordCompleto = PasswordCompleto(None, objPassword, objDetalle)
            idNewObj = ModelPasswordCompleto.add_password_completo(objPasswordCompleto)

            if len(idNewObj) == 36:
                return jsonify({'message': f'Added password: {idNewObj}'})
            else:
                return jsonify({'message': "Error on insert"}), 500
        else:
            return jsonify({'message': "Error, invalid data"}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/delete/<id>', methods=['DELETE'])
def delete_password(id):
    try:
        if (len(id) == 36) and (type(id) == str):
            idNewObj = ModelPasswordCompleto.delete_password_completo(id)
            if idNewObj is not None:
                return jsonify({'message': f'Deleted password: {idNewObj}'})
            else:
                return jsonify({'message': "No password deleted"}), 404
        else:
            return jsonify({'message': "Error, id no valid"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/update/<id>', methods=['PUT'])
def update_password(id):
    try:
        if (len(id) == 36) and (type(id) == str):
            objPassword = Password(None, request.json['password'])
            objDetalle = Detalle(None, request.json['usuario'], request.json['titulo'], request.json['url'],
                                 request.json['descripcion'])

            if objPassword.is_valid() and objDetalle.is_valid():
                objPasswordCompleto = PasswordCompleto(id, objPassword, objDetalle)
                idNewObj = ModelPasswordCompleto.update_password_completo(objPasswordCompleto)

                if len(idNewObj) == 36:
                    return jsonify({'message': f'Updated passwords: {idNewObj}'})
                else:
                    return jsonify({'message': "No password updated"}), 404
            else:
                return jsonify({'message': "Error, invalid data"}), 404

        else:
            return jsonify({'message': "Error, id no valid"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


