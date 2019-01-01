# 用户密码加密
- 密码加密的3中方法：
    1. md5
    2. sha1
        - 用户密码 + 盐值,然后后进行sha1加密,形成一个加密密码
        - `例: 密码：123456 + 盐值 abc sha1加密后变成 abc$eignpfgmclskem 这样的一个密文 存储到数据看中` 
    3. sha256
        - sha256就是sha1的升级版,操作的方式类似
        
- 当前项目使用了sha256,具体相关代码:/ihmoe/models.py


```python
# 在User模型类中添加 werkzeug 为我们封装好的sha256加密方法
from werkzeug.security import generate_password_hash, check_password_hash

# 在User模型类中添加以下:
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
```