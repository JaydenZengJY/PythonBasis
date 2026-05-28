print("这是demo1作为模块会显示的内容")
def test():
    print('HAHA')
if __name__ == "__main__": #被当作模块导入时，下面的代码不会被显示出来
    print('这是demo1作为模块不会显示的内容')