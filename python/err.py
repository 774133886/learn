# from functools import reduce
# import logging
# # logging.basicConfig(level=logging.INFO)

# def str2num(s):
#     return int(s)

# def calc(exp):
#     ss = exp.split('+')
#     ns = map(str2num, ss)
#     return reduce(lambda acc, x: acc + x, ns)

# def main():
#     try:
#         r = calc('100 + 200 + 345')
#         print('100 + 200 + 345 =', r)
#         r = calc('99 + 88 + 7.6')
#         print('99 + 88 + 7.6 =', r)
#     except ValueError as e:
#         raise ValueError('invalid value: %s' % e)

# main()

#单元测试
# import unittest

# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#     def get_grade(self):
#         if self.score < 0 or self.score > 100:
#             raise ValueError
#         if self.score >= 80:
#             return 'A'
#         if self.score >= 60:
#             return 'B'
#         return 'C'

# class TestStudent(unittest.TestCase):

#     def test_80_to_100(self):
#         s1 = Student('Bart', 80)
#         s2 = Student('Lisa', 100)
#         self.assertEqual(s1.get_grade(), 'A')
#         self.assertEqual(s2.get_grade(), 'A')

#     def test_60_to_80(self):
#         s1 = Student('Bart', 60)
#         s2 = Student('Lisa', 79)
#         self.assertEqual(s1.get_grade(), 'B')
#         self.assertEqual(s2.get_grade(), 'B')

#     def test_0_to_60(self):
#         s1 = Student('Bart', 0)
#         s2 = Student('Lisa', 59)
#         self.assertEqual(s1.get_grade(), 'C')
#         self.assertEqual(s2.get_grade(), 'C')

#     def test_invalid(self):
#         s1 = Student('Bart', -1)
#         s2 = Student('Lisa', 101)
#         with self.assertRaises(ValueError):
#             s1.get_grade()
#         with self.assertRaises(ValueError):
#             s2.get_grade()

# if __name__ == '__main__':
#     unittest.main()


#文档测试
def fact(n):
    '''
    Calculate 1*2*...*n

    >>> fact(1)
    1
    >>> fact(10)
    3628800
    >>> fact(-1)
    Traceback (most recent call last):
    ...
    ValueError
    '''
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n - 1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()