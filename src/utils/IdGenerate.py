from uuid import uuid4


class IdGenerate:

    @classmethod
    def generate_id(cls):
        id = str(uuid4())
        return id
