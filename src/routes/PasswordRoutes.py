from flask import Blueprint, jsonify, request

# Models
from src.models.ModelPassword import ModelPassword

# Entities
from src.models.entities.Password import Password

main = Blueprint('password_blueprint', __name__)


@main.route('/')
def get_passwords():
    try:
        passwords = ModelPassword.get_passwords()
        return jsonify(passwords)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/<id>')
def get_password(id):
    try:
        password = ModelPassword.get_password(id)
        if password is not None:
            return jsonify(password)
        else:
            return jsonify({'message': "Error, password not found"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/add', methods=['POST'])
def add_password():
    try:
        usuario = request.json['usuario']
        password = request.json['password']
        titulo = request.json['titulo']
        url = request.json['url']
        descripcion = request.json['descripcion']
        objPassword = Password(None, usuario, password, titulo, url, descripcion)

        affectedRows = ModelPassword.add_password(objPassword)
        if affectedRows:
            return jsonify({'message': f'Added passwords: {affectedRows}'})
        else:
            return jsonify({'message': "Error on insert"}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/delete/<id>', methods=['DELETE'])
def delete_password(id):
    try:
        objPassword = Password(id, None, None)
        affectedRows = ModelPassword.delete_password(objPassword)

        if affectedRows:
            return jsonify({'message': f'Deleted passwords: {affectedRows}'})
        else:
            return jsonify({'message': "No password deleted"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/update/<id>', methods=['PUT'])
def update_password(id):
    try:
        usuario = request.json['usuario']
        password = request.json['password']
        titulo = request.json['titulo']
        url = request.json['url']
        descripcion = request.json['descripcion']

        objPassword = Password(id, usuario, password, titulo, url, descripcion)

        affectedRows = ModelPassword.update_password(objPassword)
        if affectedRows:
            return jsonify({'message': f'Updated passwords: {affectedRows}'})
        else:
            return jsonify({'message': "No password updated"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


