# fpath = r'./python/test.txt'

# with open(fpath, 'r', encoding='utf-8') as f:
#     s = f.read()
#     print(str(s))


#OS
import os,shutil
# os.path.abspath('.')
# path = os.path.join('./python/testdir','test.py')

# 编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。

def getDir(path='.',search=''):
    li = []
    host = os.path.abspath(path)
    for item in os.listdir(host):
        files = os.path.join(host,item)
        if search in item:
            if search == '':
                li.append(files)
            else:
                li.append(files)
        if os.path.isdir(files):
            li += getDir(files,search)
    return li

if __name__ == '__main__':
    print(getDir(search='.txt'))
