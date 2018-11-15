import base64

def safe_base64_decode(s):
    res = s + b'=' * (len(s)%4)
    resB64 = base64.urlsafe_b64decode(res)
    return resB64


# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')