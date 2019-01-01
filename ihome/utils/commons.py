# coding: utf-8

from werkzeug.routing import BaseConverter
from flask import session, jsonify, g
from ihome.utils.response_code import RET
import functools

# 定义正则转换器
class ReConverter(BaseConverter):
    """"""
    def __init__(self, url_map, regex):
        # 调用父类的初始化方法
        super(ReConverter, self).__init__(url_map)
        # 保存正则表达式
        self.regex = regex


# 定义的验证登录状态的装饰器
def login_required(view_func):

    @functools.wraps(view_func)
    def wrapper(*args, **kwargs):
        # 判断用户的登录状态
        user_id = session.get("user_id")

        # 如果用户是登录的,执行试图函数
        if user_id is not None:
            # 将user_id保存到g对象中,在视图函数中可以通过g对象获取保存数据
            # g对象就是中间人,游走在各个视图函数
            g.user_id = user_id
            return view_func(*args, **kwargs)
        else:
            # 如果未登录,返回未登录的信息
            return jsonify(errno=RET.SESSIONERR, errmsg="用户未登录")

    return wrapper


# @login_required
# def set_user_avatar():
