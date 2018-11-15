
from xml.parsers.expat import ParserCreate
from urllib import request
from enum import Enum

city = ''
class DefaultSaxHandler(object):
    def __init__(self):
        self.data = {
            'city': '',
            'forecast': []
        }
    def start_element(self, name, attrs):
        if name == 'yweather:location' and attrs['city']:
            self.data['city'] = attrs['city']
        if name == 'yweather:forecast' and attrs['date']:
            obj = {}
            obj['date'] = dateFormat(attrs['date'])
            obj['high'] = attrs['high']
            obj['low'] = attrs['low']
            self.data['forecast'].append(obj)
        # print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        # print('sax:end_element: %s' % name)
        pass
    def char_data(self, text):
        # print('sax:char_data: %s' % text)
        pass
    def getCity(self):
        return self.data

#日期格式化

def dateFormat(datestr):
    listInfo = datestr.split()

    #枚举类
    Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
    listInfo[1] = str(Month[listInfo[1]].value)
    return '-'.join(listInfo[::-1])

def parseXml(xml_str):
    handler = DefaultSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    # parser.Parse(xml_str)
    
    print(parser.Parse(xml_str))
    return handler.getCity()


# 测试:
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'

with request.urlopen(URL, timeout=4) as f:
    data = f.read()

result = parseXml(data.decode('utf-8'))
assert result['city'] == 'Beijing'
