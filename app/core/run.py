# coding=utf-8
from app.core import HTMLTestRunner
import os
import unittest
import time
from app.core.config_parser import  ConfigParse
import os.path

def run():
    config = ConfigParse().getconfig()
    # 设置报告文件保存路径
    report_path = config.get('reports', 'path')
    # 获取系统当前时间
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

    # 设置报告名称格式
    if not os.path.exists(report_path):
        os.mkdir(report_path)
    HtmlFile = report_path + now + "HTMLtemplate.html"
    fp = open(HtmlFile, "wb")

    # 构建suite
    suite = unittest.TestLoader().discover(config.get('testsuites', 'path'))


    # 初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="百度项目测试报告", description="用例测试情况")
    # 开始执行测试套件
    runner.run(suite)
    return now + "HTMLtemplate.html"

