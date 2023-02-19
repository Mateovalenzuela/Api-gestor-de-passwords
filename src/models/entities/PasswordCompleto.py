from src.utils.DateFormat import DateFormat


class PasswordCompleto:
    def __init__(self, id, obj_password, obj_detalle_password):
        self._id = id
        self._obj_password = obj_password
        self._obj_detalle_password = obj_detalle_password
        self._id_password = None
        self._id_detalle_password = None
        self._fecha_creacion = None
        self._baja = False

    def to_json(self):
        return {
            'id': self.id,
            'obj_password': self.obj_password,
            'obj_detalle_password': self.detalle_password,
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
    def obj_detalle_password(self):
        return self._detalle_password

    @obj_detalle_password.setter
    def obj_detalle_password(self, obj_detalle_password):
        self._detalle_password = obj_detalle_password

    @property
    def id_password(self):
        return self._id_password

    @id_password.setter
    def id_password(self, id_password):
        self._id_password = id_password

    @property
    def id_detalle_password(self):
        return self._id_detalle_password

    @id_detalle_password.setter
    def id_detalle_password(self, id_detalle_password):
        self._id_detalle_password = id_detalle_password

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
