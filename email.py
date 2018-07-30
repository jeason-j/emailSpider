# -*- coding: utf-8 -*-
# @Time    : 2018/7/27 14:49
# @Author  : ll
# @Email   : @126.com
# @Project : email.py
# @File    : email爬虫.py
# @function：

# 注意pycharm中环境设置
# 增加了 自动翻页，write 时，使用‘a’ 写入文件方式

import requests  
import re


def get_email(url):
    """get all the email address from the url"""  
    content = requests.get(url).text  
    pattern = r'[0-9a-zA-Z._]+@[0-9a-zA-Z._]+\.[0-9a-zA-Z._]+'  
    p = re.compile(pattern)  
    m = p.findall(content)  
    with open('email.txt', 'a') as f:
        for mm in m:  
            f.write(mm+'\n')  
    ''''' 
    with open('tmp.html', 'w') as f: 
        f.writelines(content) 
    '''


if __name__ == '__main__':
    url = 'https://tieba.baidu.com/p/5805152471?pn=1'
    for i in range(10):
        url = 'https://tieba.baidu.com/p/5805152471?pn=' + str(i)
        print('获取第' + str(i + 1) + '页...')
        get_email(url)
    print('执行完成!~')

