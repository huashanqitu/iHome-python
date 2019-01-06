# 开发流程与接口文档编写
- __开发流程__
    1. 分析需求
    2. 编写代码
    3. 编写单元测试
    4. 自测
    5. 编写接口文档
    6. 提测代码
- __接口文档__
    1. 接口名字
    2. 描述(描述清楚接口的功能)
    3. url
    4. 请求方法
    5. 传入参数
    6. 返回值
- 示例：  
    接口:获取图片验证码  
    描述:前端访问,可以获取到验证码图片
    url：/api/v1.0/image_codes/<image_code_id>  
    请求方式：GET    
    传入参数(表格):    
    `格式: 路径参数 (参数是查询字符串, 请求的表单, json, xml)`  
    |名字|类型|是否必须|说明|  
    |------|------|------|------|  
    |image_code_id|字符串|是|验证码图片的编号|
      
    返回值：   
    `格式： 正常：图片， 异常：json`   
    |名字|类型|是否必须|说明|  
    |error|字符串|否|错误代码|  
    |errmsg|字符串|否|错误代码|  
    
    实例：  
    ```
    '{"errno":"4001", "errmsg":"保存图片验证码失败"}'
    ```
        