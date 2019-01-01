# coding=utf-8

from CCPRestSDK import REST

#主帐号
accountSid= '8aaf070867e8660f0167fdc0b2700b7e'

#主帐号Token
accountToken= 'beb1548364064eb0965f2d7c1a82471b'

#应用Id
appId='8aaf070867e8660f0167fdc0b2cd0b85'

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
        """"""
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
    ccp = CCP()
    ret = ccp.send_template_sms("13534755504", ["1234", "5"], 1)
    print(ret)