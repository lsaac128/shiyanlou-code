class BaseConfig(object):
    '''配置基类'''
    SECRET_KEY = 'makesure to set a very secret key'

class DevelopmentConfig(BaseConfig):
    '''开发环境配置'''
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root:Wl19891208@localhost/simpledu?charset=utf8'

class ProductionConfig(BaseConfig):
    '''生产环境配置'''
    pass

class TestingConfig(BaseConfig):
    pass

configs = {
    'development' : DevelopmentConfig,
    'production' : ProductionConfig,
    'testing' : TestingConfig
}