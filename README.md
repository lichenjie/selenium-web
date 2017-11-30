# selenium-web启动

1.pip install -r requirement.txt 安装依赖包，使用的是python3环境

2.在selenium-web目录下新建logs文件夹

3.python3 manage.py runserver 启动服务器

该项目继承了selenium自动化测试的框架，可以在app/core/pageobjects中加入需要测试的页面，在app/core/testsuites中设计测试案例
另浏览器驱动在bin目录下，需要自行导入驱动。

项目演示地址：http://un.jacklibra.cn/