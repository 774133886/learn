# class Student(object):
#     def __init__(self, name, gender):
#         self._name = name
#         self._gender = gender
#     def get_gender(self):
#         return self._gender
#     def set_gender(self,gender):
#         if gender in ['male', 'female']:
#             self._gender = gender
#         else:
#             raise ValueError('bad gender')

# # 测试:
# bart = Student('Bart', 'male')
# if bart.get_gender() != 'male':
#     print('测试失败!')
# else:
#     bart.set_gender('female')
#     if bart.get_gender() != 'female':
#         print('测试失败!')
#     else:
#         print('测试成功!')

# class Student(object):
#     count = 0

#     def __init__(self, name):
#         Student.count += 1
#         self.name = name

# # 测试:
# if Student.count != 0:
#     print('测试失败!')
# else:
#     bart = Student('Bart')
#     if Student.count != 1:
#         print('测试失败!')
#     else:
#         lisa = Student('Bart')
#         if Student.count != 2:
#             print('测试失败!')
#         else:
#             print('Students:', Student.count)
#             print('测试通过!')


class Screen(object):
    
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,value):
        self._width = value
    
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,value):
        self._height = value
    
    @property
    def resolution(self):
        return self._width*self._height

# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')

class Chain(object):

    def __init__(self, path=''):
        self.__path = path

    def __getattr__(self, item):
        return Chain('{}/{}'.format(self.__path, item))

    def __str__(self):
        return self.__path

    __repr__ = __str__

    def __call__(self, param):
        return Chain('{}/{}'.format(self.__path, param))

    __repr__ = __str__
Chain().users('michael').repos