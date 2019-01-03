# coding:utf-8

from ihome.tasks.main import celery_app
from ihome.libs.yuntongxun.sms import CCP

@celery_app.task
def send_sms(to, datas, temp_id):
    """发送短信的异步任务"""
    ccp = CCP()
    ccp.send_template_sms(to, datas, temp_id)