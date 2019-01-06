# 短信逻辑代码
- __目录 /iHome-python/ihome/libs__  

```python
|-- __init__.py
`-- yuntongxun
    |-- CCPRestSDK.py       # SDK文件
    |-- __init__.py         # 让文件成为python包的形式
    |-- sms.py              # 实际调用文件-在这里配置文件
    |-- xmltojson.py
    `-- \346\216\245\345\217\243\350\257\264\346\230\216.txt  # 接口说明


# sms.py 就是下载SDK里面的demo文件:SendTemplateSMS.py 主要就是这个文件
```
- __sms.py__  

```python
# coding=utf-8

from CCPRestSDK import REST

#主帐号
accountSid= ''

#主帐号Token
accountToken= ''

#应用Id
appId=''

#请求地址，格式如下，不需要写http://
serverIP='app.cloopen.com'

#请求端口 
serverPort='8883'

#REST版本号
softVersion='2013-12-26'

  # 发送模板短信
  # @param to 手机号码
  # @param datas 内容数据 格式为数组 例如：['12','34']，如不需替换请填 ''
  # @param $tempId 模板Id

class CCP(object):
    """
    自己封装的发送短信的辅助类
    为什么自己封装?
    避免多次初始化 REST SDK
    """
    # 用来保存对象的类属性
    instance = None

    def __new__(cls):
        # 判断CCP类有没有已经创建好的对象，如果没有，创建一个对象，并且保存
        # 如果有，则将保存的队形直接返回
        if cls.instance is None:
            obj = super(CCP, cls).__new__(cls)

            # 初始化REST SDK
            obj.rest = REST(serverIP, serverPort, softVersion)
            obj.rest.setAccount(accountSid, accountToken)
            obj.rest.setAppId(appId)

            cls.instance = obj

        return cls.instance



    def send_template_sms(self, to, datas, temp_id):
        """
        发送短信模板
        :param to: 用户的手机号
        :param datas:   填充到模板的验证数字
        :param temp_id: 模板的编号
        """
        result = self.rest.sendTemplateSMS(to, datas, temp_id)
        # for k,v in result.iteritems():
            # if k=='templateSMS' :
            #         for k,s in v.iteritems():
            #             print '%s:%s' % (k, s)
            # else:
            #     print '%s:%s' % (k, v)
        # smsMessageSid:fa9c702947c146efa897083a089dea7c
        # dateCreated:20181230145634
        # statusCode:000000
        status_code = result.get("statusCode")
        if status_code == "000000":
            # 表示发送短信成功
            return 0
        else:
            # 表示发送失败
            return -1



# def sendTemplateSMS(to,datas,tempId):
#
#
#     #初始化REST SDK
#     rest = REST(serverIP,serverPort,softVersion)
#     rest.setAccount(accountSid,accountToken)
#     rest.setAppId(appId)
#
#     result = rest.sendTemplateSMS(to,datas,tempId)
#     for k,v in result.iteritems():
#
#         if k=='templateSMS' :
#                 for k,s in v.iteritems():
#                     print '%s:%s' % (k, s)
#         else:
#             print '%s:%s' % (k, v)
    
   
#sendTemplateSMS(手机号码,内容数据,模板Id)
if __name__ == '__main__':
    print(ret)
```