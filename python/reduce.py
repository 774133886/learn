from functools import reduce
def str2float(s):
    li = list(s)
    def getMap(i):
        return i
    def getReduce(x,y):
        if y == '.':
            return int(x)
        elif len(str(x)) == len(s.split('.')[0]):
            return x+int(y)*0.1
        elif len(str(x)) > len(s.split('.')[0]):
            return x+int(y)*pow(0.1,len(str(x))-len(s.split('.')[0]))
        else:
            return int(x)*10+int(y)
    return reduce(getReduce,map(getMap,li))
    

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')    