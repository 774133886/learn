
import json


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)

def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

# print(json.dumps(s, default=student2dict))
print(json.dumps(s, default=lambda obj : obj.__dict__))




# obj = dict(name='小明', age=20)
# s = json.dumps(obj, ensure_ascii=True)

# print(s)