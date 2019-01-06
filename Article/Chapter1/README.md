# 项目文件目录结构
```
|-- Accompanying-theme-pyCharm.jar          # 我设置的pycharm的主题
|-- Article                                 # gitbook目录文件
|-- LICENSE                                 # MIT许可
|-- README.md                               # 项目介绍目录
|-- RequirementDocument.txt                 # 项目相关安装包
|-- SUMMARY.md                              # gitbook目录
|-- _book                                   # gitbook生成可本地浏览html
|-- book.json                               # gitbook配置文件
|-- config.py                               # 项目配置文件
|-- demo.py
|-- ihome                                   # 项目主要文件
|   |-- __init__.py
|   |-- api_1_0                             # 视图函数文件
|   |   |-- __init__.py                     
|   |   |-- demo.py
|   |   |-- houses.py                       # 房屋相关API
|   |   |-- keys                            # 支付宝秘钥存放文件夹
|   |   |-- orders.py                       # 订单相关API-保存订单-查询订单信息-接单-拒单-订单评论信息
|   |   |-- passport.py                     # 用户相关API-注册-登录-验证
|   |   |-- pay.py                          # 支付相关API-支付宝支付
|   |   |-- profile.py                      # 用户相关信息修改API-头像-名字-个人信息-实名认证
|   |   `-- verify_code.py                  # 验证相关API-图片验证-短信验证
|   |-- constants.py                        # 项目使用的常量
|   |-- libs                                # 第三方文件存放文件夹-短信验证(容联云)
|   |   |-- __init__.py
|   |   `-- yuntongxun
|   |       |-- CCPRestSDK.py               # 容联云PythonSDK
|   |       |-- __init__.py 
|   |       |-- sms.py                      # 容联云配置文件和封装的方法
|   |       |-- xmltojson.py
|   |       `-- \346\216\245\345\217\243\350\257\264\346\230\216.txt
|   |-- models.py                           # ORM-模型类
|   |-- static                              # 静态文件存放目录
|   |-- tasks                               # celery-分布式任务队列
|   |   |-- __init__.py
|   |   |-- config.py
|   |   |-- main.py
|   |   |-- sms
|   |   |   |-- __init__.py
|   |   |   |-- tasks.py
|   |   `-- task_sms.py
|   |-- utils                               # 工具类文件夹
|   |   |-- __init__.py
|   |   |-- captcha                         # 图片验证相关代码
|   |   |   |-- __init__.py
|   |   |   |-- captcha.py
|   |   |   `-- fonts
|   |   |       |-- Arial.ttf
|   |   |       |-- Georgia.ttf
|   |   |       `-- actionj.ttf
|   |   |-- commons.py                      # 公共类方法-定义正则转换器-定义的验证登录状态的装饰器
|   |   |-- image_storrage.py               # 七牛云图片上传相关代码
|   |   `-- response_code.py                # 项目定义返回的规范文件
|   |-- views.py                            
|   `-- web_html.py                         # html返回文件操作
|-- logs                                    # 项目日志
|-- manage.py                               # 项目启动文件
|-- manage_single.py
|-- migrations                              # 模型类迁移文件记录文件
`-- note.txt

```