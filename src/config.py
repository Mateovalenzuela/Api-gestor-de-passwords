
class Config:
    FLASK_APP = "app"
    SECRET_KEY = "P4SSWOR1*_?"


class DevelopmentConfig(Config):
    DEBUG = True


config = {
    'development': DevelopmentConfig
}
