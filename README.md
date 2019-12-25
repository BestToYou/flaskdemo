# flaskdemo
This is a demo


用到的库和类型为
flask =='0.12.2'.
flask_script.
flask_migrate.
pymysql.
flask_sqlalchemy 
主分支上的代码不进行修改 ，仅仅为 flask项目刚开始的一个框架


dev分支的代码进行一系列的更新 ，增加api或者其他的操作



#主分支模板说明
app 为所有的大部分文件所在文件夹 


 models 创建 数据库对应关系 其中 init这个文件必须，引入新创建的类，不然不会在数据库中生成
 
 
  static静态文件的存放地址 
  
  templates 网页模板的存放地址
  
  web 里面为处理网页访问的功能
  
  secure 数据库设置 等其他设置
  
  setting 也是设置 ，为一些网站功能的一些设置 
  
  init在这个文件中 可以注册一些蓝图，蓝图的定义在 web下的 init文件夹
  
 
 dzc.py为一些 flaskscript 和migrate模块的运用 写在下方
 
 
 
 
 
 ####################################
 
 当第一次运行本项目 ，数据库 和环境安装完成后
 
 python dzc.py db init  初始化数据库
  python dzc.py db migrate 生成最初的迁移
  
  python dzc.py db upgrade  数据库进行更新
  
  
  在models有所改动时 要执行 migrate 和upgrade上面的两条语句
  
  
  #####################
 


