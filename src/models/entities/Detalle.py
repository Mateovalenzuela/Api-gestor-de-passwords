
class Detalle:
    def __init__(self, id, usuario, titulo="", url="", descripcion=""):
        self._id = id
        self._titulo = titulo
        self._usuario = usuario
        self._url = url
        self._descripcion = descripcion

    def to_json(self):
        return {
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

    def is_valid(self):
        titulo = self.titulo
        usuario = self.usuario
        url = self.url
        descripcion = self.descripcion

        if (len(titulo) <= 20) and (type(titulo) == str):
            tituloValido = True
        else:
            tituloValido = False

        if (len(usuario) <= 50) and (type(usuario) == str):
            usuarioValido = True
        else:
            usuarioValido = False

        if (len(url) <= 250) and (type(url) == str):
            urlValido = True
        else:
            urlValido = False

        if (len(descripcion) <= 100) and (type(descripcion) == str):
            descripcionValido = True
        else:
            descripcionValido = False

        if tituloValido and usuarioValido and urlValido and descripcionValido:
            return True
        else:
            return False
