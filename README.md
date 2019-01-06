# Flask-爱家租房网项目
此项目是学习Flask框架时按照传智播客Python教程所学习的项目,该项目按照爱家租房网开发的实际上线项目,实现所有基本功能,采用前后端分离的方式进行开发  
__住:此项目纯属个人学习项目,不作任何商业用途__  
### [项目详细介绍目录](https://github.com/yuanwenq/iHome-python/blob/master/SUMMARY.md)
### 技术栈
python + flask + mysql + redis + celery
### 目标功能
- [x] 功能模块
    - [x] 首页
    - [x] 注册
    - [x] 登录
    - [x] 短信验证
    - [x] 用户退出
    - [x] 个人中心
    - [x] 实名认证
    - [x] 房屋列表
    - [x] 房屋管理
    - [x] 房屋详情
    - [x] 城区信息
    - [x] 发布房源
    - [x] 订单
    - [x] 订单支付
    
### 项目运行  
```python
# 安装项目相关包
pip install -r RequirementDocument.txt

# 模型类迁移
python manage.py db init 初始化数据表
python manage.py db migrate 提交修改 
python manage.py db upgrade 执行修改 
python manage.py db downgrade 回退修改

# 项目启动
python manage.py runserver
```

- [redis文档](redisdoc.com/index.html)
- [redis-py](https://redis-py.readthedocs.io/en/latest/)

