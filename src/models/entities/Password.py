from werkzeug.security import gen_salt


class Password:
    def __init__(self, id, password):
        self._id = id
        self._password = password
        self._clave = None

    @classmethod
    def generate_key(cls):
        return str(gen_salt(36))

    def to_json(self):
        return {
            'password': self.password,
        }

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    @property
    def clave(self):
        return self._clave

    @clave.setter
    def clave(self, clave):
        self._clave = clave

    def is_valid(self):
        password = self.password
        if (len(password) <= 36) and (type(password) == str):
            return True
        else:
            return False
