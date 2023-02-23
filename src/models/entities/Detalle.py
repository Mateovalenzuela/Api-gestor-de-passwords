
class Detalle:
    def __init__(self, id, usuario, titulo="", url="", descripcion=""):
        self._id = id
        self._titulo = titulo
        self._usuario = usuario
        self._url = url
        self._descripcion = descripcion

    def to_json(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'usuario': self.usuario,
            'url': self.url,
            'descripcion': self.descripcion
        }

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo

    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self, usuario):
        self._usuario = usuario

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        self._url = url

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, descripcion):
        self._descripcion = descripcion
