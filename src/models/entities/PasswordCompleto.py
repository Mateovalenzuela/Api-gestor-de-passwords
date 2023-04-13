from utils.DateFormat import DateFormat


class PasswordCompleto:
    def __init__(self, id, obj_password, obj_detalle):
        self._id = id
        self._obj_password = obj_password
        self._obj_detalle = obj_detalle
        self._id_password = None
        self._id_detalle = None
        self._fecha_creacion = None
        self._baja = False

    def to_json(self):
        return {
            'id': self.id,
            'password': self.obj_password.password,
            'titulo': self.obj_detalle.titulo,
            'usuario': self.obj_detalle.usuario,
            'url': self.obj_detalle.url,
            'descripcion': self.obj_detalle.descripcion,
            'fecha_creacion': DateFormat.convert_date(self.fecha_creacion),
        }

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def obj_password(self):
        return self._obj_password

    @obj_password.setter
    def obj_password(self, obj_password):
        self._obj_password = obj_password

    @property
    def obj_detalle(self):
        return self._obj_detalle

    @obj_detalle.setter
    def obj_detalle(self, obj_detalle):
        self._obj_detalle = obj_detalle

    @property
    def id_password(self):
        return self._id_password

    @id_password.setter
    def id_password(self, id_password):
        self._id_password = id_password

    @property
    def id_detalle(self):
        return self._id_detalle

    @id_detalle.setter
    def id_detalle(self, id_detalle):
        self._id_detalle = id_detalle

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
