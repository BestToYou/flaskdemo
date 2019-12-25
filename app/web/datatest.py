from flask import render_template
from  . import web


@web.route('/', methods=['GET', 'POST'])
def send_drift():
    return "sadsa"



@web.route('/review')
def review():
    # 传入一个网址
    my_url = 'www.baidu.com'
    # 传入一个列表
    my_list = [1,2,3,4,5,6]
    # 传入一个字典
    my_dict = {"name":'哈哈韩',"age":34}
    # 传入一个整数
    my_int = 890
    return render_template('test.html',
                           url = my_url,
                           list = my_list,
                           dict = my_dict,
                           int = my_int,
                           )
