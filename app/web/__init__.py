from flask import Blueprint
#蓝图的注册


#一下为 web蓝图的注册 在下方可以找到，至于为什么在init这个文件中引入 from  app.web import datatest
#因为 如果不进行引入 在运行flask时无法找到 datatest 这个文件
web = Blueprint('web',__name__)
from  app.web import datatest