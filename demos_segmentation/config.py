class Config(object):
    DEBUG = True
    RESTPLUS_VALIDATE = True


class DevConfig(Config):
    pass


class TestConfig(Config):
    pass


class ProdConfig(Config):
    DEBUG = False
