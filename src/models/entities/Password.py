from src.utils.DateFormat import DateFormat

class Password:
    def __init__(self, id, usuario, password, titulo="", url="", descripcion=""):
        self._id = id
        self._usuario = usuario
        self._password = password
        self._titulo = titulo
        self._url = url
        self._descripcion = descripcion
        self._fecha_creacion = None
        self._baja = False

    def to_JSON(self):
        return {
            'id': self.id,
            'usuario': self.usuario,
            'password': self.password,
            'titulo': self.titulo,
            'url': self.url,
            'descripcion': self.descripcion,
            'fecha_creacion': DateFormat.convert_date(self.fecha_creacion),
            'baja': self.baja,
        }

    @property
    def id(self):
        return self._id

    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self, usuario):
        self._usuario = usuario

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        self._url = url

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, descripcion):
        self._descripcion = descripcion

    @property
    def fecha_creacion(self):
        return self._fecha_creacion

    @fecha_creacion.setter
    def fecha_creacion(self, fecha_creacion):
        self._fecha_creacion = fecha_creacion

    @property
    def baja(self):
        return self._baja

    @baja.setter
    def baja(self, baja: bool):
        self._baja = baja
