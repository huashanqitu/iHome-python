# coding:utf-8
# 配置信息
# 开发环境 和 生产环境
import redis

class Config(object):
    """配置信息"""


    SECRET_KEY = "ADSFE5*ad4f8843e5f1654s5"

    # 数据库
    SQLALCHEMY_DATABASE_URI = "mysql://root:123qwe@127.0.0.1:3306/ihome_pthon04"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # redis
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    # flask-session配置
    SESSION_TYPE = 'redis'
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    SESSION_USE_SIGNER = True  # 对cookie中session_id进行隐藏处理
    PERMANENT_SESSION_LIFETIME = 86400  # sessoin数据的有效期，单位秒


class DevelopmentConfig(Config):
    """开发模型配置信息"""
    DEBUG = True


class ProductConfig(Config):
    """生产环境配置信息"""
    pass


# 名字与类的对应关系

config_map = {
    "develop": DevelopmentConfig,
    "product": ProductConfig
}