# coding=UTF-8

import string
def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

"""
测试一段文本是否是回文
并去掉标点符号
带分号输入内容
"""
something = input("enter text :")
something_new = ''
for i in something:
    if i not in string.punctuation:
        something_new = i +something_new
print(something)
print(something_new)
if is_palindrome(something_new):
    print("yes, it is a palindrome")
else:
    print("no, it is not a palindrome")

