# -*- coding:utf-8 -*-

from datetime import datetime
from . import db
from werkzeug.security import generate_password_hash, check_password_hash


class BaseModel(object):
    """模型基类，为每个模型补充创建时间与更新时间"""

    create_time = db.Column(db.DateTime, default=datetime.now)  # 记录的创建时间
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)  # 记录的更新时间


class User(BaseModel, db.Model):
    """用户"""

    __tablename__ = "ih_user_profile"

    id = db.Column(db.Integer, primary_key=True)  # 用户编号
    name = db.Column(db.String(32), unique=True, nullable=False)  # 用户暱称
    password_hash = db.Column(db.String(128), nullable=False)  # 加密的密码
    mobile = db.Column(db.String(11), unique=True, nullable=False)  # 手机号
    real_name = db.Column(db.String(32))  # 真实姓名
    id_card = db.Column(db.String(20))  # 身份证号
    avatar_url = db.Column(db.String(128))  # 用户头像路径
    houses = db.relationship("House", backref="user")  # 用户发布的房屋
    orders = db.relationship("Order", backref="user")  # 用户下的订单

    # 加上property装饰器后，会把函数变为属性，户属性名即为函数名
    @property
    def password(self):
        """读取属性的函数行为"""
        # print(user.password)  读取属性时被调用
        # 函数的返回值会作为属性值
        # return "xxx"
        raise AttributeError("这个属性只能设置,不能读取")

    # 使用这个装饰器,对应设置属性操作
    @password.setter
    def password(self, value):
        """
        设置属性  user.password = "xxx"
        :param value: 设置属性时候的数据 value就是"xxxx", 原始明文密码
        :return:
        """
        self.password_hash = generate_password_hash(value)

    # def generate_password_hash(self, origin_password):
    #     """对密码进行加密"""
    #     self.password_hash = generate_password_hash(origin_password)

    def check_password(self, passwd):
        """
        检验密码正确性
        :param passwd:  用户登录时填写的原始密码
        :return:  如果正确返回True 否则返回 False
        """
        return check_password_hash(self.password_hash, passwd)


class Area(BaseModel, db.Model):
    """城区"""

    __tablename__ = "ih_area_info"

    id = db.Column(db.Integer, primary_key=True)  # 区域编号
    name = db.Column(db.String(32), nullable=False)  # 区域名字
    houses = db.relationship("House", backref="area")  # 区域的房屋


# 房屋设施表，建立房屋与设施的多对多关系
house_facility = db.Table(
    "ih_house_facility",
    db.Column("house_id", db.Integer, db.ForeignKey("ih_house_info.id"), primary_key=True),  # 房屋编号
    db.Column("facility_id", db.Integer, db.ForeignKey("ih_facility_info.id"), primary_key=True)  # 设施编号
)


class House(BaseModel, db.Model):
    """房屋信息"""

    __tablename__ = "ih_house_info"

    id = db.Column(db.Integer, primary_key=True)  # 房屋编号
    user_id = db.Column(db.Integer, db.ForeignKey("ih_user_profile.id"), nullable=False)  # 房屋主人的用户编号
    area_id = db.Column(db.Integer, db.ForeignKey("ih_area_info.id"), nullable=False)  # 归属地的区域编号
    title = db.Column(db.String(64), nullable=False)  # 标题
    price = db.Column(db.Integer, default=0)  # 单价，单位：分
    address = db.Column(db.String(512), default="")  # 地址
    room_count = db.Column(db.Integer, default=1)  # 房间数目
    acreage = db.Column(db.Integer, default=0)  # 房屋面积
    unit = db.Column(db.String(32), default="")  # 房屋单元， 如几室几厅
    capacity = db.Column(db.Integer, default=1)  # 房屋容纳的人数
    beds = db.Column(db.String(64), default="")  # 房屋床铺的配置
    deposit = db.Column(db.Integer, default=0)  # 房屋押金
    min_days = db.Column(db.Integer, default=1)  # 最少入住天数
    max_days = db.Column(db.Integer, default=0)  # 最多入住天数，0表示不限制
    order_count = db.Column(db.Integer, default=0)  # 预订完成的该房屋的订单数
    index_image_url = db.Column(db.String(256), default="")  # 房屋主图片的路径
    facilities = db.relationship("Facility", secondary=house_facility)  # 房屋的设施
    images = db.relationship("HouseImage")  # 房屋的图片
    orders = db.relationship("Order", backref="house")  # 房屋的订单


class Facility(BaseModel, db.Model):
    """设施信息"""

    __tablename__ = "ih_facility_info"

    id = db.Column(db.Integer, primary_key=True)  # 设施编号
    name = db.Column(db.String(32), nullable=False)  # 设施名字


class HouseImage(BaseModel, db.Model):
    """房屋图片"""

    __tablename__ = "ih_house_image"

    id = db.Column(db.Integer, primary_key=True)
    house_id = db.Column(db.Integer, db.ForeignKey("ih_house_info.id"), nullable=False)  # 房屋编号
    url = db.Column(db.String(256), nullable=False)  # 图片的路径


class Order(BaseModel, db.Model):
    """订单"""

    __tablename__ = "ih_order_info"

    id = db.Column(db.Integer, primary_key=True)  # 订单编号
    user_id = db.Column(db.Integer, db.ForeignKey("ih_user_profile.id"), nullable=False)  # 下订单的用户编号
    house_id = db.Column(db.Integer, db.ForeignKey("ih_house_info.id"), nullable=False)  # 预订的房间编号
    begin_date = db.Column(db.DateTime, nullable=False)  # 预订的起始时间
    end_date = db.Column(db.DateTime, nullable=False)  # 预订的结束时间
    days = db.Column(db.Integer, nullable=False)  # 预订的总天数
    house_price = db.Column(db.Integer, nullable=False)  # 房屋的单价
    amount = db.Column(db.Integer, nullable=False)  # 订单的总金额
    status = db.Column(  # 订单的状态
        db.Enum(
            "WAIT_ACCEPT",  # 待接单,
            "WAIT_PAYMENT",  # 待支付
            "PAID",  # 已支付
            "WAIT_COMMENT",  # 待评价
            "COMPLETE",  # 已完成
            "CANCELED",  # 已取消
            "REJECTED"  # 已拒单
        ),
        default="WAIT_ACCEPT", index=True)
    comment = db.Column(db.Text)  # 订单的评论信息或者拒单原因
