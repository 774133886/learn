
import re

def is_valid_email(addr):
    ts = r'^[0-9a-zA-Z\.]+\@+[0-9a-zA-Z-]+.com$'
    if re.match(ts,addr):
        return True
    else:
        return False
# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert is_valid_email('a.bill.gates@microsoft.com')
assert is_valid_email('01.bill.gates@microsoft.com')
assert is_valid_email('98bill.gates@microsoft.com')
assert is_valid_email('j9asd.asd9f08.98j.bill.gates@microsoft.com')
assert is_valid_email('1@q.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
assert not is_valid_email('mrbob@.com')
assert not is_valid_email('mrbob@.com.')
assert not is_valid_email('mrbob@com.')
assert not is_valid_email('@a.com')
assert not is_valid_email('x@a.com.')
assert not is_valid_email('@a.com')
print('ok')