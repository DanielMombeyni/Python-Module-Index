# encoding: utf-8
name = 'helló wörld from example'
print name.encode('utf8')

# Output
# Traceback (most recent call last):
#   File "main.py", line 3, in <module>
#     print name.encode('utf8')
# UnicodeDecodeError: 'ascii' codec can't decode byte 0xc3 in position 4: ordinal not in range(128)